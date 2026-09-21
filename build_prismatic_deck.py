import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import win32com.client

# ==========================================
# COLOR PALETTE (Prismatic Dark Modern Theme)
# ==========================================
BG_COLOR = RGBColor(11, 15, 25)         # #0B0F19 Deep Space Navy
SURFACE_COLOR = RGBColor(18, 24, 38)    # #121826 Elevated Card
SURFACE_ALT = RGBColor(26, 34, 52)      # #1A2234 Highlighted Card
BORDER_COLOR = RGBColor(40, 56, 85)     # #283855 Clean border
CYAN_ACCENT = RGBColor(0, 212, 255)     # #00D4FF Prismatic Cyan
VIOLET_ACCENT = RGBColor(168, 85, 247)  # #A855F7 Prismatic Violet
AMBER_ACCENT = RGBColor(245, 158, 11)   # #F59E0B Warning / Stat Accent
EMERALD_ACCENT = RGBColor(16, 185, 129) # #10B981 Success Green
ROSE_ACCENT = RGBColor(244, 63, 94)     # #F43F5E Contrast Alert
TEXT_WHITE = RGBColor(255, 255, 255)    # Pure White
TEXT_LIGHT = RGBColor(226, 232, 240)    # Slate 200
TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400
TEXT_DIM = RGBColor(100, 116, 139)      # Slate 500

BASE_DIR = os.path.abspath(r"c:\Users\Saksham Kapoor\Documents\SHARK-TANK-AWS-MLU")
OUTPUT_PPTX = os.path.join(BASE_DIR, "Prismatic_Shark_Tank_Pitch_Deck.pptx")
OUTPUT_PDF = os.path.join(BASE_DIR, "Prismatic_Shark_Tank_Pitch_Deck.pdf")

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()
    return bg

def add_header(slide, tracker_text, title_text, subtitle_text=""):
    tb_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_tr = tb_box.text_frame
    tf_tr.word_wrap = True
    tf_tr.margin_left = tf_tr.margin_top = tf_tr.margin_right = tf_tr.margin_bottom = 0
    p_tr = tf_tr.paragraphs[0]
    p_tr.text = tracker_text.upper()
    p_tr.font.name = "Segoe UI"
    p_tr.font.size = Pt(11)
    p_tr.font.bold = True
    p_tr.font.color.rgb = CYAN_ACCENT

    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.55))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = "Segoe UI"
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE

    if subtitle_text:
        tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.35))
        tf_sub = tb_sub.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle_text
        p_sub.font.name = "Segoe UI"
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = TEXT_MUTED

def add_card(slide, left, top, width, height, bg_color=SURFACE_COLOR, border_color=BORDER_COLOR):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
    else:
        card.line.fill.background()
    return card

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6]

    # ==========================================
    # SLIDE 1: TITLE & CORE HOOK
    # ==========================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s1)

    # Decorative hero pill
    pill = add_card(s1, Inches(0.8), Inches(1.0), Inches(4.5), Inches(0.4), bg_color=SURFACE_ALT, border_color=CYAN_ACCENT)
    tb_pill = s1.shapes.add_textbox(Inches(0.9), Inches(1.05), Inches(4.3), Inches(0.3))
    p_p = tb_pill.text_frame.paragraphs[0]
    p_p.text = "CLOUD CONNECT — HOWARD 2026 | AWS × MLU × BEN TECH"
    p_p.font.name = "Segoe UI"
    p_p.font.size = Pt(9.5)
    p_p.font.bold = True
    p_p.font.color.rgb = CYAN_ACCENT

    # Main Title
    tb = s1.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "PRISMATIC"
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(46)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf.add_paragraph()
    p2.text = "Refracting Complex Knowledge Into Your Mind's Native Spectrum"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(20)
    p2.font.color.rgb = VIOLET_ACCENT

    # 3 Stat / Insight Hero Cards
    card_data = [
        ("300 STUDENTS, 1 FORMAT", "Lecture Hall Asymmetry", "Professors teach one way. Half the room absorbs it; the other half walks out with intense brain fog.", ROSE_ACCENT),
        ("78% TASK PARALYSIS", "The 2026 Reality", "Students don't fail from lack of intellect; they freeze when staring at 40-page PDFs with zero cognitive adaptation.", AMBER_ACCENT),
        ("< 30 SEC DIAGNOSTIC", "The Prismatic Answer", "5 scenario questions map your cognitive profile and refract any topic into 4 personalized learning modalities.", EMERALD_ACCENT)
    ]
    card_w = Inches(3.7)
    card_h = Inches(3.2)
    top_pos = Inches(3.4)

    for i, (metric, label, desc, color) in enumerate(card_data):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s1, left_pos, top_pos, card_w, card_h)
        
        # Metric
        tb_m = s1.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(0.3), card_w - Inches(0.5), Inches(0.5))
        pm = tb_m.text_frame.paragraphs[0]
        pm.text = metric
        pm.font.name = "Segoe UI"
        pm.font.size = Pt(16)
        pm.font.bold = True
        pm.font.color.rgb = color

        # Label
        tb_l = s1.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(0.85), card_w - Inches(0.5), Inches(0.4))
        pl = tb_l.text_frame.paragraphs[0]
        pl.text = label
        pl.font.name = "Segoe UI"
        pl.font.size = Pt(13)
        pl.font.bold = True
        pl.font.color.rgb = TEXT_WHITE

        # Desc
        tb_d = s1.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(1.35), card_w - Inches(0.5), Inches(1.4))
        pd = tb_d.text_frame.paragraphs[0]
        pd.text = desc
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_MUTED

    # Speaker notes
    notes = s1.notes_slide.notes_text_frame
    notes.text = (
        "THE 25-SECOND HOOK:\n"
        "Judges, picture a 300-person lecture hall right here at Howard or UMD. The professor spends 75 minutes covering one complex concept. "
        "Half the class nods; the other half walks out completely lost, staring at a 40-page slide deck with intense brain fog.\n\n"
        "The problem isn't that college students aren't smart. The problem is that white light contains every color, but a flat chalkboard only projects one shade. "
        "Professors teach in one rigid format, while human brains process information in completely different spectrums."
    )

    # ==========================================
    # SLIDE 2: HOW IT WORKS (THE COGNITIVE PIPELINE)
    # ==========================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s2)
    add_header(s2, "System Architecture", "The Cognitive Prism Engine: Ingest, Diagnose & Refract", "Engineered in 60 minutes on Amazon Quick with agentic multi-widget pipeline orchestration")

    steps = [
        ("STEP 1: INGEST", "Raw Academic Material", "Student pastes confusing lecture slides, a syllabus link, or a brutal midterm exam review sheet.", CYAN_ACCENT),
        ("STEP 2: DIAGNOSE", "30-Second Cognitive Triage", "5 scenario questions identify primary learning modality, friction bottlenecks, and exam countdown.", VIOLET_ACCENT),
        ("STEP 3: REFRACT", "Multi-Modal Synthesis", "Amazon Quick orchestrates Amazon Bedrock models into 4 distinct, simultaneous learning spectrums.", EMERALD_ACCENT)
    ]
    step_w = Inches(3.7)
    step_h = Inches(4.9)
    top_pos2 = Inches(1.85)

    for i, (st, sl, sd, sc) in enumerate(steps):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s2, left_pos, top_pos2, step_w, step_h)

        tb_s = s2.shapes.add_textbox(left_pos + Inches(0.3), top_pos2 + Inches(0.4), step_w - Inches(0.6), Inches(0.4))
        ps = tb_s.text_frame.paragraphs[0]
        ps.text = st
        ps.font.name = "Segoe UI"
        ps.font.size = Pt(14)
        ps.font.bold = True
        ps.font.color.rgb = sc

        tb_sl = s2.shapes.add_textbox(left_pos + Inches(0.3), top_pos2 + Inches(0.9), step_w - Inches(0.6), Inches(0.5))
        psl = tb_sl.text_frame.paragraphs[0]
        psl.text = sl
        psl.font.name = "Segoe UI"
        psl.font.size = Pt(15)
        psl.font.bold = True
        psl.font.color.rgb = TEXT_WHITE

        tb_sd = s2.shapes.add_textbox(left_pos + Inches(0.3), top_pos2 + Inches(1.5), step_w - Inches(0.6), Inches(2.8))
        psd = tb_sd.text_frame.paragraphs[0]
        psd.text = sd
        psd.font.name = "Segoe UI"
        psd.font.size = Pt(12)
        psd.font.color.rgb = TEXT_MUTED

    notes2 = s2.notes_slide.notes_text_frame
    notes2.text = (
        "THE SOLUTION PITCH:\n"
        "That is why we built Prismatic. Prismatic is an agentic learning engine on Amazon Quick that acts as a cognitive prism.\n"
        "In under 30 seconds, a rapid 5-question diagnostic maps how your brain actually absorbs information—whether you need analogies, visual flowcharts, Socratic active recall, or an emergency 15-minute action sprint.\n"
        "Instead of forcing you to adapt to the syllabus, Prismatic adapts the syllabus to you."
    )

    # ==========================================
    # SLIDE 3: THE 4 LEARNING SPECTRUMS
    # ==========================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s3)
    add_header(s3, "Product Experience", "The 4 Learning Spectrums: Zero Errors, Maximum Retention", "Every student gets the modality their brain naturally responds to")

    spectrums = [
        ("SPECTRUM 1: INTUITIVE ANALOGY", "Dorm & Campus Analogies", "Maps abstract theory to everyday student life. E.g., Dijkstra's shortest path = navigating dining hall rush hours at peak times.", CYAN_ACCENT),
        ("SPECTRUM 2: VISUAL SCHEMATIC", "ASCII & Concept Maps", "Structures execution order, logical branches, and state changes into visual mental architectures for STEM/CS.", VIOLET_ACCENT),
        ("SPECTRUM 3: SOCRATIC SPARRING", "Active Retrieval Partner", "Chatbot strictly limited to 2 sentences; never lectures; fires progressive edge cases to force active recall.", EMERALD_ACCENT),
        ("SPECTRUM 4: EXAM TRAP DECK", "4-Slide Micro-Presentation", "Distills the topic into 4 slides exposing the exact tricks and traps professors test on Midterm #2.", AMBER_ACCENT)
    ]

    spec_w = Inches(5.7)
    spec_h = Inches(2.3)

    for i, (sp_t, sp_l, sp_d, sp_c) in enumerate(spectrums):
        col = i % 2
        row = i // 2
        left_pos = Inches(0.8 + col * (5.7 + 0.3))
        top_pos3 = Inches(1.85 + row * (2.3 + 0.3))

        add_card(s3, left_pos, top_pos3, spec_w, spec_h)

        tb_t = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos3 + Inches(0.25), spec_w - Inches(0.6), Inches(0.35))
        pt = tb_t.text_frame.paragraphs[0]
        pt.text = sp_t
        pt.font.name = "Segoe UI"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = sp_c

        tb_l = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos3 + Inches(0.65), spec_w - Inches(0.6), Inches(0.4))
        pl = tb_l.text_frame.paragraphs[0]
        pl.text = sp_l
        pl.font.name = "Segoe UI"
        pl.font.size = Pt(14)
        pl.font.bold = True
        pl.font.color.rgb = TEXT_WHITE

        tb_d = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos3 + Inches(1.15), spec_w - Inches(0.6), Inches(0.95))
        pd = tb_d.text_frame.paragraphs[0]
        pd.text = sp_d
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_MUTED

    notes3 = s3.notes_slide.notes_text_frame
    notes3.text = (
        "LIVE APPLICATION WALKTHROUGH:\n"
        "Here is Prismatic running live on Amazon Quick:\n"
        "When you paste in a notoriously brutal topic—like Dijkstra’s Algorithm or Cellular Respiration:\n"
        "1. For conceptual thinkers, Spectrum 1 translates the math into a relatable campus dining hall rush.\n"
        "2. For visual learners, Spectrum 2 renders an interactive ASCII concept map.\n"
        "3. For active crammers, Spectrum 3 launches our Socratic Sparring Partner—an AI that quizzes you with high-yield edge cases.\n"
        "4. And for exam morning, it builds a 4-slide micro-deck exposing the exact trap questions professors love to test."
    )

    # ==========================================
    # SLIDE 4: THE SHARK TANK CLOSE & IMPACT
    # ==========================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s4)
    add_header(s4, "Market Opportunity & Closing Ask", "Democratizing Elite Tutoring: From Luxury to Student Right", "The $80/hr private tutor in every student's pocket on Amazon Quick")

    metrics_close = [
        ("20M+", "U.S. Undergrads", "Struggling with post-AI curriculum shifts and dense, fast-moving lectures.", CYAN_ACCENT),
        ("$80 / HR", "Private Tutoring Cost", "Traditional tutoring is financially gatekept; Prismatic costs pennies on Bedrock.", ROSE_ACCENT),
        ("100% NO-CODE", "Amazon Quick Power", "Shipped a working, interactive multi-widget app in 60 minutes flat.", EMERALD_ACCENT)
    ]
    mc_w = Inches(3.7)
    mc_h = Inches(2.2)
    top_pos4 = Inches(1.85)

    for i, (mv, ml, md, mc) in enumerate(metrics_close):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s4, left_pos, top_pos4, mc_w, mc_h)

        tb_mv = s4.shapes.add_textbox(left_pos + Inches(0.25), top_pos4 + Inches(0.25), mc_w - Inches(0.5), Inches(0.5))
        pmv = tb_mv.text_frame.paragraphs[0]
        pmv.text = mv
        pmv.font.name = "Segoe UI"
        pmv.font.size = Pt(24)
        pmv.font.bold = True
        pmv.font.color.rgb = mc

        tb_ml = s4.shapes.add_textbox(left_pos + Inches(0.25), top_pos4 + Inches(0.8), mc_w - Inches(0.5), Inches(0.35))
        pml = tb_ml.text_frame.paragraphs[0]
        pml.text = ml
        pml.font.name = "Segoe UI"
        pml.font.size = Pt(13)
        pml.font.bold = True
        pml.font.color.rgb = TEXT_WHITE

        tb_md = s4.shapes.add_textbox(left_pos + Inches(0.25), top_pos4 + Inches(1.2), mc_w - Inches(0.5), Inches(0.85))
        pmd = tb_md.text_frame.paragraphs[0]
        pmd.text = md
        pmd.font.name = "Segoe UI"
        pmd.font.size = Pt(10.5)
        pmd.font.color.rgb = TEXT_MUTED

    # Bottom Banner: The Closing Statement
    banner = add_card(s4, Inches(0.8), Inches(4.35), Inches(11.7), Inches(2.4), bg_color=SURFACE_ALT, border_color=CYAN_ACCENT)
    tb_b = s4.shapes.add_textbox(Inches(1.2), Inches(4.6), Inches(10.9), Inches(1.9))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    pb1 = tf_b.paragraphs[0]
    pb1.text = "THE SHARK TANK VERDICT"
    pb1.font.name = "Segoe UI"
    pb1.font.size = Pt(12)
    pb1.font.bold = True
    pb1.font.color.rgb = CYAN_ACCENT

    pb2 = tf_b.add_paragraph()
    pb2.text = "\"Private tutors cost $80 an hour. Campus office hours are packed 2 hours a week.\nPrismatic makes world-class, adaptive cognitive education accessible to every student on campus.\nWe don't just help students pass exams; we eliminate academic paralysis and unlock confidence.\""
    pb2.font.name = "Segoe UI"
    pb2.font.size = Pt(13.5)
    pb2.font.italic = True
    pb2.font.color.rgb = TEXT_WHITE

    pb3 = tf_b.add_paragraph()
    pb3.text = "WE ARE PRISMATIC — REFRACTING COMPLEX KNOWLEDGE INTO YOUR NATIVE SPECTRUM."
    pb3.font.name = "Segoe UI"
    pb3.font.size = Pt(12.5)
    pb3.font.bold = True
    pb3.font.color.rgb = EMERALD_ACCENT

    notes4 = s4.notes_slide.notes_text_frame
    notes4.text = (
        "THE SHARK TANK CLOSE:\n"
        "Private tutors cost $80 an hour. University office hours are 2 hours a week. "
        "Prismatic democratizes elite, personalized cognitive tutoring for every college student on campus with zero barriers to entry.\n"
        "We don't just help students pass exams; we eliminate academic paralysis and unlock confidence. "
        "We are Prismatic—refracting complex knowledge into your native spectrum. Thank you!"
    )

    prs.save(OUTPUT_PPTX)
    print(f"[+] Successfully generated PPTX: {OUTPUT_PPTX}")

def export_to_pdf():
    print("[*] Exporting PPTX to PDF via PowerPoint COM...")
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    deck = powerpoint.Presentations.Open(OUTPUT_PPTX, WithWindow=False)
    # 32 = ppSaveAsPDF
    deck.SaveAs(OUTPUT_PDF, 32)
    deck.Close()
    powerpoint.Quit()
    print(f"[+] Successfully exported PDF: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_deck()
    export_to_pdf()
