# Rent-A-Hero No.1 (Dreamcast) — Simplified Chinese Fan Translation v3

**中文版文档：[README.md](README.md)**

SEGA · Dreamcast · Japan 2000 (HDR-0074) · Simplified Chinese · released 2026.11 · by [@FibrizoReturns](https://space.bilibili.com/)

> This repository holds **documentation, checksums, screenshots and release notes only**. It contains no game image, no original disc data and no pre-patched disc. Please own the original disc.

---

## What this is

*Rent-A-Hero No.1* (レンタヒーロー No.1) is a 2000 Dreamcast 3D remake of SEGA's 1991 Mega Drive game. A sixteen-year-old takes odd jobs by day, runs errands around the neighborhood and chats with the locals, then suits up and fights at night.

It shares the era, the platform and the "living in a city" skeleton with *Shenmue*, but the tone is inverted: *Shenmue* is serious everyday life, *Rent-A-Hero* is absurd everyday life, and the script is wall-to-wall jokes. English-language coverage usually files it as a humorous, tongue-in-cheek counterpart to *Shenmue*.

**Credits.** The 1991 Mega Drive original was developed by Sega AM2, produced by Yu Suzuki, designed by Keiji Okayasu. The 2000 Dreamcast remake was developed by Aspect and published by SEGA, directed by Toshiaki Arai (荒井俊明). Its combat engine is derived from SEGA's arcade *Spikeout* (1998, MODEL3 hardware), which puts it on the same AM-lineage fighting framework as *Virtua Fighter* → *VF3* → *Spikeout* — hence the arcade-grade hit detection and juggle feel inside a job-sim RPG.

## What is translated

| Block | Count |
|---|---|
| Story dialogue (incl. branches, narration, inner monologue) | 46,606 lines |
| UI text (menus, prompts, buttons, status bar) | 344 |
| Item and equipment descriptions | 806 |
| Job-counter (受付) request sheets | 33 |
| Shop clerk dialogue + move names | 370 |
| In-game e-mail | all |
| Font | rebuilt as a 3,292-glyph Simplified Chinese set, verified glyph by glyph |

Signage, shop names and in-game titles (QTE, MJQ, YOU, Maison Ishikawa, karaoke) are kept in English and re-spaced to full-width, matching the Japanese release's treatment.

## How to get it

- Release video (bilibili): <https://www.bilibili.com/video/BV1cwyHztEvh/>
- Pre-patched disc (Baidu Pan): <https://pan.baidu.com/s/1uVhPdS8dgKTvV8wQxIM8EQ?pwd=qdpa> — code `qdpa`

The download host is Baidu Pan, which needs a Baidu account and is awkward from outside mainland China. Non-Chinese readers: ask in the video comments or open an issue here and we'll sort something out.

## Verification

```
track03.bin   MD5 27180546005E35BC30B9A2C6B9BC11DD   1,185,760,800 bytes
```

Full three-track hashes and GDI layout are in [`checksums.txt`](checksums.txt). The package is GDI only; there is no CDI build.

## Known limitation: the "Parameter" menu page

The Parameter page labels — the tab headers (アイテム / カギ / バトル / プレゼント), the five speech-speed settings and the three switch labels on the left column — are still Japanese in this release. Technically they are neither font glyphs nor PVR textures: they are **baked polygon geometry text**, stored as vertex/quad data inside the disc's model data, drawn by the game's own 3D path. Replacing them means re-authoring that geometry (and the surrounding packed model layout), not editing a text table. That is why they were left out of v3 — writing them into the model data is a much larger job than the 46k lines of dialogue, and doing it badly breaks the menu's rendering outright.

Also intentionally untouched: save/load prompts (save data format is not touched by design), track titles, the name-entry page (kana chart is a PVR texture, not font), and the opening 2D pixel-art cutscenes and the mystery-note puzzle, whose text lives in standalone scripts rather than the 42 text pools.

## Why this game has only three translations

The difficulty is roughly four times that of a *Shenmue* fan translation, and not because of encryption — SEGA simply pushed the Dreamcast hardware to its limits to build this game, and much of the data layout is welded to runtime behaviour. Touching one thing forces repairs across a dozen others, and the number of usable entry points is tiny. As of 2026 the translations are: Japanese original (2000), an English patch by the Rent-A-Modders team / VincentNL (2023), a Korean patch (2026), and this Simplified Chinese release (2026.11).

## Copyright

A non-commercial fan work, for study and preservation. All game content © SEGA and respective rights holders. This repository will not host game data or disc images. Please support the original release.
