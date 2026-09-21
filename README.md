# Shark Tank App-Build Challenge — AWS x MLU Fall Symposium

Welcome to the **Shark Tank App-Build Challenge** repository for the **Cloud Connect — Howard 2026** symposium (AWS × MLU × BEN Tech × Howard University).

This repository stores all challenge context, scenario breakdowns, rubric definitions, and tooling guidelines to support builders, mentors, and judges.

---

## 📁 Repository Structure

```text
SHARK-TANK-AWS-MLU/
├── README.md                                    # Repository index and architectural overview
├── PRESENTER_TALKING_POINTS.md                  # Verbatim 2-min timed script, pivots, choreography & Q&A
├── PRESENTER_TALKING_POINTS.pdf                 # Portable 2-page print-ready cue card PDF (via ReportLab)
├── build_talking_points_pdf.py                  # Portable ReportLab script generating the 2-page PDF
├── build_prismatic_deck.py                      # Multi-platform 16:9 widescreen PPTX/PDF/PNG generator
├── Prismatic_Shark_Tank_Pitch_Deck.pptx         # Executive PowerPoint Presentation with integrated speaker notes
├── Prismatic_Shark_Tank_Pitch_Deck.pdf          # High-resolution PDF export for mobile, tablet, or projector display
├── web-app/                                     # Zero-dependency, offline-ready glassmorphic web app
│   ├── index.html                               # Semantic, accessible HTML structure
│   ├── styles.css                               # Obsidian Neon responsive styling (down to 360px mobile)
│   ├── app.js                                   # Multi-modal engine, safe XSS escaping & DeepSeek V4 integration
│   └── config.local.js.example                  # Template for optional Live AI API key
├── assets/
│   ├── prismatic_github_qr.png                  # Glowing neon QR code pointing to live repo
│   └── slides/                                  # 1080p slide images for visual reviews
│       ├── slide_1.png                          # Slide 1: Title & The 35-Second Hook
│       ├── slide_2.png                          # Slide 2: Segment 3 - App Overview (4 Spectrums)
│       ├── slide_3.png                          # Slide 3: Segment 4 - Why It Wins ($80/hr Gap)
│       └── slide_4.png                          # Slide 4: Segment 5 - The Close & Shark Criteria
└── challenge-context/
    ├── event_overview.md                        # Challenge rules, timetable, tooling, and flow
    ├── scenarios.md                             # In-depth breakdown of all 5 student challenge scenarios
    ├── scenarios.json                           # Machine-readable scenario database (for skills & automations)
    ├── rubric_framework.md                      # Scoring pillars, 1-5 scale rubrics, and judge criteria
    ├── undergrad_problems_and_ideas_2026.md      # Unfinalized brainstorm of 2026 undergrad pain points & concepts
    ├── amazon_quick_setup_guide.md              # Setup, access methods, and sprint guide for Amazon Quick & PartyRock
    ├── agentic_learning_multimodal_plan.md      # Deep architectural blueprint for 4-modality diagnostic engine
    ├── prismatic_build_kit.md                   # Scenario 2 aligned seed prompt, widget map, and 60-min sprint guide
    ├── prismatic_extended_modalities.md         # Slide decks, Socratic sparring, exam trap matrix, and flashcards
    ├── prismatic_presentation_materials.md      # 2-minute timed pitch, 10-person role cards, 4-slide deck, and Q&A defense
    └── official_presentation_master_playbook.md # Exact official handout 5-segment breakdown and voting playbook
```

---

## 🎯 Event Summary at a Glance

| Item | Details |
| :--- | :--- |
| **Event** | Cloud Connect — Howard 2026: Shark Tank App-Build Challenge |
| **Partners** | AWS, Amazon MLU (Machine Learning University), BEN Tech, Howard University |
| **Date & Location** | September 21–22, 2026 • Howard University (D.C.) & Amazon HQ2 (Arlington, VA) |
| **Team Size** | ~10 students per team |
| **Sprint Window** | 60–75 minutes |
| **Platform** | **Amazon Quick** (`Apps` mode recommended; `Chat` alternative; **PartyRock** fallback) |
| **Pitch Format** | 2-minute overview per team (Team name + core functionality; no live demo required) |
| **Advancement** | Breakout room peer vote $\rightarrow$ Room Champions advance to Main-Stage Final |

---

## 🚀 The 5 Challenge Scenarios

1. **[Scenario 1: Fuel Up: Healthy Eating Coach](challenge-context/scenarios.md#scenario-1-fuel-up-healthy-eating-coach)** (*Wellness • Nutrition*)  
   Help students eat healthily on dorm food, dining-hall options, and tight budgets without shame.
2. **[Scenario 2: Study Buddy: The AI Learning Sidekick](challenge-context/scenarios.md#scenario-2-study-buddy-the-ai-learning-sidekick)** (*Academics • Productivity*)  
   Demystify complex lecture materials, generate flashcards/quizzes, and structure exam countdown plans.
3. **[Scenario 3: Money Moves: Student Budget Planner](challenge-context/scenarios.md#scenario-3-money-moves-student-budget-planner)** (*Finance • Life Skills*)  
   Track income and expenses, calibrate flexible monthly budgets, and answer student money questions.
4. **[Scenario 4: Campus Compass: Navigate College Life](challenge-context/scenarios.md#scenario-4-campus-compass-navigate-college-life)** (*Community • Belonging*)  
   Guide incoming/freshman students to clubs, events, campus traditions, and administrative resources.
5. **[Scenario 5: Balance: Wellness & Stress Companion](challenge-context/scenarios.md#scenario-5-balance-wellness--stress-companion)** (*Mental Health • Wellbeing*)  
   Provide empathetic stress check-ins, guided micro-resets, and campus wellness resource navigation.

---

## ▶️ Run the Live Demo

No build step, no dependencies, no `.env` file. The demo is a static
three-file web app (`web-app/index.html` + `styles.css` + `app.js`) that runs
100% offline in any modern browser.

**Option A — Zero setup (recommended for stage):**

```text
Double-click web-app/index.html
```

That's it. Presets, diagnostic, all 4 spectrums, Socratic sparring, and the
120-second pitch timer work with no network.

**Option B — Local server (presentation cart / projector):**

```powershell
cd web-app
python -m http.server 8000
# open http://localhost:8000
```

**Option C — Live AI mode (optional DeepSeek upgrade):**

1. Click **⚡ Live AI Settings** in the app header.
2. Paste a DeepSeek API key → saved to browser `localStorage` only.
   *Or* copy `web-app/config.local.js.example` → `web-app/config.local.js`
   (git-ignored, never committed) and add the key + optional `partyRockUrl`.
3. The status badge flips to **⚡ Live DeepSeek V4 Engine Active**.
   Without a key, the deterministic offline engine runs — nothing breaks.

**Do we need a `.env`? No.** Browsers can't read `.env`, and committing one
with a real key would leak it to a public repo. Secrets stay in
`localStorage` or the git-ignored `config.local.js`. Verified: no `sk-`
keys exist in any tracked file.

**Pitch-time runbook (2 minutes):**

1. Open the app + `Prismatic_Shark_Tank_Pitch_Deck.pptx` side by side.
2. Hit **Start Pitch** in the cue-bar timer — segment chips light in real time.
3. Walk presets: Dijkstra → Respiration → Macro. Invite a judge to paste
   custom notes and hit **Refract** (auto-mapped visual graph).
4. If Wi-Fi dies: everything above still works offline. If a PartyRock URL is
   configured, the **PartyRock Fallback ↗** link appears in the cue bar.

Regenerate all artifacts with:

```powershell
python build_prismatic_deck.py        # PPTX + PDF + assets/slides/*.png
python build_talking_points_pdf.py    # PRESENTER_TALKING_POINTS.html + .pdf
```

---

## 🛠️ Next Steps & Extensions

With this foundation established, we can build:
- **Custom Agent Skills**: Interactive app prompt generators for Amazon Quick/PartyRock, pitch script creators, and scenario advisors.
- **Rubrics & Audit Systems**: Automated judges and peer evaluation sheets.
- **Team Builder Instructions**: Step-by-step mentor checklists for 60-minute build sprints.
