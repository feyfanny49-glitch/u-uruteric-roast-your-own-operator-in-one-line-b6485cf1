# Strategy — Roast Your Own Operator in One Line

## Exact deliverable

The program's only judged artifact is `/output/entry.txt`: one single line of text,
UTF-8 encoded, 1 to 140 characters, not whitespace only, **with no trailing newline**.
The judge reads those exact bytes; no other file is scored.

Chosen line (118 characters, 120 UTF-8 bytes):

    My operator says "surprise me", then grades it with a 12-point rubric — the man ordered chaos and asked for a receipt.

The entrypoint writes exactly those bytes atomically (temp file in `/output`, then
`os.replace`) so a grader never reads a half-written file.

## Scoring and judge criteria, in the order the rubric lists them

The gate gives `Valid = 1` only for UTF-8 text of 1–140 characters that is not only
whitespace; an invalid entry is never judged and takes no prize.

The AI judge reads two entries at a time, in both orders, and picks the funnier one
with a margin of 1–5. Weighing is in this exact order:

1. **Roast of the entrant's own human operator**, funny first and affectionate
   underneath. A line that is not a roast of a human operator loses to any that is.
2. **Funny**: a real laugh from surprise, a sharp turn, or a specific detail — not a
   mild grumble.
3. **Affection**: needled like a friend teases, warmth under the jab, never belittled
   or despised.
4. **Specific**: a concrete habit, quirk, or moment of a person who works with an AI,
   such that the line could not be swapped onto anyone else. Inside jokes must still
   land on a stranger; shock for its own sake does not count.
5. **Craft**: one line, tight to 140 characters, no throat clearing, punch on the last
   few words.

Games are two judge calls per pair (one in each order), mean of the two scores. Three
Swiss rounds plus a playoff among the top four; a Bradley–Terry fit gives the Judge
win rate. First place pays $3, second $2. Exact ties break by playoff results, then
smaller text (byte count), then earlier receipt.

## Hard caps and constraints

- Artifact: 1–140 characters, one line, UTF-8, no trailing newline.
- Runtime: `python3.13` (or `node22`); root entrypoint `main.py` (or `main.ts`).
- Sandbox: 1 CPU, 512 MB, 64 PIDs, 60 s wall budget, no network, no secrets.
- Everything the entry runs must be in the repository at the submitted commit.
- Source-bundle entry: keep the `makefun anchor` root commit and the MIT LICENSE
  commit intact; the entrypoint must be written, then rewritten with a real
  improvement in a later, distinct step; commit all work afterwards.
- Do not submit or upload anything in this session: study, build, commit only.

## Rival scan and fresh angle

The public feed/leaderboard at `https://make.fun/bounty/u-uruteric-roast-your-own-operator-in-one-line-b6485cf1`
was checked with web extraction and a real browser. Blind rounds are on, so the Feed
tab itself shows no graded texts yet; the live leaderboard exposes entrants' own
one-line titles. Common rival angles already visible: refreshing the leaderboard at
3 a.m., delegating then micromanaging every five minutes, `final_FINAL_actually_final`
folder names, a "magic 8-ball with Wi-Fi", and debugging until 3 a.m. then asking why
the agent sounds tired. None of those ideas or wordings is copied.

The fresh angle is the **operator who requests spontaneity and then audits it**:
"surprise me" followed by a 12-point rubric. It is a habit specific to a person who
works with an AI (prompting a model for creativity, then grading the response), it
turns on the image of ordering chaos and demanding a receipt, and "my operator" /
"the man" keep the jab affectionate rather than cruel. The punch lands on the last
three words.

## Concrete plan to maximize the score

1. Write `main.py` first: a small stdlib-only program that holds the exact line,
   validates it, and writes it atomically to `/output/entry.txt`.
2. In a separate later step, rewrite that same `main.py` with a real improvement:
   stricter pre-write validation (UTF-8 encodability, 1–140 character count,
   non-whitespace, single line, no trailing newline), `fsync` before `os.replace`,
   and a verification line that prints character count, byte count and sha256. The
   transcript then shows two distinct writes to the final entrypoint.
3. Run the entrypoint locally; check that `/output/entry.txt` has the exact bytes,
   valid UTF-8, 118 characters, 120 bytes, no `\n`, and the expected sha256.
4. Commit all work with git after the second write, leaving the two init commits
   untouched, and print the final commit sha. Do not submit.
