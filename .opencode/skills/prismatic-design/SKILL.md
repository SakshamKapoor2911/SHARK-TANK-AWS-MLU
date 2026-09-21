---
name: prismatic-design
description: Prismatic Obsidian Neon design system — canonical color tokens, typography, accessibility, and print rules for web-app/styles.css, build_prismatic_deck.py, and build_talking_points_pdf.py. Use when editing any Prismatic visual theme, slide styling, PDF styling, or adding UI components.
---

# Prismatic Design Skill

Single source of truth for every Prismatic surface. When visuals drift between
the web app, the pitch deck, and the printed cue cards, this file wins.

## 1. Canonical tokens — Executive theme (do not invent new hues)

The project migrated from Obsidian Neon to the MatrAIx executive palette.
These values are authoritative across all surfaces:

| Token     | Hex       | Usage                              |
| --------- | --------- | ---------------------------------- |
| `bg`      | `#0B0E14` | screen canvas                      |
| `card`    | `#131822` | elevated cards                     |
| `inner`   | `#1A202E` | inset panels, pills                |
| `hover`   | `#222B3D` | hover fills                        |
| `border`  | `#2B3C55` | subtle lines                       |
| `primary` | `#4A8FC2` | phosphor blue, executive primary   |
| `mint`    | `#00C49F` | metrics, success, focus rings      |
| `violet`  | `#A855F7` | spectral accent                    |
| `amber`   | `#F59E0B` | warnings, timing, traps            |
| `coral`   | `#EF4444` | alerts, trap radar                 |
| `ink`     | `#FFFFFF` / `#E8E9EC` | headings / body on dark   |
| `muted`   | `#A0A8B4` | secondary text on dark             |
| `dim`     | `#78808E` | captions                           |

CSS variables in `web-app/styles.css`, hardcoded hexes in `web-app/app.js`
(SVG nodes, edges, legends), RGB constants in `build_prismatic_deck.py`,
and the print accents in `build_talking_points_pdf.py` must carry identical
hex values. Check all four files when changing any token. Variable names
like `--cyan-neon` are legacy aliases — they now resolve to executive hues.

## 2. Screen vs. print (deliberate split, not drift)

- **Screen** (web app, PPTX): dark executive theme.
- **Print** (`PRESENTER_TALKING_POINTS.pdf`): light theme, dark ink on white —
  projectors and printers punish dark fills. Never "unify" print to dark.
  Print accents stay in the executive family (`#4A8FC2` banners, `#00C49F`
  highlights, slate body text).

## 3. Hard rules for any UI change

1. **Min sizes**: body copy ≥ 10.5pt (deck/PDF) or ≥ 0.8rem (web); footers and
   metadata may go smaller. Back-row readability beats density.
2. **Focus visible**: every keyboard-operable element — including `div[role=button]`
   like `.trap-card` — gets a cyan `:focus-visible` ring. The selector must name
   them explicitly; `button/input` coverage alone is not enough.
3. **Reduced motion**: any `transition`/`animation` in CSS ships with a
   `@media (prefers-reduced-motion: reduce)` block that disables it.
4. **No clipping**: deck textboxes use word-wrap + shrink-to-fit; web panels use
   wrapping layouts down to 360px. Never let text overflow a card on projector.
5. **Scannable QR**: dark modules on white with a full quiet zone, NEAREST
   resampling. On-brand low-contrast QR codes fail under stage lighting.
6. **No import-time side effects** in builder scripts: directory creation, QR
   generation, and COM imports belong inside functions, with graceful fallbacks.
7. **XSS-safe rendering**: dynamic strings go through escaping before `innerHTML`.
   Style changes must not reintroduce unescaped interpolation.

## 4. Verification after any theme edit

- `python build_prismatic_deck.py` exits 0; PPTX is 4 slides at 13.33×7.5 in.
- PDF + 4 slide PNGs regenerate; QR tile scans from a phone.
- CSS edits: balanced braces, 360px layout intact, focus rings visible by keyboard.
- Commit theme + regenerated artifacts together so previews never go stale.
