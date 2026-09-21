import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import win32com.client
import qrcode
from PIL import Image

# ==============================================================================
# THEME: PRISMATIC OBSIDIAN NEON (Ultra-Premium High-Contrast Shark Tank Theme)
# ==============================================================================
# Base canvas
BG_COLOR = RGBColor(8, 11, 19)          # #080B13 Obsidian Deep Space
SURFACE_CARD = RGBColor(16, 22, 34)     # #101622 Elevated Card Canvas
SURFACE_INNER = RGBColor(22, 30, 48)    # #161E30 Inner Contrast Box
SURFACE_HERO = RGBColor(26, 36, 58)     # #1A243A Focal Hero Card

# Card borders
BORDER_SUBTLE = RGBColor(32, 45, 70)    # #202D46 Clean Subtle Line
BORDER_CYAN = RGBColor(0, 229, 255)     # #00E5FF Glowing Prismatic Cyan
BORDER_VIOLET = RGBColor(168, 85, 247)  # #A855F7 Glowing Violet
BORDER_EMERALD = RGBColor(16, 185, 129) # #10B981 Emerald Win Line

# Prismatic Spectral Accents
CYAN_NEON = RGBColor(0, 229, 255)       # Spectrum Cyan (Primary)
VIOLET_NEON = RGBColor(180, 100, 255)   # Spectrum Violet (Secondary)
AMBER_NEON = RGBColor(251, 191, 36)     # Warm Gold Warning
EMERALD_NEON = RGBColor(52, 211, 153)   # High-Contrast Mint
CORAL_NEON = RGBColor(255, 107, 107)    # Alert Coral

# Typography hierarchy
TEXT_WHITE = RGBColor(255, 255, 255)    # Headers & Major Values
TEXT_HIGH = RGBColor(241, 245, 249)     # Slate 100
TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400
TEXT_DIM = RGBColor(100, 116, 139)      # Slate 500

BASE_DIR = os.path.abspath(r"c:\Users\Saksham Kapoor\Documents\SHARK-TANK-AWS-MLU")
OUTPUT_PPTX = os.path.join(BASE_DIR, "Prismatic_Shark_Tank_Pitch_Deck.pptx")
OUTPUT_PDF = os.path.join(BASE_DIR, "Prismatic_Shark_Tank_Pitch_Deck.pdf")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_qr_code(url, out_path, color=(0, 229, 255), bg=(8, 11, 19)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=bg).convert("RGBA")
    img = img.resize((400, 400), Image.Resampling.LANCZOS)
    img.save(out_path, "PNG")

GITHUB_QR = os.path.join(ASSETS_DIR, "prismatic_github_qr.png")
generate_qr_code("https://github.com/SakshamKapoor2911/SHARK-TANK-AWS-MLU", GITHUB_QR)

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()
    return bg

def add_header(slide, tracker_tag, title_text, subtitle_text="", timing_badge=""):
    # Header tag and timing badge
    tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(9.0), Inches(0.32))
    tf_tag = tb_tag.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = tracker_tag.upper()
    p_tag.font.name = "Segoe UI"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = CYAN_NEON

    if timing_badge:
        # High-visibility timing pill on top right
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.333), Inches(0.35), Inches(2.2), Inches(0.38))
        pill.fill.solid()
        pill.fill.fore_color.rgb = SURFACE_INNER
        pill.line.color.rgb = BORDER_CYAN
        pill.line.width = Pt(1.2)
        tf_p = pill.text_frame
        tf_p.margin_left = tf_p.margin_right = tf_p.margin_top = tf_p.margin_bottom = 0
        p_pill = tf_p.paragraphs[0]
        p_pill.text = timing_badge.upper()
        p_pill.font.name = "Segoe UI"
        p_pill.font.size = Pt(10)
        p_pill.font.bold = True
        p_pill.font.color.rgb = CYAN_NEON
        p_pill.alignment = PP_ALIGN.CENTER

    # Title
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.733), Inches(0.55))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_t = tf_title.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = "Segoe UI"
    p_t.font.size = Pt(23)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE

    if subtitle_text:
        tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.30), Inches(11.733), Inches(0.35))
        tf_sub = tb_sub.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        p_s = tf_sub.paragraphs[0]
        p_s.text = subtitle_text
        p_s.font.name = "Segoe UI"
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_MUTED

def add_card(slide, left, top, width, height, bg_color=SURFACE_CARD, border_color=BORDER_SUBTLE, border_width=1.0):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
    else:
        card.line.fill.background()
    return card

def build_prismatic_masterpiece():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==============================================================================
    # SLIDE 1: TITLE & THE 35-SECOND HOOK (SEGMENTS 1 & 2)
    # ==============================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Top Event Badge
    badge = add_card(s1, Inches(0.8), Inches(0.65), Inches(5.6), Inches(0.42), bg_color=SURFACE_INNER, border_color=BORDER_CYAN, border_width=1.2)
    tb_b = s1.shapes.add_textbox(Inches(0.9), Inches(0.70), Inches(5.4), Inches(0.32))
    p_b = tb_b.text_frame.paragraphs[0]
    p_b.text = "CLOUD CONNECT 2026 · AWS × MLU × BEN TECH · HOWARD UNIVERSITY"
    p_b.font.name = "Segoe UI"
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = CYAN_NEON

    # Big Title Block
    tb_hero = s1.shapes.add_textbox(Inches(0.8), Inches(1.22), Inches(8.5), Inches(1.5))
    tf_h = tb_hero.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h1 = tf_h.paragraphs[0]
    p_h1.text = "PRISMATIC"
    p_h1.font.name = "Segoe UI"
    p_h1.font.size = Pt(48)
    p_h1.font.bold = True
    p_h1.font.color.rgb = TEXT_WHITE

    p_h2 = tf_h.add_paragraph()
    p_h2.text = "Refracting Complex Knowledge Into Your Mind's Native Spectrum"
    p_h2.font.name = "Segoe UI"
    p_h2.font.size = Pt(19)
    p_h2.font.color.rgb = VIOLET_NEON

    # GitHub QR Card on Top Right
    qr_card = add_card(s1, Inches(9.8), Inches(0.65), Inches(2.733), Inches(2.1), bg_color=SURFACE_CARD, border_color=BORDER_SUBTLE)
    if os.path.exists(GITHUB_QR):
        s1.shapes.add_picture(GITHUB_QR, Inches(10.0), Inches(0.78), Inches(1.2), Inches(1.2))
    
    tb_qr = s1.shapes.add_textbox(Inches(11.3), Inches(0.82), Inches(1.15), Inches(1.2))
    tf_qr = tb_qr.text_frame
    tf_qr.word_wrap = True
    tf_qr.margin_left = tf_qr.margin_top = tf_qr.margin_right = tf_qr.margin_bottom = 0
    pq1 = tf_qr.paragraphs[0]
    pq1.text = "SCAN TO VIEW"
    pq1.font.name = "Segoe UI"
    pq1.font.size = Pt(10)
    pq1.font.bold = True
    pq1.font.color.rgb = CYAN_NEON
    pq2 = tf_qr.add_paragraph()
    pq2.text = "Live GitHub repo, prompts, and Quick specs."
    pq2.font.name = "Segoe UI"
    pq2.font.size = Pt(8.5)
    pq2.font.color.rgb = TEXT_MUTED

    # 3 High-Impact Narrative Columns for Segments 1 & 2
    cards_s1 = [
        ("SEGMENT 1: 10 SECONDS", "High-Energy Intro", "We are Prismatic — 10 builders solving college cognitive overload.", "TEAM ENERGY", CYAN_NEON, BORDER_CYAN),
        ("SEGMENT 2: 25 SECONDS", "The 300-Student Hook", "1 professor. 300 students. 1 static format. White light has every color, but lectures project only one shade.", "THE CRISIS", CORAL_NEON, BORDER_SUBTLE),
        ("THE EMOTIONAL TRUTH", "Cognitive Mismatch", "Students don't freeze from lack of intelligence; they freeze when raw syllabus format clashes with their brain.", "THE CORE MISSION", EMERALD_NEON, BORDER_EMERALD)
    ]
    c_w = Inches(3.7)
    c_h = Inches(4.1)
    top_pos = Inches(2.95)

    for i, (tag, title, desc, pill_text, color, border) in enumerate(cards_s1):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s1, left_pos, top_pos, c_w, c_h, bg_color=SURFACE_CARD, border_color=border, border_width=1.4 if border != BORDER_SUBTLE else 1.0)
        
        # Pill inside card
        pill = add_card(s1, left_pos + Inches(0.3), top_pos + Inches(0.35), Inches(2.2), Inches(0.32), bg_color=SURFACE_INNER, border_color=color, border_width=1.0)
        tb_p = s1.shapes.add_textbox(left_pos + Inches(0.35), top_pos + Inches(0.39), Inches(2.1), Inches(0.25))
        p_pill = tb_p.text_frame.paragraphs[0]
        p_pill.text = pill_text
        p_pill.font.name = "Segoe UI"
        p_pill.font.size = Pt(9)
        p_pill.font.bold = True
        p_pill.font.color.rgb = color

        # Tag
        tb_tag = s1.shapes.add_textbox(left_pos + Inches(0.3), top_pos + Inches(0.85), c_w - Inches(0.6), Inches(0.35))
        pt = tb_tag.text_frame.paragraphs[0]
        pt.text = tag
        pt.font.name = "Segoe UI"
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = color

        # Title
        tb_t = s1.shapes.add_textbox(left_pos + Inches(0.3), top_pos + Inches(1.25), c_w - Inches(0.6), Inches(0.45))
        ptt = tb_t.text_frame.paragraphs[0]
        ptt.text = title
        ptt.font.name = "Segoe UI"
        ptt.font.size = Pt(15)
        ptt.font.bold = True
        ptt.font.color.rgb = TEXT_WHITE

        # Desc
        tb_d = s1.shapes.add_textbox(left_pos + Inches(0.3), top_pos + Inches(1.85), c_w - Inches(0.6), Inches(2.0))
        pd = tb_d.text_frame.paragraphs[0]
        pd.text = desc
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MUTED

    notes1 = s1.notes_slide.notes_text_frame
    notes1.text = (
        "OFFICIAL TIMED SCRIPT (0:00 - 0:35):\n\n"
        "[0:00 - 0:10] SEGMENT 1: TEAM NAME (10s)\n"
        "\"Good afternoon, judges and fellow builders! We are PRISMATIC—and we are here to refract the way college students learn!\"\n\n"
        "[0:10 - 0:35] SEGMENT 2: THE HOOK (25s)\n"
        "\"Picture a 300-person lecture hall right here at Howard or UMD. The professor spends 75 minutes covering one complex concept. Half the class nods; the other half walks out completely lost with intense brain fog.\n"
        "The problem isn't student intellect. White light contains every color, but a flat chalkboard only projects one shade. Professors teach in one rigid format, while human brains process knowledge in completely different spectrums.\""
    )

    # ==============================================================================
    # SLIDE 2: SEGMENT 3 (YOUR APP OVERVIEW - 45 SECONDS)
    # ==============================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Segment 3: App Overview (45s)", "The 4 Refracted Learning Spectrums: Zero Errors, Pure Retention", "A pipelined architecture orchestrated in 60 minutes on Amazon Quick & Amazon Bedrock", "45 SECONDS")

    spectrums_data = [
        ("SPECTRUM 1: ANALOGY", "Dorm & Dining Hall Metaphors", "Translates abstract theory into daily campus reality. E.g., Dijkstra's shortest path = navigating peak dining hall line rush.", "METAPHORICAL", CYAN_NEON, BORDER_CYAN),
        ("SPECTRUM 2: VISUAL MAP", "ASCII & Schematic Blueprints", "Renders execution trees, logical branches, and state machines into structural mental schemas for STEM/CS.", "SCHEMATIC", VIOLET_NEON, BORDER_VIOLET),
        ("SPECTRUM 3: SOCRATIC SPARRING", "Active Retrieval Partner", "Chatbot strictly capped at 2 sentences; never lectures; fires progressive edge cases to force active recall.", "KINESTHETIC", EMERALD_NEON, BORDER_EMERALD),
        ("SPECTRUM 4: EXAM TRAP DECK", "4-Slide Micro-Presentation", "Exposes the exact trick questions professors test on Midterm #2, coupled with an AI visual memory anchor.", "SYNTHESIS", AMBER_NEON, BORDER_SUBTLE)
    ]

    sp_w = Inches(5.7)
    sp_h = Inches(2.45)

    for i, (spec_tag, spec_title, spec_desc, badge_text, color, border) in enumerate(spectrums_data):
        col = i % 2
        row = i // 2
        left_pos = Inches(0.8 + col * (5.7 + 0.3))
        top_pos2 = Inches(1.8) + row * (Inches(2.45 + 0.28))

        add_card(s2, left_pos, top_pos2, sp_w, sp_h, bg_color=SURFACE_CARD, border_color=border, border_width=1.3)

        # Internal Badge
        pill = add_card(s2, left_pos + Inches(0.28), top_pos2 + Inches(0.25), Inches(1.8), Inches(0.28), bg_color=SURFACE_INNER, border_color=color)
        tb_p = s2.shapes.add_textbox(left_pos + Inches(0.3), top_pos2 + Inches(0.27), Inches(1.76), Inches(0.25))
        pp = tb_p.text_frame.paragraphs[0]
        pp.text = badge_text
        pp.font.name = "Segoe UI"
        pp.font.size = Pt(8.5)
        pp.font.bold = True
        pp.font.color.rgb = color
        pp.alignment = PP_ALIGN.CENTER

        # Title
        tb_t = s2.shapes.add_textbox(left_pos + Inches(0.28), top_pos2 + Inches(0.65), sp_w - Inches(0.56), Inches(0.45))
        ptt = tb_t.text_frame.paragraphs[0]
        ptt.text = spec_title
        ptt.font.name = "Segoe UI"
        ptt.font.size = Pt(14.5)
        ptt.font.bold = True
        ptt.font.color.rgb = TEXT_WHITE

        # Subtag
        tb_st = s2.shapes.add_textbox(left_pos + Inches(0.28), top_pos2 + Inches(1.05), sp_w - Inches(0.56), Inches(0.3))
        pst = tb_st.text_frame.paragraphs[0]
        pst.text = spec_tag
        pst.font.name = "Segoe UI"
        pst.font.size = Pt(10.5)
        pst.font.bold = True
        pst.font.color.rgb = color

        # Desc
        tb_d = s2.shapes.add_textbox(left_pos + Inches(0.28), top_pos2 + Inches(1.4), sp_w - Inches(0.56), Inches(0.95))
        pd = tb_d.text_frame.paragraphs[0]
        pd.text = spec_desc
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_MUTED

    notes2 = s2.notes_slide.notes_text_frame
    notes2.text = (
        "OFFICIAL TIMED SCRIPT (0:35 - 1:20):\n\n"
        "[0:35 - 1:20] SEGMENT 3: YOUR APP (45s)\n"
        "\"We built Prismatic on Amazon Quick—an agentic cognitive engine that turns 1 static lecture into 4 tailored learning modalities in under 30 seconds.\n"
        "First, a rapid 5-question diagnostic maps how your brain absorbs information. Then, our Amazon Bedrock pipeline instantly refracts the material:\n"
        "- Spectrum 1 translates abstract theory into relatable dorm and dining hall analogies.\n"
        "- Spectrum 2 renders structural ASCII concept maps.\n"
        "- Spectrum 3 launches a Socratic Sparring Partner that quizzes you one edge-case at a time without spoiling answers.\n"
        "- And Spectrum 4 builds a 4-slide micro-deck exposing the exact trap questions professors test on midterms.\""
    )

    # ==============================================================================
    # SLIDE 3: SEGMENT 4 (WHY IT WINS - 25 SECONDS)
    # ==============================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Segment 4: Why It Wins (25s)", "The Unfair Advantage: Why Prismatic Destroys Generic Tools", "Who uses this, and why is it exponentially better than everything on the market?", "25 SECONDS")

    wins_data = [
        ("VS. CHATGPT / LLMS", "Active Sparring vs. Passive Text", "ChatGPT dumps 800-word walls of text that cause immediate student eye glaze. Prismatic bounds answers to 2 sentences and forces active retrieval.", CYAN_NEON, BORDER_CYAN),
        ("VS. $80/HR TUTORING", "Zero Financial Gatekeeping", "Private tutors cost $80/hr; university office hours are 2 hours a week. Prismatic gives every student 24/7 elite adaptive tutoring for pennies on Bedrock.", CORAL_NEON, BORDER_SUBTLE),
        ("VS. STATIC SLIDES", "Dynamic Cognitive Fit", "Eliminates task paralysis for ADHD, visual, and conceptual learners through a 30-second diagnostic triage.", EMERALD_NEON, BORDER_EMERALD)
    ]

    w_w = Inches(3.7)
    w_h = Inches(4.9)
    top_pos_w = Inches(1.8)

    for i, (w_tag, w_title, w_desc, color, border) in enumerate(wins_data):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s3, left_pos, top_pos_w, w_w, w_h, bg_color=SURFACE_CARD, border_color=border, border_width=1.3)

        # Header tag
        tb_wt = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos_w + Inches(0.4), w_w - Inches(0.6), Inches(0.35))
        pwt = tb_wt.text_frame.paragraphs[0]
        pwt.text = w_tag
        pwt.font.name = "Segoe UI"
        pwt.font.size = Pt(12)
        pwt.font.bold = True
        pwt.font.color.rgb = color

        # Title
        tb_wl = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos_w + Inches(0.85), w_w - Inches(0.6), Inches(0.55))
        pwl = tb_wl.text_frame.paragraphs[0]
        pwl.text = w_title
        pwl.font.name = "Segoe UI"
        pwl.font.size = Pt(14)
        pwl.font.bold = True
        pwl.font.color.rgb = TEXT_WHITE

        # Desc
        tb_wd = s3.shapes.add_textbox(left_pos + Inches(0.3), top_pos_w + Inches(1.5), w_w - Inches(0.6), Inches(2.9))
        pwd = tb_wd.text_frame.paragraphs[0]
        pwd.text = w_desc
        pwd.font.name = "Segoe UI"
        pwd.font.size = Pt(12)
        pwd.font.color.rgb = TEXT_MUTED

    notes3 = s3.notes_slide.notes_text_frame
    notes3.text = (
        "OFFICIAL TIMED SCRIPT (1:20 - 1:45):\n\n"
        "[1:20 - 1:45] SEGMENT 4: WHY IT WINS (25s)\n"
        "\"Over 20 million college students face academic paralysis every semester.\n"
        "Generic tools like ChatGPT just dump dry walls of text that students glaze over.\n"
        "Private tutoring costs $80 an hour, and professor office hours are only 2 hours a week.\n"
        "Prismatic is active, multi-modal, and adapts the syllabus to the student—democratizing elite private tutoring for pennies.\""
    )

    # ==============================================================================
    # SLIDE 4: SEGMENT 5 (THE CLOSE - 15s) & SHARK CRITERIA DEFENSE
    # ==============================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Segment 5: The Close (15s)", "'With More Time We'd Add...' & The Shark Tank Verdict", "Scoring 100% across the 4 official Shark metrics: Creativity, Usefulness, Execution & Teamwork", "15 SECONDS")

    # 4 Shark Criterion Pill Cards
    criteria_data = [
        ("CREATIVITY", "Fresh cognitive refraction metaphor", CYAN_NEON),
        ("USEFULNESS", "Solves dorm paralysis & exam panic", EMERALD_NEON),
        ("EXECUTION", "6-widget pipeline on Amazon Quick", VIOLET_NEON),
        ("TEAMWORK", "10 teammates with active stage roles", AMBER_NEON)
    ]
    sc_w = Inches(2.7)
    sc_h = Inches(1.55)
    for i, (ct, cd, cc) in enumerate(criteria_data):
        left_pos = Inches(0.8 + i * (2.7 + 0.3))
        add_card(s4, left_pos, Inches(1.8), sc_w, sc_h, bg_color=SURFACE_CARD, border_color=BORDER_SUBTLE)

        tb_ct = s4.shapes.add_textbox(left_pos + Inches(0.2), Inches(1.95), sc_w - Inches(0.4), Inches(0.35))
        pct = tb_ct.text_frame.paragraphs[0]
        pct.text = ct
        pct.font.name = "Segoe UI"
        pct.font.size = Pt(12)
        pct.font.bold = True
        pct.font.color.rgb = cc

        tb_cd = s4.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.35), sc_w - Inches(0.4), Inches(0.9))
        pcd = tb_cd.text_frame.paragraphs[0]
        pcd.text = cd
        pcd.font.name = "Segoe UI"
        pcd.font.size = Pt(10.5)
        pcd.font.color.rgb = TEXT_HIGH

    # Master Close Box
    banner = add_card(s4, Inches(0.8), Inches(3.6), Inches(11.733), Inches(3.3), bg_color=SURFACE_CARD, border_color=BORDER_CYAN, border_width=1.6)
    tb_b = s4.shapes.add_textbox(Inches(1.2), Inches(3.85), Inches(10.9), Inches(2.8))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    pb1 = tf_b.paragraphs[0]
    pb1.text = "OFFICIAL HANDOUT MANDATE: 'WITH MORE TIME WE'D ADD...'"
    pb1.font.name = "Segoe UI"
    pb1.font.size = Pt(12)
    pb1.font.bold = True
    pb1.font.color.rgb = CYAN_NEON

    pb2 = tf_b.add_paragraph()
    pb2.text = "\"With more time, we’d add live Canvas and syllabus LMS integration, automatically syncing weekly exam dates and generating proactive 15-minute micro-sprints before every morning class.\n\nWe don't just help students pass exams; we eliminate academic paralysis and unlock confidence.\""
    pb2.font.name = "Segoe UI"
    pb2.font.size = Pt(13.5)
    pb2.font.italic = True
    pb2.font.color.rgb = TEXT_WHITE

    pb3 = tf_b.add_paragraph()
    pb3.text = "WE ARE PRISMATIC — REFRACTING COMPLEX KNOWLEDGE INTO YOUR NATIVE SPECTRUM. VOTE PRISMATIC!"
    pb3.font.name = "Segoe UI"
    pb3.font.size = Pt(13)
    pb3.font.bold = True
    pb3.font.color.rgb = EMERALD_NEON

    notes4 = s4.notes_slide.notes_text_frame
    notes4.text = (
        "OFFICIAL TIMED SCRIPT (1:45 - 2:00):\n\n"
        "[1:45 - 2:00] SEGMENT 5: THE CLOSE (15s)\n"
        "\"With more time, we’d add live Canvas and syllabus LMS integration, automatically syncing weekly exam dates and generating proactive 15-minute micro-sprints before every morning class.\n"
        "We are PRISMATIC—refracting complex knowledge into your native spectrum.\n"
        "Vote Prismatic for your room champion! Thank you!\""
    )

    prs.save(OUTPUT_PPTX)
    print(f"[+] Successfully generated Masterpiece PPTX: {OUTPUT_PPTX}")

def export_to_pdf():
    print("[*] Exporting Masterpiece PPTX to PDF via PowerPoint COM...")
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    deck = powerpoint.Presentations.Open(OUTPUT_PPTX, WithWindow=False)
    deck.SaveAs(OUTPUT_PDF, 32)
    deck.Close()
    powerpoint.Quit()
    print(f"[+] Successfully exported Masterpiece PDF: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_prismatic_masterpiece()
    export_to_pdf()
