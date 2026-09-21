import os
import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "PRESENTER_TALKING_POINTS.pdf"

class NumberedCanvas(canvas.Canvas):
    """Adds running headers and page numbers to each page."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#0284c7"))
        self.drawString(36, 756, "PRISMATIC · SHARK TANK SPRINT PLAYBOOK")
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(576, 756, "CLOUD CONNECT 2026 · HOWARD & AMAZON HQ2")
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 750, 576, 750)
        
        # Footer
        self.line(36, 32, 576, 32)
        self.drawString(36, 22, "CONFIDENTIAL & PROPRIETARY · PRESENTATION DRILL COPY")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 22, page_str)
        self.restoreState()

def build_pdf():
    # 0.5 in margins (36 pt)
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=2
    )
    
    banner_style = ParagraphStyle(
        'BannerText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0369a1')
    )

    h2_style = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#0284c7'),
        spaceBefore=5,
        spaceAfter=3
    )

    box_title = ParagraphStyle(
        'BoxTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )

    box_body = ParagraphStyle(
        'BoxBody',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.0,
        leading=10.2,
        textColor=colors.HexColor('#1e293b')
    )

    pivot_style = ParagraphStyle(
        'PivotBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=9.8,
        textColor=colors.HexColor('#334155')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.5,
        textColor=colors.white
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=8.8,
        textColor=colors.HexColor('#1e293b')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=8.8,
        textColor=colors.HexColor('#0f172a')
    )

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("PRISMATIC: 2-MINUTE SHARK TANK PITCH SCRIPT & PLAYBOOK", title_style))
    
    banner_data = [[
        Paragraph("STARTUP: <b>PRISMATIC</b> · TRACK: SCENARIO 2 (STUDY BUDDY) · FORMAT: EXACTLY 2 MINUTES (120 SECONDS)<br/>RULE: NO LIVE CODE DEMO REQUIRED · SHOW RUNNING AMAZON QUICK UI · ROOM CHAMPION ADVANCES TO FINALS", banner_style)
    ]]
    t_banner = Table(banner_data, colWidths=[540])
    t_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0f9ff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#bae6fd')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_banner)
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. TIMED 2-MINUTE WORD-BY-WORD PITCH SCRIPT (THE 5 OFFICIAL SEGMENTS)", h2_style))

    segments = [
        ("SEGMENT 1: TEAM NAME [0:00 - 0:10 | 10 SECONDS] · Presenter: Speaker 1 (High Energy)",
         "\"Good afternoon, judges and fellow builders! We are PRISMATIC—and we are here to refract the way college students learn!\""),
        
        ("SEGMENT 2: THE HOOK [0:10 - 0:35 | 25 SECONDS] · Presenter: Speaker 1 (Relatable & Empathic)",
         "\"Picture a 300-person lecture hall right here at Howard or UMD. The professor spends 75 minutes covering one complex concept. Half the class nods; the other half walks out completely lost with intense brain fog. The problem isn't student intellect. White light contains every color, but a flat chalkboard only projects one shade. Professors teach in one rigid format, while human brains process knowledge in completely different spectrums.\""),
        
        ("SEGMENT 3: YOUR APP OVERVIEW [0:35 - 1:20 | 45 SECONDS] · Presenter: Speaker 2 (Product Lead)",
         "\"We built Prismatic on Amazon Quick—an agentic cognitive engine that turns 1 static lecture into 4 tailored learning modalities in under 30 seconds. First, a rapid 5-question diagnostic maps how your brain absorbs information. Then, our Amazon Bedrock pipeline instantly refracts the material: <b>Spectrum 1</b> translates abstract theory into relatable dorm and dining hall analogies. <b>Spectrum 2</b> renders structural ASCII concept maps and visual schemas. <b>Spectrum 3</b> launches a Socratic Sparring Partner that quizzes you one edge-case at a time without spoiling answers. And <b>Spectrum 4</b> builds a 4-slide micro-deck exposing the exact trap questions professors test on midterms.\""),
        
        ("SEGMENT 4: WHY IT WINS [1:20 - 1:45 | 25 SECONDS] · Presenter: Speaker 3 (Market Lead)",
         "\"Over 20 million college students face academic paralysis every semester. Generic tools like ChatGPT just dump 800-word walls of text that students glaze over. Private tutoring costs $80 an hour, and professor office hours are only 2 hours a week. Prismatic is active, multi-modal, and adapts the syllabus to the student—democratizing elite private tutoring for pennies on Bedrock.\""),
        
        ("SEGMENT 5: THE CLOSE [1:45 - 2:00 | 15 SECONDS] · Presenter: Speaker 1 & Full Team (Unison)",
         "\"With more time, we’d add <b>live Canvas and syllabus LMS integration</b>, automatically syncing weekly exam dates and generating proactive 15-minute micro-sprints before every morning class. We don't just help students pass exams; we eliminate academic paralysis and unlock confidence. We are PRISMATIC—refracting complex knowledge into your native spectrum. Vote Prismatic for your room champion! Thank you!\"")
    ]

    for title, text in segments:
        data = [
            [Paragraph(f"<b>{title}</b>", box_title)],
            [Paragraph(text, box_body)]
        ]
        t = Table(data, colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#cbd5e1')),
            ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#e2e8f0')),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        story.append(t)
        story.append(Spacer(1, 3))

    story.append(Paragraph("2. EMERGENCY QUICK PIVOTS", h2_style))
    pivots_data = [
        [
            Paragraph("<b>60-Second Flash Pitch (If Compressed):</b> \"Judges, 300 students in a lecture hall shouldn't be taught one way. When students freeze, it's not a lack of intelligence—it's a cognitive mismatch. We built Prismatic on Amazon Quick: a 30-second diagnostic maps your learning profile and refracts any syllabus topic into 4 active modalities: dorm analogies, visual flowcharts, Socratic active recall, and midterm exam trap decks. ChatGPT dumps text; private tutors cost $80/hr. Prismatic gives every student an elite, adaptive tutor on Bedrock. With more time, we'd add Canvas LMS integration. We are Prismatic—vote Prismatic!\"", pivot_style),
            Paragraph("<b>30-Second Speed-Dating Hook:</b> \"White light has every color, but college lectures only teach in one shade. Prismatic is an agentic learning engine on Amazon Quick that turns any dense topic into 4 personalized spectrums—analogies, visual schematics, Socratic sparring, and exam trap cards. We democratize $80/hour tutoring for every undergrad on campus!\"<br/><br/><b>Tech Fallback:</b> Pivot to offline local web app (`web-app/index.html`) if Wi-Fi drops.", pivot_style)
        ]
    ]
    t_piv = Table(pivots_data, colWidths=[265, 265])
    t_piv.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94a3b8')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_piv)

    # ================= PAGE 2 =================
    story.append(PageBreak())

    story.append(Paragraph("3. 10-PERSON TEAM CHOREOGRAPHY & STAGE POSITIONING", h2_style))

    roles = [
        ("#1", "Founding Anchor", "Delivers Segments 1 & 2 (Hook), leads team cheer, coordinates close."),
        ("#2", "Product Architect", "Delivers Segment 3 (App Overview), points to widgets on screen."),
        ("#3", "Market Lead", "Delivers Segment 4 (Why It Wins), fields business/market questions."),
        ("#4", "Display Pilot", "Holds laptop/cart showing running Amazon Quick UI or local Prismatic Web App."),
        ("#5", "Cognitive Pedagogy", "Answers Q&A on learning styles, VARK theory, and cognitive friction."),
        ("#6", "Cloud Architect", "Answers Q&A on Amazon Quick, Bedrock models, latency, and prompt engineering."),
        ("#7", "Student Experience", "Answers Q&A on user persona, dorm life realities, and ADHD study habits."),
        ("#8", "Campus Integration", "Answers Q&A on Canvas/Blackboard LMS API sync and university licensing."),
        ("#9", "Official Room Voter", "Designated team representative holding the official ballot for your room."),
        ("#10", "Timekeeper / Co-Founder", "Gives silent hand gestures at 1:00, 1:30, and 1:45 to keep pitch under 2 minutes.")
    ]

    r_table_data = [[Paragraph("Role", table_header), Paragraph("Title", table_header), Paragraph("Responsibility During Presentation", table_header)]]
    for r_num, r_title, r_desc in roles:
        r_table_data.append([
            Paragraph(r_num, table_cell_bold),
            Paragraph(r_title, table_cell_bold),
            Paragraph(r_desc, table_cell)
        ])

    t_roles = Table(r_table_data, colWidths=[35, 125, 380])
    t_roles.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_roles)
    story.append(Spacer(1, 5))

    story.append(Paragraph("4. ANTICIPATED SHARK TANK Q&A DEFENSE", h2_style))

    qa_list = [
        ("Q1: How does this differ from typing 'explain this to me' into ChatGPT?",
         "ChatGPT is passive text generation: it dumps 800 words that cause cognitive glaze. Prismatic is an agentic multi-widget pipeline. It starts with a 30-second diagnostic triage, and orchestrates 4 distinct modalities simultaneously—including a Socratic Sparring Partner that refuses to lecture and instead forces active recall by testing edge cases."),
        ("Q2: Why did you use Amazon Quick instead of coding a frontend from scratch?",
         "Velocity and multi-model orchestration. In a 75-minute sprint, coding full-stack auth, state management, and Bedrock API calls would introduce latency and bugs. Amazon Quick's Apps mode allowed our 10-person team to chain inputs into text generation, image generation, and a chatbot on a single screen without touching boilerplate."),
        ("Q3: How do you prevent students from using this to cheat?",
         "Prismatic is engineered for learning retention, not answer generation. The Socratic module bounds answers to 2 sentences and asks conceptual 'why' questions. It cannot write essays; it trains students to master the underlying mechanics so they can perform on in-person exams."),
        ("Q4: What is your revenue and distribution model?",
         "B2B university licensing (enterprise campus software) integrated into Canvas, plus a freemium B2C tier for students. Universities currently spend millions on retention programs; Prismatic directly increases course completion rates.")
    ]

    qa_table_data = []
    for q, a in qa_list:
        qa_table_data.append([
            Paragraph(f"<b>{q}</b><br/><font color='#334155'><b>Defense:</b> {a}</font>", table_cell)
        ])
    t_qa = Table(qa_table_data, colWidths=[540])
    t_qa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_qa)
    story.append(Spacer(1, 5))

    story.append(Paragraph("5. WHAT THE SHARKS LOOK FOR: FINAL AUDIT", h2_style))
    audit_data = [
        [
            Paragraph("✔ <b>Creativity:</b> Cognitive refraction metaphor (white light → 4 learning spectrums).<br/>✔ <b>Usefulness:</b> Solves real 2026 undergraduate task paralysis and cram anxiety.", table_cell),
            Paragraph("✔ <b>Execution:</b> Working multi-widget pipeline on Amazon Quick + local standalone web app.<br/>✔ <b>Teamwork:</b> All 10 members have explicit on-stage roles. <b>Timing:</b> Exactly 1m 52s.", table_cell)
        ]
    ]
    t_audit = Table(audit_data, colWidths=[265, 265])
    t_audit.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ecfdf5')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#a7f3d0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_audit)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Successfully built portable 2-page PDF via ReportLab: {PDF_PATH}")

if __name__ == "__main__":
    build_pdf()
