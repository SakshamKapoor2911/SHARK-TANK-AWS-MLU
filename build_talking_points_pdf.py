import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "PRESENTER_TALKING_POINTS.html"
PDF_PATH = BASE_DIR / "PRESENTER_TALKING_POINTS.pdf"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Prismatic: Presenter Talking Points & Sprint Playbook</title>
<style>
  @page {
    size: letter portrait;
    margin: 0.42in 0.48in;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.35;
    font-size: 8.6pt;
    background: #ffffff;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page-container {
    page-break-after: always;
  }
  .page-container:last-child {
    page-break-after: avoid;
  }
  .header-banner {
    background: linear-gradient(135deg, #0b0e14 0%, #131822 100%);
    color: #ffffff;
    border-radius: 6px;
    padding: 9px 13px;
    margin-bottom: 7px;
    border-left: 4px solid #4a8fc2;
  }
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2px;
  }
  .brand-title {
    font-size: 13.5pt;
    font-weight: 800;
    letter-spacing: 0.05em;
    color: #ffffff;
  }
  .event-tag {
    font-size: 7.5pt;
    font-weight: 700;
    color: #00c49f;
    background: #1a202e;
    padding: 2px 8px;
    border-radius: 12px;
    border: 1px solid #2b3c55;
  }
  .header-sub {
    font-size: 7.8pt;
    color: #a0a8b4;
    line-height: 1.3;
  }
  h2 {
    font-size: 9.3pt;
    font-weight: 800;
    color: #0b0e14;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-top: 5px;
    margin-bottom: 3px;
    padding-bottom: 2px;
    border-bottom: 1.5px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .h2-badge {
    font-size: 7pt;
    color: #4a8fc2;
    font-weight: 700;
  }
  .segment-card {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 5px 9px;
    margin-bottom: 4.5px;
    page-break-inside: avoid;
  }
  .seg-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2px;
  }
  .seg-title {
    font-size: 8.4pt;
    font-weight: 800;
    color: #0f172a;
  }
  .seg-time {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, monospace;
    font-size: 7.5pt;
    font-weight: 700;
    color: #0284c7;
    background: #e0f2fe;
    padding: 1px 6px;
    border-radius: 4px;
  }
  .seg-speaker {
    font-size: 7.2pt;
    font-weight: 600;
    color: #64748b;
    margin-left: 6px;
  }
  .seg-script {
    font-size: 7.9pt;
    font-style: italic;
    color: #1e293b;
    background: #ffffff;
    border-left: 2.5px solid #4a8fc2;
    padding: 3.5px 7px;
    border-radius: 0 4px 4px 0;
    line-height: 1.33;
  }
  .pivots-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-top: 4px;
    page-break-inside: avoid;
  }
  .pivot-box {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 5px 8px;
  }
  .pivot-title {
    font-size: 7.8pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2px;
  }
  .pivot-text {
    font-size: 7.1pt;
    color: #334155;
    line-height: 1.28;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 3px;
    margin-bottom: 5px;
    font-size: 7.2pt;
    page-break-inside: avoid;
  }
  th {
    background: #0b0e14;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 3.5px 6px;
    letter-spacing: 0.02em;
  }
  td {
    border-bottom: 1px solid #e2e8f0;
    padding: 3px 6px;
    vertical-align: top;
    color: #1e293b;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }
  .qa-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
    margin-top: 3px;
    page-break-inside: avoid;
  }
  .qa-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 4.5px 7.5px;
  }
  .qa-q {
    font-size: 7.4pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2px;
  }
  .qa-a {
    font-size: 6.9pt;
    color: #334155;
    line-height: 1.28;
  }
  .audit-banner {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-radius: 5px;
    padding: 4.5px 9px;
    margin-top: 5px;
    display: flex;
    justify-content: space-between;
    font-size: 7.0pt;
    color: #065f46;
    font-weight: 600;
    page-break-inside: avoid;
  }
  .check-item {
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .footer-bar {
    margin-top: 5px;
    padding-top: 3px;
    border-top: 1px solid #cbd5e1;
    display: flex;
    justify-content: space-between;
    font-size: 6.8pt;
    color: #94a3b8;
  }
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="page-container">
  <div class="header-banner">
    <div class="header-top">
      <div class="brand-title">PRISMATIC · PRESENTER TALKING POINTS</div>
      <div class="event-tag">AWS × MLU FALL SYMPOSIUM 2026</div>
    </div>
    <div class="header-sub">
      STARTUP: <b>PRISMATIC</b> · TRACK: SCENARIO 2 (STUDY BUDDY) · FORMAT: EXACTLY 2 MINUTES (120 SECONDS)<br/>
      DELIVERY: NO LIVE CODE DEMO REQUIRED · SHOW RUNNING AMAZON QUICK UI · ROOM WINNER ADVANCES TO MAIN STAGE
    </div>
  </div>

  <h2>1. Timed 2-Minute Word-by-Word Pitch Script <span class="h2-badge">VERBATIM OFFICIAL HANDOUT CALIBRATION</span></h2>

  <!-- Segment 1 -->
  <div class="segment-card">
    <div class="seg-header">
      <div class="seg-title">SEGMENT 1: TEAM NAME <span class="seg-speaker">· Presenter: Speaker 1 (High Energy, Strong Smile)</span></div>
      <div class="seg-time">0:00 - 0:10 (10s)</div>
    </div>
    <div class="seg-script">
      "Good afternoon, judges and fellow builders! We are <b>PRISMATIC</b>—and we are here to refract the way college students learn!"
    </div>
  </div>

  <!-- Segment 2 -->
  <div class="segment-card">
    <div class="seg-header">
      <div class="seg-title">SEGMENT 2: THE HOOK <span class="seg-speaker">· Presenter: Speaker 1 (Relatable, Empathetic, Direct Eye Contact)</span></div>
      <div class="seg-time">0:10 - 0:35 (25s)</div>
    </div>
    <div class="seg-script">
      "It’s 2:00 AM before midterms. You’ve re-read the exact same textbook paragraph six times—and understood it zero times. <i>[Micro-pause]</i> You turn to ChatGPT in desperation, and it dumps an 800-word wall of text that makes your brain freeze even harder.<br/>
      That sinking panic isn't a lack of intelligence—it's a failure of wavelength. White light holds every color, but professors lecture in one flat shade. Human brains don't think in monochrome—we learn in spectrums."
    </div>
  </div>

  <!-- Segment 3 -->
  <div class="segment-card">
    <div class="seg-header">
      <div class="seg-title">SEGMENT 3: YOUR APP OVERVIEW <span class="seg-speaker">· Presenter: Speaker 2 (Product Lead, Gestures to Screen)</span></div>
      <div class="seg-time">0:35 - 1:20 (45s)</div>
    </div>
    <div class="seg-script">
      "We built <b>Prismatic</b> on Amazon Quick—an agentic cognitive engine that turns 1 static lecture into 4 tailored learning modalities in under 30 seconds. First, a rapid 5-question diagnostic maps how your brain absorbs information. Then, our Amazon Bedrock pipeline instantly refracts the material:<br/>
      • <b>Spectrum 1</b> translates abstract theory into relatable dorm and dining hall analogies.<br/>
      • <b>Spectrum 2</b> renders structural ASCII concept maps and visual schemas.<br/>
      • <b>Spectrum 3</b> launches a Socratic Sparring Partner that quizzes you one edge-case at a time without spoiling answers.<br/>
      • And <b>Spectrum 4</b> builds a 4-slide micro-deck exposing the exact trap questions professors test on midterms."
    </div>
  </div>

  <!-- Segment 4 -->
  <div class="segment-card">
    <div class="seg-header">
      <div class="seg-title">SEGMENT 4: WHY IT WINS <span class="seg-speaker">· Presenter: Speaker 3 (Market Lead, Confident & Authoritative)</span></div>
      <div class="seg-time">1:20 - 1:45 (25s)</div>
    </div>
    <div class="seg-script">
      "Over 20 million college students face academic paralysis every semester.<br/>
      Generic tools like ChatGPT just dump 800-word walls of text that students glaze over.<br/>
      Private tutoring costs $80 an hour, and professor office hours are only 2 hours a week.<br/>
      Prismatic is active, multi-modal, and adapts the syllabus to the student—democratizing elite private tutoring for pennies on Bedrock."
    </div>
  </div>

  <!-- Segment 5 -->
  <div class="segment-card">
    <div class="seg-header">
      <div class="seg-title">SEGMENT 5: THE CLOSE <span class="seg-speaker">· Presenter: Speaker 1 & Full Team in Unison</span></div>
      <div class="seg-time">1:45 - 2:00 (15s)</div>
    </div>
    <div class="seg-script">
      "With more time, we’d add <b>live Canvas and syllabus LMS integration</b>, automatically syncing weekly exam dates and generating proactive 15-minute micro-sprints before every morning class.<br/>
      We don't just help students pass exams; we eliminate academic paralysis and unlock confidence.<br/>
      We are <b>PRISMATIC</b>—refracting complex knowledge into your native spectrum. Vote Prismatic for your room champion! Thank you!"
    </div>
  </div>

  <h2>2. Emergency Quick Pivots <span class="h2-badge">FAIL-SAFE DRILLS</span></h2>
  <div class="pivots-grid">
    <div class="pivot-box">
      <div class="pivot-title">⚡ 60-Second Flash Pitch (If Time Compressed)</div>
      <div class="pivot-text">
        "Judges, it’s 2:00 AM before midterms, and 20 million students are freezing over dense course material. Generic AI dumps sterile text; private tutors cost $80 an hour. That panic isn't a lack of intelligence—it's a failure of wavelength. We built Prismatic on Amazon Quick: a 30-second diagnostic maps your intake profile and refracts any syllabus topic into 4 active modalities: dorm analogies, visual flowcharts, Socratic active recall, and midterm exam trap decks. We give every student an elite, adaptive tutor on Bedrock. With more time, we'd add Canvas LMS integration. We are Prismatic—vote Prismatic!"
      </div>
    </div>
    <div class="pivot-box">
      <div class="pivot-title">🎯 30-Second Speed-Dating Hook & Fallback</div>
      <div class="pivot-text">
        "Ever re-read an exam slide six times and understood it zero times? Classrooms broadcast in monochrome, but our brains learn in spectrums. Prismatic is an agentic learning engine on Amazon Quick that refracts dense coursework into 4 active spectrums: analogies, visual schematics, Socratic sparring, and midterm trap cards. We democratize $80/hour tutoring for every undergrad on campus!"<br/>
        <b>Tech Fallback:</b> Pivot instantly to the offline local web app (<code>web-app/index.html</code>) which runs with zero Wi-Fi dependencies.
      </div>
    </div>
  </div>

  <div class="footer-bar">
    <span>PRISMATIC · AWS-MLU SYMPOSIUM 2026</span>
    <span>PAGE 1 OF 2</span>
  </div>
</div>

<!-- ================= PAGE 2 ================= -->
<div class="page-container">
  <h2>3. 10-Person Team Choreography & Stage Positioning <span class="h2-badge">ALL TEAMMATES ACTIVE</span></h2>

  <table>
    <thead>
      <tr>
        <th style="width: 10%;">Role #</th>
        <th style="width: 25%;">Dedicated Title</th>
        <th style="width: 65%;">Live Presentation & Judging Responsibility</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Member 1</b></td>
        <td><b>Founding Anchor</b></td>
        <td>Delivers Segments 1 & 2 (Team Intro & 300-Student Hook), leads team energy, coordinates closing call.</td>
      </tr>
      <tr>
        <td><b>Member 2</b></td>
        <td><b>Product Architect</b></td>
        <td>Delivers Segment 3 (App Overview), gestures smoothly to Amazon Quick screen and live 4 spectrums.</td>
      </tr>
      <tr>
        <td><b>Member 3</b></td>
        <td><b>Market & Growth Lead</b></td>
        <td>Delivers Segment 4 (Why It Wins), fields market size ($80/hr tutoring gap) and competitive moats.</td>
      </tr>
      <tr>
        <td><b>Member 4</b></td>
        <td><b>Display Pilot</b></td>
        <td>Holds laptop/cart steadily displaying running Amazon Quick UI or the local offline Prismatic Web App.</td>
      </tr>
      <tr>
        <td><b>Member 5</b></td>
        <td><b>Cognitive Pedagogy Lead</b></td>
        <td>Answers Shark Q&A on learning styles, cognitive friction points, and the 5-question diagnostic triage.</td>
      </tr>
      <tr>
        <td><b>Member 6</b></td>
        <td><b>Cloud Architect</b></td>
        <td>Answers Shark Q&A on Amazon Quick, Amazon Bedrock foundation models, prompt pipelines, and latency.</td>
      </tr>
      <tr>
        <td><b>Member 7</b></td>
        <td><b>Student Experience Lead</b></td>
        <td>Answers Shark Q&A on 2026 college student reality, dorm life constraints, dining halls, and ADHD study habits.</td>
      </tr>
      <tr>
        <td><b>Member 8</b></td>
        <td><b>Campus Integration Lead</b></td>
        <td>Answers Shark Q&A on Canvas/Blackboard LMS API sync, course reserves, and university licensing models.</td>
      </tr>
      <tr>
        <td><b>Member 9</b></td>
        <td><b>Official Room Voter</b></td>
        <td>Designated team representative holding the official ballot for your room (strategic peer voting).</td>
      </tr>
      <tr>
        <td><b>Member 10</b></td>
        <td><b>Timekeeper & Co-Founder</b></td>
        <td>Gives silent hand gestures at 1:00, 1:30, and 1:45 to guarantee pitch finishes at exactly 1m 52s.</td>
      </tr>
    </tbody>
  </table>

  <h2>4. Anticipated Shark Tank Q&A Defense <span class="h2-badge">SHARP REBUTTALS</span></h2>

  <div class="qa-grid">
    <div class="qa-box">
      <div class="qa-q">Q1: "How does this differ from typing 'explain this to me' into ChatGPT?"</div>
      <div class="qa-a"><b>Defense:</b> "ChatGPT is passive text generation: it dumps 800 words that cause immediate student glaze. Prismatic is an agentic multi-widget pipeline. It starts with a 30-second diagnostic triage, and orchestrates 4 distinct modalities simultaneously—including a Socratic Sparring Partner that refuses to lecture and instead forces active recall by testing edge cases."</div>
    </div>
    <div class="qa-box">
      <div class="qa-q">Q2: "Why did you use Amazon Quick instead of coding a frontend from scratch?"</div>
      <div class="qa-a"><b>Defense:</b> "Velocity and multi-model orchestration. In a 75-minute sprint, coding full-stack auth, state management, and Bedrock API calls would introduce latency and bugs. Amazon Quick's Apps mode allowed our 10-person team to chain inputs into text generation, image generation, and a chatbot on a single screen without touching boilerplate."</div>
    </div>
    <div class="qa-box">
      <div class="qa-q">Q3: "How do you prevent students from using this to cheat?"</div>
      <div class="qa-a"><b>Defense:</b> "Prismatic is engineered for learning retention, not answer generation. The Socratic module bounds answers to 2 sentences and asks conceptual 'why' questions. It cannot write essays; it trains students to master the underlying mechanics so they can perform on in-person exams."</div>
    </div>
    <div class="qa-box">
      <div class="qa-q">Q4: "What is your revenue and distribution model?"</div>
      <div class="qa-a"><b>Defense:</b> "B2B university licensing (enterprise campus software) integrated into Canvas, plus a freemium B2C tier for students. Universities currently spend millions on retention programs; Prismatic directly increases course completion rates."</div>
    </div>
  </div>

  <h2>5. What the Sharks Look For: Final Audit <span class="h2-badge">100% COMPLIANCE</span></h2>
  
  <div class="audit-banner">
    <div class="check-item"><span>✔</span> <b>Creativity:</b> Cognitive refraction metaphor</div>
    <div class="check-item"><span>✔</span> <b>Usefulness:</b> Solves dorm paralysis & exam panic</div>
    <div class="check-item"><span>✔</span> <b>Execution:</b> Working 6-widget Quick pipeline</div>
    <div class="check-item"><span>✔</span> <b>Teamwork:</b> 10 members with active roles</div>
    <div class="check-item"><span>✔</span> <b>Timing:</b> Exactly 1m 52s (8s buffer)</div>
  </div>

  <div class="footer-bar">
    <span>PRISMATIC · AWS-MLU SYMPOSIUM 2026</span>
    <span>PAGE 2 OF 2</span>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Wrote styled HTML talking points: {HTML_PATH}")

    # Prioritize Chrome/Edge for publication-grade Skia/PDF rendering
    candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]

    for browser in candidates:
        if browser.exists():
            print(f"[*] Rendering Skia/PDF via Chromium engine ({browser.name})...")
            cmd = [
                str(browser),
                "--headless",
                "--disable-gpu",
                f"--print-to-pdf={PDF_PATH}",
                "--no-pdf-header-footer",
                str(HTML_PATH)
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0 and PDF_PATH.exists():
                print(f"[+] Successfully exported publication-grade Skia/PDF: {PDF_PATH}")
                return

    print("[!] No Chromium engine found. Falling back to ReportLab...")
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    doc = SimpleDocTemplate(str(PDF_PATH), pagesize=letter)
    doc.build([Paragraph("Fallback document", getSampleStyleSheet()['Normal'])])

if __name__ == "__main__":
    generate_pdf()
