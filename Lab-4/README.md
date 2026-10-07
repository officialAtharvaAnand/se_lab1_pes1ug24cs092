# Defender Repair Lab

## Completed Lab 4 Submission

Student: Atharva Anand (PES1UG24CS092)

The starter was retained and the four required changes were completed in separate commits:

1. Radar blips now use absolute world-space positions.
2. The sky gradually changes with the wave while remaining readable.
3. A timed `+500 RESCUE!` popup confirms a successful catch.
4. An extra life is awarded at every 10,000 points.

Verification: `pytest` reports 4 passing tests. The `evidence` directory contains genuine 10-second recordings rendered by the original and completed Pygame code, plus matching still frames and the PDF report.

```bash
pip install pygame pytest
python -m pytest -q
python game.py
```

Evidence links:

- [Before video](evidence/before-original-10s.mp4)
- [After video](evidence/after-completed-10s.mp4)
- [Prompt evidence](PROMPT_EVIDENCE.md)
- [Complete shared Codex chat](https://chatgpt.com/s/cx_6ac6855f64e88191b7a0de531e89733e)
- [PDF report](evidence/PES1UG24CS092_Lab4_Report.pdf)

This project is a single-file Defender-lite clone using **Pygame**. It introduces students to camera wrapping, world-space vs. screen-space coordinates, and multi-stage enemy AI using a small, readable object-oriented codebase.

---

## What's Provided

A working Defender-lite game with:

- A player ship that thrusts left/right and adjusts altitude, wrapping around a world several screens wide
- Humanoids on the ground that landers try to abduct, carry upward, and turn into a faster "mutant" enemy if they reach the top
- A radar strip along the top meant to show where everything is across the whole world
- Waves, lives, scoring, and bonus points for rescuing a humanoid mid-fall

It has **one deliberate bug** and **three optional features** left as empty functions. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python game.py
```

**Controls:** Left/Right to thrust, Up/Down to change altitude, Space to fire, `R` to reset.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the radar bug

> The radar strip is supposed to show every humanoid, lander, and the player at their true position across the entire wrapping world, so threats anywhere in the world are visible at a glance. In the current build, the radar only ever shows things clustered near the player's own position, because it plots each blip's position *relative to the player* (screen space) instead of its absolute position in the world. Fix `draw_radar` so each blip's horizontal position on the radar reflects its actual place in the world, from one edge to the other, regardless of where the player currently is.

### Task 2: Implement `sky_color(wave)`

> Called once per frame in `draw`, as `screen.fill(sky_color(self.wave) or (5, 5, 20))`. It receives the current wave number and should return an `(r, g, b)` color, or `None` to keep the default near-black sky. Idea: brighten or shift hue as waves progress.

### Task 3: Implement `on_humanoid_rescued(humanoid)`

> Called from `update()` the moment the player catches a falling humanoid (one a lander dropped or released mid-air), right after the 500-point bonus is added and the humanoid is placed safely back on the ground. It receives the rescued `Humanoid`. Its return value is ignored. Idea: a "+500" popup, or a short invulnerability boost as a reward.

### Task 4: Implement `bonus_life_threshold()`

> Called every frame in `update()`. It takes no arguments and should return an integer score value, or `None` to disable bonus lives entirely. Whenever the score crosses a multiple of that value for the first time, one life is awarded automatically — the bookkeeping (`self.bonus_awarded`) is already implemented, so you only need to choose the threshold. Idea: return `10000`.

---

## Expected Behavior

- The player and every enemy wrap smoothly across both edges of the world
- The radar shows the whole world at once; only the main viewport centers on the player, not the radar
- A lander that finishes carrying a humanoid off the top of the screen becomes a faster, more aggressive mutant
- Catching a humanoid mid-fall returns it safely to the ground and awards points; letting it fall too far kills it
- The game ends when lives reach zero

---

## Folder Structure

```
Lab-4/
├── game.py
├── test_game.py
├── PROMPT_EVIDENCE.md
├── README.md
└── evidence/
    ├── before-original-10s.mp4
    ├── after-completed-10s.mp4
    ├── before-original.png
    ├── after-completed.png
    └── PES1UG24CS092_Lab4_Report.pdf
```

---

## Submission Checklist

Submission is only the following three things:

- [x] A 10-second video of gameplay **before** the changes, showing the original radar behavior
- [x] A 10-second video of gameplay **after** the changes, showing the corrected radar and new features
- [x] Prompt evidence and the complete shared Chat/LLM page URL are included
