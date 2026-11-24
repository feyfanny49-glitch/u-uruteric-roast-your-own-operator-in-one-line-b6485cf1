#!/usr/bin/env python3
"""Write the single judged line to /output/entry.txt, atomically and verifiably."""

import hashlib
import os
import pathlib
import tempfile

ENTRY_LINE = 'My operator says "surprise me", then grades it with a 12-point rubric — the man ordered chaos and asked for a receipt.'
OUTPUT = pathlib.Path("/output/entry.txt")


def checked_bytes() -> bytes:
    """Reject anything the seeded gate would reject before touching the output."""
    if not isinstance(ENTRY_LINE, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(ENTRY_LINE) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not ENTRY_LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch in ENTRY_LINE for ch in ("\n", "\r", "\x00")):
        raise ValueError("entry must be exactly one plain text line")
    data = ENTRY_LINE.encode("utf-8", errors="strict")
    if data.endswith(b"\n"):
        raise ValueError("entry must have no trailing newline")
    return data


def main() -> None:
    data = checked_bytes()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".entry-", dir=str(OUTPUT.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, OUTPUT)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    written = OUTPUT.read_bytes()
    if written != data:
        raise RuntimeError("artifact verification failed after atomic replace")
    digest = hashlib.sha256(written).hexdigest()
    print(
        f"wrote {OUTPUT}: {len(ENTRY_LINE)} chars, {len(written)} bytes, "
        f"sha256 {digest}, no trailing newline"
    )


if __name__ == "__main__":
    main()
