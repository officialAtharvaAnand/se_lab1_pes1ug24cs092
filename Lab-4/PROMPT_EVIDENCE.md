# Lab 4 AI Interaction Evidence

## Tool used

OpenAI Codex was used as an AI pair-programming assistant for analysis, implementation, testing, evidence generation, documentation, and repository publication.

## Actual prompt used

The initial request asked the assistant to complete the SE vibe-coding assignment using the supplied Defender starter repository, provide guidance about the required recordings, prepare the evidence, and publish the result to the student's SE GitHub repository.

That single request authorized the complete workflow. The assistant then decomposed the work into the four tasks from the starter README, implemented each task in a separate commit, ran automated tests, generated genuine before/after evidence from the two code versions, and prepared the report.

## Review trail

The critical review performed during the workflow included:

- checking that radar blips are calculated from `x / WORLD_W` rather than the player-centred `screen_x` value;
- capping the sky-color progression so RGB values stay readable and valid;
- confirming the rescue popup has a finite timer and disappears;
- confirming the bonus-life threshold is exactly 10,000;
- running `pytest` and Python bytecode compilation;
- visually inspecting the rendered before and after frames;
- verifying the Git history contains a separate commit for every task.

## Complete chat evidence

Complete shared Codex chat: <https://chatgpt.com/s/cx_6ac686f4ed6881918b32d7a8212516b9>

The shared history is the authoritative record of the prompt and the assistant's responses; this summary does not replace it.

## Academic-integrity note

This file records AI assistance rather than presenting the implementation as unaided work. The student should understand and be able to explain the world-space radar mapping, timed rescue feedback, wave-color calculation, and bonus-life rule during evaluation.
