"""Build the Prismatic Shark Tank pitch deck (PPTX) and export PDF + slide PNGs.

Usage:
    python build_prismatic_deck.py [--skip-pdf] [--skip-images]
        [--pptx PATH] [--pdf PATH]

Design: Prismatic Obsidian Neon, 16:9 widescreen (13.333 x 7.5 in).
PDF export tries PowerPoint COM first (Windows), then LibreOffice fallback.
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# THEME: PRISMATIC OBSIDIAN NEON (Ultra-Premium High-Contrast Shark Tank Theme)
# ==============================================================================
BG_COLOR = RGBColor(8, 11, 19)          # #080B13 Obsidian Deep Space
SURFACE_CARD = RGBColor(16, 22, 34)     # #101622 Elevated Card Canvas
SURFACE_INNER = RGBColor(22, 30, 48)    # #161E30 Inner Contrast Box
SURFACE_HERO = RGBColor(26, 36, 58)     # #1A243A Focal Hero Card

BORDER_SUBTLE = RGBColor(32, 45, 70)    # #202D46 Clean Subtle Line
BORDER_CYAN = RGBColor(0, 229, 255)     # #00E5FF Glowing Prismatic Cyan
BORDER_VIOLET = RGBColor(168, 85, 247)  # #A855F7 Glowing Violet
BORDER_EMERALD = RGBColor(16, 185, 129) # #10B981 Emerald Win Line

CYAN_NEON = RGBColor(0, 229, 255)
VIOLET_NEON = RGBColor(180, 100, 255)
AMBER_NEON = RGBColor(251, 191, 36)
EMERALD_NEON = RGBColor(52, 211, 153)
CORAL_NEON = RGBColor(255, 107, 107)

TEXT_WHITE = RGBColor(255, 255, 255)
TEXT_HIGH = RGBColor(241, 245, 249)
TEXT_MUTED = RGBColor(148, 163, 184)
TEXT_DIM = RGBColor(100, 116, 139)

FONT_NAME = "Segoe UI"
# Minimum body size for back-row / PDF-print readability. Footers excepted.
MIN_BODY_PT = 10.5

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PPTX = BASE_DIR / "Prismatic_Shark_Tank_Pitch_Deck.pptx"
OUTPUT_PDF = BASE_DIR / "Prismatic_Shark_Tank_Pitch_Deck.pdf"
ASSETS_DIR = BASE_DIR / "assets"
GITHUB_URL = "https://github.com/SakshamKapoor2911/SHARK-TANK-AWS-MLU"
GITHUB_QR = ASSETS_DIR / "prismatic_github_qr.png"
TOTAL_SLIDES = 4


# ---------------------------------------------------------------- helpers ---
def _send_to_back(shape):
    """Move a shape behind all other shapes (true background)."""
    sp_tree = shape._element.getparent()
    sp_tree.remove(shape._element)
    # index 2 = just after the required nvGrpSpPr element
    sp_tree.insert(2, shape._element)


def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()
    _send_to_back(bg)
    return bg


def add_top_accent(slide):
    """Thin cyan/violet brand bar pinned to the top edge."""
    bar_h = Inches(0.06)
    left = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(6.667), bar_h)
    left.fill.solid()
    left.fill.fore_color.rgb = CYAN_NEON
    left.line.fill.background()
    right = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.667), 0, Inches(6.666), bar_h)
    right.fill.solid()
    right.fill.fore_color.rgb = VIOLET_NEON
    right.line.fill.background()
    return (left, right)


def add_footer(slide, idx, total=TOTAL_SLIDES):
    """Small event label (left) + slide number (right) for judge reference."""
    tb_l = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(6.0), Inches(0.25))
    tf = tb_l.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CLOUD CONNECT 2026  •  PRISMATIC"
    p.font.name = FONT_NAME
    p.font.size = Pt(8)
    p.font.color.rgb = TEXT_DIM

    tb_r = slide.shapes.add_textbox(Inches(11.5), Inches(7.08), Inches(1.0), Inches(0.25))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_r = tf_r.paragraphs[0]
    p_r.text = f"{idx} / {total}"
    p_r.font.name = FONT_NAME
    p_r.font.size = Pt(8)
    p_r.font.color.rgb = TEXT_DIM
    p_r.alignment = PP_ALIGN.RIGHT


def add_textbox(slide, left, top, width, height, text, size,
                bold=False, italic=False, color=TEXT_WHITE,
                alignment=PP_ALIGN.LEFT):
    """Single helper: consistent font, wrapping, and shrink-to-fit safety."""
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    # Shrink oversized copy instead of clipping on projector / PDF.
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = FONT_NAME
    p.font.size = Pt(max(size, MIN_BODY_PT) if not bold or size >= 10 else Pt(size))
    p.font.bold = bold
    p.font.italic = italic
    p.font.color.rgb = color
    p.alignment = alignment
    return tb


def add_card(slide, left, top, width, height, bg_color=SURFACE_CARD,
             border_color=BORDER_SUBTLE, border_width=1.0):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    try:
        card.adjustments[0] = 0.08
    except Exception:
        pass
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
    else:
        card.line.fill.background()
    return card


def ensure_qr_code(url=GITHUB_URL, out_path=GITHUB_QR, box_px=400):
    """Generate a *scannable* QR: dark modules on a white quiet zone.

    Previous cyan-on-obsidian QR looked on-brand but fails phone scanners
    under stage lighting. White card = reliable scan; card chrome keeps theme.
    """
    try:
        import qrcode
        from PIL import Image
    except ImportError as exc:
        print(f"[!] QR deps missing ({exc}); skipping QR. pip install qrcode pillow",
              file=sys.stderr)
        return None
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,  # full quiet zone = required for scanning
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    # NEAREST keeps module edges crisp; LANCZOS blurs them and hurts scanning.
    img = img.resize((box_px, box_px), Image.NEAREST)
    img.save(out_path, "PNG")
    return out_path


def add_header(slide, tracker_tag, title_text, subtitle_text="", timing_badge=""):
    add_textbox(slide, Inches(0.8), Inches(0.38), Inches(9.0), Inches(0.32),
                tracker_tag.upper(), 11, bold=True, color=CYAN_NEON)

    if timing_badge:
        pill = add_card(slide, Inches(10.333), Inches(0.35), Inches(2.2),
                        Inches(0.38), bg_color=SURFACE_INNER, border_color=BORDER_CYAN,
                        border_width=1.2)
        pill.text_frame.margin_left = pill.text_frame.margin_right = 0
        pill.text_frame.margin_top = pill.text_frame.margin_bottom = 0
        pill.text_frame.word_wrap = True
        pill.text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
        pp = pill.text_frame.paragraphs[0]
        pp.text = timing_badge.upper()
        pp.font.name = FONT_NAME
        pp.font.size = Pt(10)
        pp.font.bold = True
        pp.font.color.rgb = CYAN_NEON
        pp.alignment = PP_ALIGN.CENTER

    add_textbox(slide, Inches(0.8), Inches(0.72), Inches(11.733), Inches(0.55),
                title_text, 23, bold=True, color=TEXT_WHITE)
    if subtitle_text:
        add_textbox(slide, Inches(0.8), Inches(1.30), Inches(11.733), Inches(0.35),
                    subtitle_text, MIN_BODY_PT, color=TEXT_MUTED)


def build_prismatic_masterpiece(output_pptx=OUTPUT_PPTX):
    output_pptx = Path(output_pptx)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    qr_path = ensure_qr_code()

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==================================================================
    # SLIDE 1: TITLE & THE 35-SECOND HOOK (SEGMENTS 1 & 2)
    # ==================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_top_accent(s1)

    add_card(s1, Inches(0.8), Inches(0.65), Inches(5.6), Inches(0.42),
             bg_color=SURFACE_INNER, border_color=BORDER_CYAN, border_width=1.2)
    add_textbox(s1, Inches(0.9), Inches(0.70), Inches(5.4), Inches(0.32),
                "CLOUD CONNECT 2026 \u00b7 AWS \u00d7 MLU \u00d7 BEN TECH \u00b7 HOWARD UNIVERSITY",
                10, bold=True, color=CYAN_NEON)

    tb_hero = s1.shapes.add_textbox(Inches(0.8), Inches(1.22), Inches(8.5), Inches(1.5))
    tf_h = tb_hero.text_frame
    tf_h.word_wrap = True
    tf_h.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h1 = tf_h.paragraphs[0]
    p_h1.text = "PRISMATIC"
    p_h1.font.name = FONT_NAME
    p_h1.font.size = Pt(48)
    p_h1.font.bold = True
    p_h1.font.color.rgb = TEXT_WHITE
    p_h2 = tf_h.add_paragraph()
    p_h2.text = "Refracting Complex Knowledge Into Your Mind's Native Spectrum"
    p_h2.font.name = FONT_NAME
    p_h2.font.size = Pt(19)
    p_h2.font.color.rgb = VIOLET_NEON

    # GitHub QR card (white QR tile = scannable; dark card keeps theme)
    add_card(s1, Inches(9.8), Inches(0.65), Inches(2.733), Inches(2.1),
             bg_color=SURFACE_CARD, border_color=BORDER_SUBTLE)
    if qr_path and qr_path.exists():
        s1.shapes.add_picture(str(qr_path), Inches(10.0), Inches(0.78),
                              Inches(1.2), Inches(1.2))

    tb_qr = s1.shapes.add_textbox(Inches(11.3), Inches(0.82), Inches(1.15), Inches(1.2))
    tf_qr = tb_qr.text_frame
    tf_qr.word_wrap = True
    tf_qr.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf_qr.margin_left = tf_qr.margin_top = tf_qr.margin_right = tf_qr.margin_bottom = 0
    pq1 = tf_qr.paragraphs[0]
    pq1.text = "SCAN TO VIEW"
    pq1.font.name = FONT_NAME
    pq1.font.size = Pt(10)
    pq1.font.bold = True
    pq1.font.color.rgb = CYAN_NEON
    pq2 = tf_qr.add_paragraph()
    pq2.text = "Live GitHub repo, prompts, and Quick specs."
    pq2.font.name = FONT_NAME
    pq2.font.size = Pt(MIN_BODY_PT)
    pq2.font.color.rgb = TEXT_MUTED

    cards_s1 = [
        ("SEGMENT 1: 10 SECONDS", "High-Energy Intro",
         "We are Prismatic \u2014 10 builders solving college cognitive overload.",
         "TEAM ENERGY", CYAN_NEON, BORDER_CYAN),
        ("SEGMENT 2: 25 SECONDS", "The 300-Student Hook",
         "1 professor. 300 students. 1 static format. White light has every color, but lectures project only one shade.",
         "THE CRISIS", CORAL_NEON, BORDER_SUBTLE),
        ("THE EMOTIONAL TRUTH", "Cognitive Mismatch",
         "Students don't freeze from lack of intelligence; they freeze when raw syllabus format clashes with their brain.",
         "THE CORE MISSION", EMERALD_NEON, BORDER_EMERALD),
    ]
    c_w, c_h, top_pos = Inches(3.7), Inches(4.1), Inches(2.95)
    for i, (tag, title, desc, pill_text, color, border) in enumerate(cards_s1):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s1, left_pos, top_pos, c_w, c_h, bg_color=SURFACE_CARD,
                 border_color=border, border_width=1.4 if border != BORDER_SUBTLE else 1.0)
        add_card(s1, left_pos + Inches(0.3), top_pos + Inches(0.35),
                 Inches(2.2), Inches(0.32), bg_color=SURFACE_INNER, border_color=color)
        add_textbox(s1, left_pos + Inches(0.35), top_pos + Inches(0.39),
                    Inches(2.1), Inches(0.25), pill_text, 10, bold=True, color=color)
        add_textbox(s1, left_pos + Inches(0.3), top_pos + Inches(0.85),
                    c_w - Inches(0.6), Inches(0.35), tag, 12, bold=True, color=color)
        add_textbox(s1, left_pos + Inches(0.3), top_pos + Inches(1.25),
                    c_w - Inches(0.6), Inches(0.45), title, 15, bold=True, color=TEXT_WHITE)
        add_textbox(s1, left_pos + Inches(0.3), top_pos + Inches(1.85),
                    c_w - Inches(0.6), Inches(2.0), desc, 12, color=TEXT_MUTED)

    add_footer(s1, 1)
    s1.notes_slide.notes_text_frame.text = (
        "OFFICIAL TIMED SCRIPT (0:00 - 0:35):\n\n"
        "[0:00 - 0:10] SEGMENT 1: TEAM NAME (10s)\n"
        "\"Good afternoon, judges and fellow builders! We are PRISMATIC\u2014and we are here to refract the way college students learn!\"\n\n"
        "[0:10 - 0:35] SEGMENT 2: THE HOOK (25s)\n"
        "\"Picture a 300-person lecture hall right here at Howard or UMD. The professor spends 75 minutes covering one complex concept. Half the class nods; the other half walks out completely lost with intense brain fog.\n"
        "The problem isn't student intellect. White light contains every color, but a flat chalkboard only projects one shade. Professors teach in one rigid format, while human brains process knowledge in completely different spectrums.\""
    )

    # ==================================================================
    # SLIDE 2: SEGMENT 3 (YOUR APP OVERVIEW - 45 SECONDS)
    # ==================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_top_accent(s2)
    add_header(s2, "Segment 3: App Overview (45s)",
               "The 4 Refracted Learning Spectrums: Zero Errors, Pure Retention",
               "A pipelined architecture orchestrated in 60 minutes on Amazon Quick & Amazon Bedrock",
               "45 SECONDS")

    spectrums_data = [
        ("SPECTRUM 1: ANALOGY", "Dorm & Dining Hall Metaphors",
         "Translates abstract theory into daily campus reality. E.g., Dijkstra's shortest path = navigating peak dining hall line rush.",
         "METAPHORICAL", CYAN_NEON, BORDER_CYAN),
        ("SPECTRUM 2: VISUAL MAP", "ASCII & Schematic Blueprints",
         "Renders execution trees, logical branches, and state machines into structural mental schemas for STEM/CS.",
         "SCHEMATIC", VIOLET_NEON, BORDER_VIOLET),
        ("SPECTRUM 3: SOCRATIC SPARRING", "Active Retrieval Partner",
         "Chatbot strictly capped at 2 sentences; never lectures; fires progressive edge cases to force active recall.",
         "KINESTHETIC", EMERALD_NEON, BORDER_EMERALD),
        ("SPECTRUM 4: EXAM TRAP DECK", "4-Slide Micro-Presentation",
         "Exposes the exact trick questions professors test on Midterm #2, coupled with an AI visual memory anchor.",
         "SYNTHESIS", AMBER_NEON, BORDER_SUBTLE),
    ]
    sp_w, sp_h = Inches(5.7), Inches(2.45)
    for i, (spec_tag, spec_title, spec_desc, badge_text, color, border) in enumerate(spectrums_data):
        col, row = i % 2, i // 2
        left_pos = Inches(0.8 + col * (5.7 + 0.3))
        top_pos2 = Inches(1.8) + row * Inches(2.45 + 0.28)
        add_card(s2, left_pos, top_pos2, sp_w, sp_h, bg_color=SURFACE_CARD,
                 border_color=border, border_width=1.3)
        add_card(s2, left_pos + Inches(0.28), top_pos2 + Inches(0.25),
                 Inches(1.8), Inches(0.28), bg_color=SURFACE_INNER, border_color=color)
        add_textbox(s2, left_pos + Inches(0.3), top_pos2 + Inches(0.27),
                    Inches(1.76), Inches(0.25), badge_text, 10, bold=True,
                    color=color, alignment=PP_ALIGN.CENTER)
        add_textbox(s2, left_pos + Inches(0.28), top_pos2 + Inches(0.65),
                    sp_w - Inches(0.56), Inches(0.45), spec_title, 14.5,
                    bold=True, color=TEXT_WHITE)
        add_textbox(s2, left_pos + Inches(0.28), top_pos2 + Inches(1.05),
                    sp_w - Inches(0.56), Inches(0.3), spec_tag, MIN_BODY_PT,
                    bold=True, color=color)
        add_textbox(s2, left_pos + Inches(0.28), top_pos2 + Inches(1.4),
                    sp_w - Inches(0.56), Inches(0.95), spec_desc, 11, color=TEXT_MUTED)

    add_footer(s2, 2)
    s2.notes_slide.notes_text_frame.text = (
        "OFFICIAL TIMED SCRIPT (0:35 - 1:20):\n\n"
        "[0:35 - 1:20] SEGMENT 3: YOUR APP (45s)\n"
        "\"We built Prismatic on Amazon Quick\u2014an agentic cognitive engine that turns 1 static lecture into 4 tailored learning modalities in under 30 seconds.\n"
        "First, a rapid 5-question diagnostic maps how your brain absorbs information. Then, our Amazon Bedrock pipeline instantly refracts the material:\n"
        "- Spectrum 1 translates abstract theory into relatable dorm and dining hall analogies.\n"
        "- Spectrum 2 renders structural ASCII concept maps.\n"
        "- Spectrum 3 launches a Socratic Sparring Partner that quizzes you one edge-case at a time without spoiling answers.\n"
        "- And Spectrum 4 builds a 4-slide micro-deck exposing the exact trap questions professors test on midterms.\""
    )

    # ==================================================================
    # SLIDE 3: SEGMENT 4 (WHY IT WINS - 25 SECONDS)
    # ==================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_top_accent(s3)
    add_header(s3, "Segment 4: Why It Wins (25s)",
               "The Unfair Advantage: Why Prismatic Destroys Generic Tools",
               "Who uses this, and why is it exponentially better than everything on the market?",
               "25 SECONDS")

    wins_data = [
        ("VS. CHATGPT / LLMS", "Active Sparring vs. Passive Text",
         "ChatGPT dumps 800-word walls of text that cause immediate student eye glaze. Prismatic bounds answers to 2 sentences and forces active retrieval.",
         CYAN_NEON, BORDER_CYAN),
        ("VS. $80/HR TUTORING", "Zero Financial Gatekeeping",
         "Private tutors cost $80/hr; university office hours are 2 hours a week. Prismatic gives every student 24/7 elite adaptive tutoring for pennies on Bedrock.",
         CORAL_NEON, BORDER_SUBTLE),
        ("VS. STATIC SLIDES", "Dynamic Cognitive Fit",
         "Eliminates task paralysis for ADHD, visual, and conceptual learners through a 30-second diagnostic triage.",
         EMERALD_NEON, BORDER_EMERALD),
    ]
    w_w, w_h, top_pos_w = Inches(3.7), Inches(4.9), Inches(1.8)
    for i, (w_tag, w_title, w_desc, color, border) in enumerate(wins_data):
        left_pos = Inches(0.8 + i * (3.7 + 0.3))
        add_card(s3, left_pos, top_pos_w, w_w, w_h, bg_color=SURFACE_CARD,
                 border_color=border, border_width=1.3)
        add_textbox(s3, left_pos + Inches(0.3), top_pos_w + Inches(0.4),
                    w_w - Inches(0.6), Inches(0.35), w_tag, 12, bold=True, color=color)
        add_textbox(s3, left_pos + Inches(0.3), top_pos_w + Inches(0.85),
                    w_w - Inches(0.6), Inches(0.55), w_title, 14, bold=True, color=TEXT_WHITE)
        add_textbox(s3, left_pos + Inches(0.3), top_pos_w + Inches(1.5),
                    w_w - Inches(0.6), Inches(2.9), w_desc, 12, color=TEXT_MUTED)

    add_footer(s3, 3)
    s3.notes_slide.notes_text_frame.text = (
        "OFFICIAL TIMED SCRIPT (1:20 - 1:45):\n\n"
        "[1:20 - 1:45] SEGMENT 4: WHY IT WINS (25s)\n"
        "\"Over 20 million college students face academic paralysis every semester.\n"
        "Generic tools like ChatGPT just dump dry walls of text that students glaze over.\n"
        "Private tutoring costs $80 an hour, and professor office hours are only 2 hours a week.\n"
        "Prismatic is active, multi-modal, and adapts the syllabus to the student\u2014democratizing elite private tutoring for pennies.\""
    )

    # ==================================================================
    # SLIDE 4: SEGMENT 5 (THE CLOSE - 15s) & SHARK CRITERIA DEFENSE
    # ==================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_top_accent(s4)
    add_header(s4, "Segment 5: The Close (15s)",
               "'With More Time We'd Add...' & The Shark Tank Verdict",
               "Scoring 100% across the 4 official Shark metrics: Creativity, Usefulness, Execution & Teamwork",
               "15 SECONDS")

    criteria_data = [
        ("CREATIVITY", "Fresh cognitive refraction metaphor", CYAN_NEON),
        ("USEFULNESS", "Solves dorm paralysis & exam panic", EMERALD_NEON),
        ("EXECUTION", "6-widget pipeline on Amazon Quick", VIOLET_NEON),
        ("TEAMWORK", "10 teammates with active stage roles", AMBER_NEON),
    ]
    sc_w, sc_h = Inches(2.7), Inches(1.55)
    for i, (ct, cd, cc) in enumerate(criteria_data):
        left_pos = Inches(0.8 + i * (2.7 + 0.3))
        add_card(s4, left_pos, Inches(1.8), sc_w, sc_h, bg_color=SURFACE_CARD,
                 border_color=BORDER_SUBTLE)
        add_textbox(s4, left_pos + Inches(0.2), Inches(1.95), sc_w - Inches(0.4),
                    Inches(0.35), ct, 12, bold=True, color=cc)
        add_textbox(s4, left_pos + Inches(0.2), Inches(2.35), sc_w - Inches(0.4),
                    Inches(0.9), cd, MIN_BODY_PT, color=TEXT_HIGH)

    add_card(s4, Inches(0.8), Inches(3.6), Inches(11.733), Inches(3.3),
             bg_color=SURFACE_CARD, border_color=BORDER_CYAN, border_width=1.6)
    tb_b = s4.shapes.add_textbox(Inches(1.2), Inches(3.85), Inches(10.9), Inches(2.8))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    tf_b.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    pb1 = tf_b.paragraphs[0]
    pb1.text = "OFFICIAL HANDOUT MANDATE: 'WITH MORE TIME WE'D ADD...'"
    pb1.font.name = FONT_NAME
    pb1.font.size = Pt(12)
    pb1.font.bold = True
    pb1.font.color.rgb = CYAN_NEON
    pb2 = tf_b.add_paragraph()
    pb2.text = (
        "\"With more time, we\u2019d add live Canvas and syllabus LMS integration, automatically "
        "syncing weekly exam dates and generating proactive 15-minute micro-sprints before every "
        "morning class.\n\nWe don't just help students pass exams; we eliminate academic paralysis "
        "and unlock confidence.\""
    )
    pb2.font.name = FONT_NAME
    pb2.font.size = Pt(13.5)
    pb2.font.italic = True
    pb2.font.color.rgb = TEXT_WHITE
    pb3 = tf_b.add_paragraph()
    pb3.text = "WE ARE PRISMATIC \u2014 REFRACTING COMPLEX KNOWLEDGE INTO YOUR NATIVE SPECTRUM. VOTE PRISMATIC!"
    pb3.font.name = FONT_NAME
    pb3.font.size = Pt(13)
    pb3.font.bold = True
    pb3.font.color.rgb = EMERALD_NEON

    add_footer(s4, 4)
    s4.notes_slide.notes_text_frame.text = (
        "OFFICIAL TIMED SCRIPT (1:45 - 2:00):\n\n"
        "[1:45 - 2:00] SEGMENT 5: THE CLOSE (15s)\n"
        "\"With more time, we\u2019d add live Canvas and syllabus LMS integration, automatically syncing weekly exam dates and generating proactive 15-minute micro-sprints before every morning class.\n"
        "We are PRISMATIC\u2014refracting complex knowledge into your native spectrum.\n"
        "Vote Prismatic for your room champion! Thank you!\""
    )

    output_pptx.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_pptx))
    print(f"[+] PPTX: {output_pptx} ({output_pptx.stat().st_size / 1024:.1f} KB)")
    return output_pptx


# ------------------------------------------------------- PDF / PNG export ---
def _export_via_powerpoint(pptx_path, pdf_path, slides_dir, export_images):
    """Windows + PowerPoint installed path. Returns True on success."""
    try:
        import win32com.client
    except ImportError:
        return False
    powerpoint = None
    deck = None
    try:
        print("[*] Exporting via PowerPoint COM...")
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        deck = powerpoint.Presentations.Open(str(pptx_path.resolve()), WithWindow=False)
        if pdf_path is not None:
            deck.SaveAs(str(pdf_path.resolve()), 32)  # ppSaveAsPDF
            print(f"[+] PDF: {pdf_path}")
        if export_images:
            slides_dir.mkdir(parents=True, exist_ok=True)
            for i in range(1, deck.Slides.Count + 1):
                img_path = slides_dir / f"slide_{i}.png"
                deck.Slides(i).Export(str(img_path.resolve()), "PNG", 1920, 1080)
                print(f"[+] Slide image: {img_path}")
        return True
    except Exception as exc:
        print(f"[!] PowerPoint COM export failed: {exc}", file=sys.stderr)
        return False
    finally:
        try:
            if deck is not None:
                deck.Close()
        except Exception:
            pass
        try:
            if powerpoint is not None:
                powerpoint.Quit()
        except Exception:
            pass


def _export_via_libreoffice(pptx_path, pdf_path):
    """Cross-platform fallback: soffice --headless --convert-to pdf."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice or pdf_path is None:
        return False
    try:
        print("[*] Exporting via LibreOffice headless...")
        subprocess.run(
            [soffice, "--headless", "--convert-to", "pdf",
             "--outdir", str(pdf_path.parent.resolve()), str(pptx_path.resolve())],
            check=True, capture_output=True, text=True, timeout=180,
        )
        produced = pdf_path.parent / (pptx_path.stem + ".pdf")
        if produced.resolve() != pdf_path.resolve() and produced.exists():
            produced.replace(pdf_path)
        print(f"[+] PDF: {pdf_path}")
        return True
    except Exception as exc:
        print(f"[!] LibreOffice export failed: {exc}", file=sys.stderr)
        return False


def export_to_pdf_and_images(pptx_path=None, pdf_path=None,
                             slides_dir=None, export_images=True):
    pptx_path = Path(pptx_path) if pptx_path is not None else OUTPUT_PPTX
    pdf_path = Path(pdf_path) if pdf_path is not None else OUTPUT_PDF
    slides_dir = Path(slides_dir) if slides_dir else (ASSETS_DIR / "slides")
    if not pptx_path.exists():
        print(f"[!] PPTX not found: {pptx_path}", file=sys.stderr)
        return False
    ok = False
    if pdf_path is not None or export_images:
        ok = _export_via_powerpoint(pptx_path, pdf_path, slides_dir, export_images)
    if pdf_path is not None and (not ok or not pdf_path.exists()):
        ok = _export_via_libreoffice(pptx_path, pdf_path) or ok
    if pdf_path is not None and not pdf_path.exists():
        print("[!] PDF was not produced (no PowerPoint / LibreOffice available). "
              "PPTX is still valid; use --skip-pdf on machines without Office.",
              file=sys.stderr)
    return ok


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="Build Prismatic pitch deck")
    ap.add_argument("--pptx", default=str(OUTPUT_PPTX), help="Output PPTX path")
    ap.add_argument("--pdf", default=str(OUTPUT_PDF), help="Output PDF path")
    ap.add_argument("--skip-pdf", action="store_true", help="Skip PDF export")
    ap.add_argument("--skip-images", action="store_true", help="Skip slide PNG export")
    return ap.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    pptx_path = Path(args.pptx)
    pdf_path = None if args.skip_pdf else Path(args.pdf)
    build_prismatic_masterpiece(pptx_path)
    if pdf_path is None and args.skip_images:
        return 0
    ok = export_to_pdf_and_images(pptx_path, pdf_path,
                                  export_images=not args.skip_images)
    if pdf_path is not None and not pdf_path.exists():
        print("[!] Continuing with PPTX only (PDF unavailable).", file=sys.stderr)
    return 0 if ok or pdf_path is None or pdf_path.exists() else 1


if __name__ == "__main__":
    raise SystemExit(main())
