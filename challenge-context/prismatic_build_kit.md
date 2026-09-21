# Prismatic App Build Kit (Amazon Quick & PartyRock)

This build kit contains the finalized assets, widget parameters, copy-paste prompts, and pitch scripts for **Prismatic**.

---

## ⚡ Quick-Start: The Master Seed Prompt

Copy this exact prompt into **Amazon Quick** (`Apps` mode) or **PartyRock**:

```text
Build a web application called "Prismatic" that solves academic fragmentation by refracting complex college topics into 4 distinct learning modalities based on a 5-question cognitive diagnostic.

Include the following connected widgets:
1. User Input (multiline text) for pasting lecture notes, topics, or study materials.
2. User Input / Form for a 30-second 5-question diagnostic (learning preference, cognitive roadblocks, exam countdown, quiz style, and tutor persona).
3. Text generation widget that outputs a Cognitive Spectrum Profile and custom study plan based on the inputs.
4. Text generation widget providing an intuitive, plain-English college/dorm life analogy of the concept.
5. Text generation widget rendering a structured ASCII flowchart or concept map of the topic.
6. Chatbot widget configured as a Socratic sparring partner that tests the student one practice question at a time.
7. Image generation widget creating a vibrant visual memory anchor illustration of the topic.

Make the UI clean, modern, dark-mode inspired, and tailored for college students preparing for midterms and finals.
```

---

## 🧩 Widget Connection Map

| Widget ID | Name | Role | Upstream Dependency |
| :--- | :--- | :--- | :--- |
| **Widget 1** | `TopicInput` | User pastes notes/concept | *None (User Input)* |
| **Widget 2** | `DiagnosticMatrix` | 5 Quick questions | *None (User Form)* |
| **Widget 3** | `CognitiveProfile` | Personalized diagnostic roadmap | `@TopicInput`, `@DiagnosticMatrix` |
| **Widget 4** | `AnalogyExplainer` | Modality 1: Dorm/Campus Analogy | `@TopicInput` |
| **Widget 5** | `ConceptMap` | Modality 2: ASCII/Mermaid Schema | `@TopicInput` |
| **Widget 6** | `SocraticChat` | Modality 3: Interactive Quizzing | `@TopicInput`, `@DiagnosticMatrix` |
| **Widget 7** | `MemoryImage` | Modality 4: AI Visual Infographic | `@TopicInput` |

---

## 🎤 The 2-Minute Shark Tank Pitch Script

* **[0:00 - 0:25] The Hook**:
  > *"Every semester, 300 students sit in the exact same lecture hall, listening to the exact same professor, looking at the exact same slides. Yet half the room walks out confident, while the other half walks out completely lost. Why? Because white light contains every color, but a flat wall only sees one shade. Traditional lectures teach everyone one way, even though human brains process information in completely different spectrums."*

* **[0:25 - 0:50] The Solution (Introducing Prismatic)**:
  > *"We built **Prismatic**. Prismatic is an agentic learning engine that refracts any dense lecture slide, syllabus, or exam topic into your brain's native cognitive spectrum. In under 30 seconds, 5 diagnostic micro-questions identify whether you think in analogies, structural schematics, Socratic dialogue, or visual anchors."*

* **[0:50 - 1:30] The Live Product Walkthrough**:
  > *"Here it is running live on Amazon Quick: Paste in something notoriously brutal like Dijkstra's Algorithm or Cellular Respiration. For our visual thinkers, Prismatic renders an interactive concept flowchart. For conceptual learners, it translates the logic into how students navigate rush hour at the campus dining hall. And for exam-night crammers, our Socratic sparring chatbot immediately fires off targeted edge-case questions with zero fluff."*

* **[1:30 - 2:00] The Shark Tank Close**:
  > *"Private tutoring costs $80 an hour. Campus office hours are packed. Prismatic democratizes personalized, multi-modal mastery for every student on campus with zero friction. We are Prismatic—refracting complex knowledge into your native spectrum. Thank you!"*
