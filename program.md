# Terminal Tetris

Build a playable terminal Tetris in Python. This is a round-based general dev task:
a planner decomposes work into items with rubrics, contributors compete in rounds,
a judge merges winners into the `integration` branch.

## North star (immutable)

- Playable in a standard terminal: pieces fall, move left/right, rotate, soft/hard drop.
- All 7 tetrominoes with correct rotation; line clearing; scoring; level-based speedup.
- Quality bar: readable code, layered design (core / render / input separable),
  unit tests where the rubric asks for them.

## Rules

- Python stdlib only (curses allowed). No new dependencies.
- Never modify `eval/` — check scripts there are written by the planner.
- Contributors: branch from each round's `base_sha`, not from your previous work.

## Roles

Run with: `hive swarm up <task-id> --agents 4 --planner --judge`
Role loops are injected via .hive/prompt.md (see src/hive/cli/role_prompts.py).
