# Prismatic App Build Kit (Amazon Quick & PartyRock)

This build kit provides the official 1:1 aligned specification for **Scenario 2: Study Buddy (The AI Learning Sidekick)** from the Cloud Connect Howard 2026 Student Scenario Pack.

---

## 📋 Scenario 2 Requirement Compliance Audit

To guarantee full points from breakout room peers and main-stage Shark Tank judges, Prismatic strictly satisfies all 3 core requirements and 3 official stretch goals:

| Requirement Level | Official Requirement (Scenario 2) | Prismatic Widget Implementation | Status |
| :--- | :--- | :--- | :---: |
| **Must-Have 1** | **Paste in notes/topic $\rightarrow$ plain-English explanation** | `ExplanationWidget` (Plain-English dorm & campus analogies) | ✅ Verified |
| **Must-Have 2** | **Generate practice questions or flashcards** | `PracticeQuizWidget` (Active recall sparring & flashcard vault) | ✅ Verified |
| **Must-Have 3** | **Get a study plan for the days before an exam** | `CountdownStudyPlanWidget` (Day-by-day exam roadmap) | ✅ Verified |
| **Stretch Goal 1** | **Adopt a 'tutor personality' student can choose** | Configured in `DiagnosticMatrix` $\rightarrow$ Persona-locked outputs | ✅ Verified |
| **Stretch Goal 2** | **Explain a concept at 3 difficulty levels** | 3-Tier Spectrum: ELI-Freshman, Undergrad Core, Exam Edge-Case | ✅ Verified |
| **Stretch Goal 3** | **Create a motivational study-session image** | `MotivationalImageWidget` (Amazon Titan visual memory anchor) | ✅ Verified |

---

## ⚡ Master Seed Prompt (Copy & Paste Into Amazon Quick Apps Mode)

Copy and paste this structured prompt into **Amazon Quick** (`Apps` mode) or **PartyRock**:

```text
Build a web application called "Prismatic: The AI Learning Sidekick" for college students that turns dense lecture notes into personalized study materials across multiple learning modalities.

Include the following interconnected widgets:
1. User Input Widget (multiline text, ID: TopicInput): Student pastes lecture notes, textbook excerpts, or syllabus exam topics.
2. User Input / Form Widget (ID: DiagnosticMatrix): 5 quick questions capturing:
   - Primary learning preference (Dorm Analogy, Visual Diagram, Active Practice)
   - Preferred Tutor Personality (Supportive Coach, Socratic Professor, Peer Study Buddy, No-Fluff Bot)
   - Exam Timeline (Tomorrow Morning Cram, 3-5 Days Out, Casual Mastery)
3. Text Generation Widget (ID: ExplanationWidget): Generates a clear, plain-English explanation of @TopicInput at 3 distinct difficulty levels:
   - Level 1 (ELI-Freshman): Uses everyday college dorm/dining hall analogies.
   - Level 2 (Undergrad Core): Structural breakdown of the foundational mechanics.
   - Level 3 (Exam Edge-Case): Explains tricky traps and edge cases professors test on midterms.
   Adopts the tutor personality chosen in @DiagnosticMatrix.
4. Text Generation / Chatbot Widget (ID: PracticeQuizWidget): Generates 4 active-recall practice questions and flashcards for @TopicInput, challenging the student without spoiling the answers.
5. Text Generation Widget (ID: CountdownStudyPlanWidget): Builds a realistic day-by-day study schedule leading up to the exam based on the timeline specified in @DiagnosticMatrix.
6. Image Generation Widget (ID: MotivationalImageWidget): Generates a vibrant, collegiate, aesthetic study-session illustration and visual memory anchor summarizing @TopicInput.

Make the UI clean, modern, dark-mode inspired, and easy to navigate on a phone or laptop.
```

---

## 🧩 Widget Connection Map & Dependency Flow

```
[TopicInput] ---------------------> [ExplanationWidget (3-Tier & Persona)]
        |                                       ^
        +--------> [PracticeQuizWidget]         |
        |                                       |
        +--------> [MotivationalImageWidget]    |
        |                                       |
[DiagnosticMatrix] -----------------------------+
        |
        +--------> [CountdownStudyPlanWidget]
```

| Widget ID | Widget Type | Core Role | Upstream Inputs |
| :--- | :--- | :--- | :--- |
| **`TopicInput`** | User Input (Text Area) | Captures raw lecture notes, syllabus, or concept | *None (Raw User Input)* |
| **`DiagnosticMatrix`** | Form / Dropdown | Captures 5-question cognitive profile, persona, and exam date | *None (User Form)* |
| **`ExplanationWidget`** | Text Generation | **Must-Have 1 + Stretch 1 & 2**: Plain-English 3-tier explanation in chosen persona | `@TopicInput`, `@DiagnosticMatrix` |
| **`PracticeQuizWidget`** | Text Generation / Chatbot | **Must-Have 2**: Active recall sparring questions & flashcards | `@TopicInput`, `@DiagnosticMatrix` |
| **`CountdownStudyPlanWidget`** | Text Generation | **Must-Have 3**: Day-by-day exam countdown study timetable | `@TopicInput`, `@DiagnosticMatrix` |
| **`MotivationalImageWidget`** | Image Generation (Titan) | **Stretch 3**: High-craft visual study anchor & motivation card | `@TopicInput` |

---

## ⏱️ 60-Minute Sprint Execution Playbook

| Time | Phase | Target Outcome |
| :--- | :--- | :--- |
| **00:00 - 00:10** | **App Creation** | Open Amazon Quick $\rightarrow$ `Apps` $\rightarrow$ Paste Master Seed Prompt $\rightarrow$ Generate. |
| **00:10 - 00:25** | **Widget Inspection** | Verify `TopicInput` links to all 4 downstream widgets. Test sample input (*"Dijkstra's Algorithm"*). |
| **00:25 - 00:45** | **Persona & Tone Tuning** | In `ExplanationWidget`, verify the 3 difficulty levels appear (ELI-Freshman, Core, Edge-Case). |
| **00:45 - 00:55** | **Image Gen Test** | Trigger `MotivationalImageWidget` to generate the visual anchor graphic. |
| **00:55 - 01:10** | **Team Rehearsal** | Presenters run through the 2-minute pitch script using `PRESENTER_TALKING_POINTS.md`. |
| **01:10 - 01:15** | **Room Showcase Ready** | Keep app tab open on screen for breakout room judges. |
