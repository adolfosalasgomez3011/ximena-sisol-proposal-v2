"""
Propuesta CEMIS V2 — Con ilustraciones generadas por Gemini IA
==============================================================
Extends generate_proposal_pdf.py (V1) adding four AI-generated visuals:
  - cover_hero.png        → cover page (hero illustration)
  - science_gutbrain.png  → Section 3 Marco Científico
  - three_pillars.png     → Section 4 Los Tres Pilares
  - implementation_path.png → Section 9 Plan de Implementación

V1 PDF is NOT modified. This script writes:
  output/PropuestaCEMIS_DraXimenaChirinos_V2.pdf
"""

import os
import sys

# Allow importing V1 module from the same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ── Import all V1 helpers, constants and builders ──────────────────────────────
from generate_proposal_pdf import (
    build_styles, DocCanvas, section_banner, info_box, two_col_cards,
    data_table,
    build_toc, build_executive_summary, build_context,
    build_science      as _build_science_v1,
    build_pillars      as _build_pillars_v1,
    build_model, build_objectives, build_naming, build_bio,
    build_implementation as _build_implementation_v1,
    build_investment, build_evidence, build_next_steps,
    # layout constants
    TEAL, TEAL_LIGHT, PEACH, PEACH_LIGHT, DARK, GREEN, GREEN_LIGHT,
    GRAY_BG, GRAY_MID, GRAY_TEXT, GRAY_LIGHT, WHITE, BLACK,
    PAGE_W, PAGE_H, MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B, CONTENT_W,
)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether, Image as RLImage,
)
from reportlab.lib.colors import HexColor
from datetime import date

# ── V2 paths ───────────────────────────────────────────────────────────────────
_BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR  = os.path.join(_BASE, "assets")
OUTPUT_PATH = os.path.join(_BASE, "output",
                           "PropuestaCEMIS_DraXimenaChirinos_V2.pdf")


# ── Image helper ───────────────────────────────────────────────────────────────
def _centered_image(filename, w, h):
    """Return a full-content-width Table that centres the image."""
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        print(f"  [WARN] Image not found, skipping: {path}")
        return Spacer(1, 0.1)
    img = RLImage(path, width=w, height=h)
    t = Table([[img]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t


# ── COVER PAGE (V2 — with hero image) ─────────────────────────────────────────
def build_cover(styles):
    """Cover page with the AI-generated hero illustration."""
    story = []
    story.append(Spacer(1, 1.5 * cm))

    # Institution header
    story.append(Paragraph(
        "HOSPITAL DE LA SOLIDARIDAD · SISOL · LIMA, PERÚ",
        styles['cover_institution']
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(HRFlowable(
        width=CONTENT_W, thickness=2, color=TEAL, spaceAfter=0.4 * cm
    ))

    # Main title
    story.append(Paragraph(
        "Propuesta de Implementación<br/>del Departamento de<br/>Medicina Integrativa",
        styles['cover_title']
    ))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph(
        "CEMIS — Centro de Medicina Integrativa Solidaria",
        styles['cover_subtitle']
    ))
    story.append(Spacer(1, 0.45 * cm))

    # ── AI HERO IMAGE ──────────────────────────────────────────────────────────
    story.append(_centered_image("cover_hero.png", 9 * cm, 6.0 * cm))
    story.append(Spacer(1, 0.35 * cm))
    # ──────────────────────────────────────────────────────────────────────────

    story.append(HRFlowable(
        width=6 * cm, thickness=3, color=PEACH,
        hAlign='CENTER', spaceAfter=0.5 * cm
    ))

    # Summary box
    summary_t = Table(
        [[Paragraph(
            "Este documento propone la creación del primer departamento de Medicina "
            "Integrativa en el sistema SISOL, bajo la dirección de la Dra. Ximena "
            "Chirinos Orbegozo. El modelo articula la biología del conflicto "
            "(Germanische Heilkunde), las terapias sistémicas familiares y la "
            "medicina funcional como complemento al tratamiento alopático "
            "convencional, con el objetivo de mejorar los outcomes clínicos en "
            "pacientes con enfermedades crónicas.",
            styles['body']
        )]],
        colWidths=[CONTENT_W - 4 * cm]
    )
    summary_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), TEAL_LIGHT),
        ('LEFTPADDING',   (0, 0), (-1, -1), 18),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 18),
        ('TOPPADDING',    (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('LINEBEFORE',    (0, 0), (0,  -1), 4, TEAL),
        ('LINEAFTER',     (0, 0), (-1, -1), 4, TEAL),
    ]))
    story.append(summary_t)
    story.append(Spacer(1, 0.5 * cm))

    # Author / date block
    story.append(HRFlowable(
        width=CONTENT_W, thickness=0.5,
        color=HexColor('#DDDDDD'), spaceAfter=0.4 * cm
    ))
    story.append(Paragraph(
        "<b>Dra. Ximena Chirinos Orbegozo</b> &nbsp; · &nbsp; CMP 36103",
        styles['cover_author']
    ))
    story.append(Paragraph(
        "Médico Integrativa · Especialista en Nueva Medicina Germánica, "
        "Constelaciones Familiares y Medicina Funcional",
        styles['cover_author']
    ))
    story.append(Paragraph("Clínica Magga · La Molina, Lima", styles['cover_author']))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        f"Lima, Perú · {date.today().strftime('%B %Y')}",
        styles['cover_date']
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "DOCUMENTO CONFIDENCIAL — USO EXCLUSIVO SISOL",
        ParagraphStyle(
            'conf_v2', fontSize=8, textColor=PEACH,
            fontName='Helvetica-Bold', alignment=TA_CENTER, letterSpacing=1
        )
    ))
    story.append(PageBreak())
    return story


# ── SECTION 3 — SCIENCE  (V2 — with gut-brain illustration) ───────────────────
def build_science(styles):
    """Section 3 with AI gut-brain axis illustration inserted after the banner."""
    story = _build_science_v1(styles)
    # section_banner() adds 3 items: [Spacer, Table, Spacer] → indices 0, 1, 2
    # Intro paragraph is at index 3.
    # We insert: image at [3], spacer at [4], pushing intro to [5].
    img  = _centered_image("science_gutbrain.png", CONTENT_W, CONTENT_W * 0.42)
    story.insert(3, Spacer(1, 6))   # spacer after image
    story.insert(3, img)            # image right after banner
    return story


# ── SECTION 4 — PILLARS  (V2 — with triptych illustration) ────────────────────
def build_pillars(styles):
    """Section 4 with AI three-pillars illustration inserted after the intro para."""
    story = _build_pillars_v1(styles)
    # Banner = [0,1,2], intro paragraph = [3], Pilar 1 starts at [4].
    # We want: banner, intro_para, image, spacer, Pilar1 → insert at position 4.
    img  = _centered_image("three_pillars.png", CONTENT_W, CONTENT_W * 0.38)
    story.insert(4, Spacer(1, 6))   # spacer after image  (now at [5])
    story.insert(4, img)            # image at [4], spacer shifts to [5]
    return story


# ── SECTION 9 — IMPLEMENTATION  (V2 — with pathway illustration) ──────────────
def build_implementation(styles):
    """Section 9 with AI implementation-pathway illustration appended at the end."""
    story = _build_implementation_v1(styles)
    img  = _centered_image("implementation_path.png", CONTENT_W, CONTENT_W * 0.38)
    story.append(Spacer(1, 10))
    story.append(img)
    story.append(Spacer(1, 4))
    return story


# ── MAIN BUILD ─────────────────────────────────────────────────────────────────
def build_pdf():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    canvas_obj = DocCanvas("Propuesta CEMIS V2 — Medicina Integrativa SISOL")

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T + 0.8 * cm,
        bottomMargin=MARGIN_B + 0.8 * cm,
        title="Propuesta CEMIS V2 — Departamento de Medicina Integrativa SISOL",
        author="Dra. Ximena Chirinos Orbegozo CMP 36103",
        subject="Propuesta de implementación del Centro de Medicina Integrativa Solidaria",
        creator="CEMIS Proposal Generator v2.0",
    )

    styles = build_styles()

    story = []
    story += build_cover(styles)
    story += build_toc(styles)
    story += build_executive_summary(styles)
    story.append(PageBreak())
    story += build_context(styles)
    story.append(PageBreak())
    story += build_science(styles)      # ← with gut-brain image
    story.append(PageBreak())
    story += build_pillars(styles)      # ← with three-pillars image
    story.append(PageBreak())
    story += build_model(styles)
    story.append(PageBreak())
    story += build_objectives(styles)
    story.append(PageBreak())
    story += build_naming(styles)
    story += build_bio(styles)
    story.append(PageBreak())
    story += build_implementation(styles)  # ← with pathway image
    story.append(PageBreak())
    story += build_investment(styles)
    story.append(PageBreak())
    story += build_evidence(styles)
    story.append(PageBreak())
    story += build_next_steps(styles)

    doc.build(
        story,
        onFirstPage=canvas_obj.on_page,
        onLaterPages=canvas_obj.on_page,
    )

    print(f"\n✓ PDF V2 generated: {OUTPUT_PATH}")
    print(f"  Size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")


if __name__ == "__main__":
    build_pdf()
