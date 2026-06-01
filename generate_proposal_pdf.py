"""
Propuesta Formal — Departamento de Medicina Integrativa SISOL
Dra. Ximena Chirinos Orbegozo · CMP 36103
PDF Generator — ReportLab Platypus
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.platypus.flowables import BalancedColumns
from reportlab.lib.colors import HexColor
import os
from datetime import date

# ──────────────────────────────────────────────
# BRAND COLORS
# ──────────────────────────────────────────────
TEAL       = HexColor('#1A6B6B')
TEAL_LIGHT = HexColor('#E8F5F5')
PEACH      = HexColor('#E8906A')
PEACH_LIGHT= HexColor('#FDF0EB')
DARK       = HexColor('#1A3A3A')
GREEN      = HexColor('#4A8A4A')
GREEN_LIGHT= HexColor('#F0F8F0')
GRAY_BG    = HexColor('#FAFAF8')
GRAY_MID   = HexColor('#F0EDE8')
GRAY_TEXT  = HexColor('#555555')
GRAY_LIGHT = HexColor('#AAAAAA')
WHITE      = colors.white
BLACK      = colors.black

PAGE_W, PAGE_H = A4
MARGIN_L = 2.2 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.5 * cm
MARGIN_B = 2.2 * cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "output",
    "PropuestaCEMIS_DraXimenaChirinos_V1.pdf"
)

# ──────────────────────────────────────────────
# STYLES
# ──────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        'cover_institution': ParagraphStyle(
            'cover_institution', fontSize=8, textColor=TEAL,
            fontName='Helvetica-Bold', letterSpacing=2,
            alignment=TA_CENTER, spaceAfter=4
        ),
        'cover_title': ParagraphStyle(
            'cover_title', fontSize=28, textColor=DARK,
            fontName='Helvetica-Bold', leading=34,
            alignment=TA_CENTER, spaceAfter=8
        ),
        'cover_subtitle': ParagraphStyle(
            'cover_subtitle', fontSize=14, textColor=GRAY_TEXT,
            fontName='Helvetica', leading=20,
            alignment=TA_CENTER, spaceAfter=6
        ),
        'cover_author': ParagraphStyle(
            'cover_author', fontSize=10, textColor=GRAY_TEXT,
            fontName='Helvetica', leading=16,
            alignment=TA_CENTER, spaceAfter=4
        ),
        'cover_date': ParagraphStyle(
            'cover_date', fontSize=9, textColor=GRAY_LIGHT,
            fontName='Helvetica', alignment=TA_CENTER
        ),
        'section_title': ParagraphStyle(
            'section_title', fontSize=16, textColor=WHITE,
            fontName='Helvetica-Bold', leading=22,
            alignment=TA_LEFT, spaceAfter=0, spaceBefore=0
        ),
        'h1': ParagraphStyle(
            'h1', fontSize=13, textColor=TEAL,
            fontName='Helvetica-Bold', leading=18,
            spaceBefore=14, spaceAfter=6,
            borderPadding=(0, 0, 4, 0)
        ),
        'h2': ParagraphStyle(
            'h2', fontSize=11, textColor=DARK,
            fontName='Helvetica-Bold', leading=16,
            spaceBefore=10, spaceAfter=4
        ),
        'h3_teal': ParagraphStyle(
            'h3_teal', fontSize=10, textColor=TEAL,
            fontName='Helvetica-Bold', leading=14,
            spaceBefore=6, spaceAfter=3
        ),
        'h3_orange': ParagraphStyle(
            'h3_orange', fontSize=10, textColor=HexColor('#C06030'),
            fontName='Helvetica-Bold', leading=14,
            spaceBefore=6, spaceAfter=3
        ),
        'h3_green': ParagraphStyle(
            'h3_green', fontSize=10, textColor=GREEN,
            fontName='Helvetica-Bold', leading=14,
            spaceBefore=6, spaceAfter=3
        ),
        'body': ParagraphStyle(
            'body', fontSize=9.5, textColor=HexColor('#333333'),
            fontName='Helvetica', leading=15, alignment=TA_JUSTIFY,
            spaceBefore=3, spaceAfter=4
        ),
        'body_small': ParagraphStyle(
            'body_small', fontSize=8.5, textColor=HexColor('#444444'),
            fontName='Helvetica', leading=13, alignment=TA_JUSTIFY,
            spaceBefore=2, spaceAfter=2
        ),
        'bullet': ParagraphStyle(
            'bullet', fontSize=9.5, textColor=HexColor('#333333'),
            fontName='Helvetica', leading=15,
            leftIndent=14, firstLineIndent=-10,
            spaceBefore=2, spaceAfter=2
        ),
        'bullet_small': ParagraphStyle(
            'bullet_small', fontSize=8.5, textColor=HexColor('#444444'),
            fontName='Helvetica', leading=13,
            leftIndent=14, firstLineIndent=-10,
            spaceBefore=1, spaceAfter=1
        ),
        'quote': ParagraphStyle(
            'quote', fontSize=10, textColor=DARK,
            fontName='Helvetica-Oblique', leading=16,
            leftIndent=16, rightIndent=16,
            spaceBefore=8, spaceAfter=8
        ),
        'callout': ParagraphStyle(
            'callout', fontSize=9.5, textColor=DARK,
            fontName='Helvetica-Bold', leading=15,
            alignment=TA_CENTER,
            spaceBefore=6, spaceAfter=6
        ),
        'table_header': ParagraphStyle(
            'table_header', fontSize=9, textColor=WHITE,
            fontName='Helvetica-Bold', leading=13,
            alignment=TA_LEFT
        ),
        'table_cell': ParagraphStyle(
            'table_cell', fontSize=9, textColor=HexColor('#333333'),
            fontName='Helvetica', leading=13, alignment=TA_LEFT
        ),
        'table_cell_bold': ParagraphStyle(
            'table_cell_bold', fontSize=9, textColor=DARK,
            fontName='Helvetica-Bold', leading=13, alignment=TA_LEFT
        ),
        'footer': ParagraphStyle(
            'footer', fontSize=7.5, textColor=GRAY_LIGHT,
            fontName='Helvetica', alignment=TA_CENTER
        ),
        'label_teal': ParagraphStyle(
            'label_teal', fontSize=8, textColor=TEAL,
            fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER
        ),
        'label_orange': ParagraphStyle(
            'label_orange', fontSize=8, textColor=HexColor('#C06030'),
            fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER
        ),
        'label_green': ParagraphStyle(
            'label_green', fontSize=8, textColor=GREEN,
            fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER
        ),
    }
    return styles


# ──────────────────────────────────────────────
# HEADER / FOOTER CANVAS
# ──────────────────────────────────────────────
class DocCanvas:
    def __init__(self, doc_title="Propuesta CEMIS"):
        self.title = doc_title

    def on_page(self, canvas, doc):
        canvas.saveState()
        # Top teal bar (only on non-cover pages)
        if doc.page > 1:
            canvas.setFillColor(TEAL)
            canvas.rect(0, PAGE_H - 1*cm, PAGE_W, 1*cm, fill=1, stroke=0)
            canvas.setFillColor(WHITE)
            canvas.setFont('Helvetica', 7)
            canvas.drawString(MARGIN_L, PAGE_H - 0.62*cm,
                              "HOSPITAL DE LA SOLIDARIDAD · SISOL")
            canvas.setFont('Helvetica', 7)
            canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 0.62*cm,
                                   self.title)

        # Bottom footer
        canvas.setFillColor(GRAY_LIGHT)
        canvas.setFont('Helvetica', 7)
        footer_text = (
            "Propuesta Confidencial  ·  Dra. Ximena Chirinos Orbegozo CMP 36103  "
            "·  clinicamagga.com  ·  Lima, Perú"
        )
        canvas.drawCentredString(PAGE_W / 2, 1.1*cm, footer_text)
        # Page number
        canvas.drawRightString(PAGE_W - MARGIN_R, 1.1*cm,
                               f"Página {doc.page}")
        # Bottom line
        canvas.setStrokeColor(HexColor('#DDDDDD'))
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_L, 1.55*cm, PAGE_W - MARGIN_R, 1.55*cm)
        canvas.restoreState()


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
def section_banner(styles, text, color=TEAL):
    """Full-width colored banner for section headings."""
    t = Table(
        [[Paragraph(text, styles['section_title'])]],
        colWidths=[CONTENT_W]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    return [Spacer(1, 8), t, Spacer(1, 10)]


def info_box(styles, paragraphs, bg=TEAL_LIGHT, left_bar=TEAL):
    """Highlighted info box with left colored bar."""
    inner = Table(
        [[p] for p in paragraphs],
        colWidths=[CONTENT_W - 1.2*cm]
    )
    inner.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    outer = Table(
        [[inner]],
        colWidths=[CONTENT_W]
    )
    outer.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LINEBEFORETABLE', (0, 0), (0, 0), 3, left_bar),
        ('LINEBEFORE', (0, 0), (0, -1), 3, left_bar),
        ('ROUNDEDCORNERS', [0, 4, 4, 0]),
    ]))
    return [outer, Spacer(1, 8)]


def two_col_cards(styles, items, bg=GRAY_BG, header_color=TEAL):
    """Render a list of (title, bullets) pairs as a 2-col card grid."""
    cells = []
    row = []
    for i, (title, bullets) in enumerate(items):
        content = [Paragraph(title, styles['h3_teal'
                    if header_color == TEAL else (
                    'h3_orange' if header_color == PEACH else 'h3_green')])]
        for b in bullets:
            content.append(Paragraph(f"\u2022  {b}", styles['bullet_small']))
        card = Table(
            [[c] for c in content],
            colWidths=[(CONTENT_W / 2) - 0.5*cm]
        )
        card.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (0, 0), 8),
            ('BOTTOMPADDING', (0, -1), (0, -1), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -2), 2),
            ('LINEBEFORE', (0, 0), (0, -1), 2.5, header_color),
            ('ROUNDEDCORNERS', [0, 4, 4, 0]),
        ]))
        row.append(card)
        if len(row) == 2:
            cells.append(row)
            row = []
    if row:
        row.append(Spacer(1, 1))
        cells.append(row)

    col_w = (CONTENT_W / 2) - 0.4*cm
    grid = Table(cells, colWidths=[col_w + 0.5*cm, col_w + 0.5*cm],
                 hAlign='LEFT')
    grid.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return [grid, Spacer(1, 6)]


def data_table(styles, headers, rows, col_widths, accent=TEAL):
    """Render a formatted data table."""
    header_row = [Paragraph(h, styles['table_header']) for h in headers]
    table_data = [header_row]
    for row in rows:
        table_data.append([
            Paragraph(str(c), styles['table_cell_bold'] if i == 0
                      else styles['table_cell'])
            for i, c in enumerate(row)
        ])
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), accent),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor('#F5F5F3')]),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return [t, Spacer(1, 8)]


# ──────────────────────────────────────────────
# COVER PAGE
# ──────────────────────────────────────────────
def build_cover(styles):
    story = []
    story.append(Spacer(1, 2.5*cm))

    # Institution line
    story.append(Paragraph(
        "HOSPITAL DE LA SOLIDARIDAD · SISOL · LIMA, PERÚ",
        styles['cover_institution']
    ))
    story.append(Spacer(1, 0.4*cm))

    # Teal rule
    story.append(HRFlowable(width=CONTENT_W, thickness=2, color=TEAL,
                             spaceAfter=0.6*cm))

    # Title
    story.append(Paragraph(
        "Propuesta de Implementación<br/>del Departamento de<br/>Medicina Integrativa",
        styles['cover_title']
    ))
    story.append(Spacer(1, 0.3*cm))

    # Subtitle
    story.append(Paragraph(
        "CEMIS — Centro de Medicina Integrativa Solidaria",
        styles['cover_subtitle']
    ))
    story.append(Spacer(1, 0.8*cm))

    # Teal accent rule
    story.append(HRFlowable(width=6*cm, thickness=3, color=PEACH,
                             hAlign='CENTER', spaceAfter=0.8*cm))

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
        colWidths=[CONTENT_W - 4*cm]
    )
    summary_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TEAL_LIGHT),
        ('LEFTPADDING', (0, 0), (-1, -1), 18),
        ('RIGHTPADDING', (0, 0), (-1, -1), 18),
        ('TOPPADDING', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LINEBEFORE', (0, 0), (0, -1), 4, TEAL),
        ('LINEAFTER', (0, 0), (-1, -1), 4, TEAL),
    ]))
    story.append(summary_t)
    story.append(Spacer(1, 0.8*cm))

    # Author / date block
    story.append(HRFlowable(width=CONTENT_W, thickness=0.5,
                             color=HexColor('#DDDDDD'), spaceAfter=0.4*cm))
    story.append(Paragraph(
        "<b>Dra. Ximena Chirinos Orbegozo</b> &nbsp; · &nbsp; CMP 36103",
        styles['cover_author']
    ))
    story.append(Paragraph(
        "Médico Integrativa · Especialista en Nueva Medicina Germánica, "
        "Constelaciones Familiares y Medicina Funcional",
        styles['cover_author']
    ))
    story.append(Paragraph(
        "Clínica Magga · La Molina, Lima",
        styles['cover_author']
    ))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        f"Lima, Perú · {date.today().strftime('%B %Y')}",
        styles['cover_date']
    ))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "DOCUMENTO CONFIDENCIAL — USO EXCLUSIVO SISOL",
        ParagraphStyle('conf', fontSize=8, textColor=PEACH,
                       fontName='Helvetica-Bold', alignment=TA_CENTER,
                       letterSpacing=1)
    ))
    story.append(PageBreak())
    return story


# ──────────────────────────────────────────────
# SECTION 1 — EXECUTIVE SUMMARY
# ──────────────────────────────────────────────
def build_executive_summary(styles):
    story = []
    story += section_banner(styles, "1.  Resumen Ejecutivo")

    story.append(Paragraph(
        "El sistema de salud pública peruano enfrenta una paradoja estructural: "
        "disponemos de la infraestructura para atender el evento agudo —el infarto, "
        "el trauma, la fractura— con estándares comparables a los de cualquier país "
        "desarrollado. Sin embargo, más del <b>80% de la carga asistencial</b> recae "
        "sobre condiciones crónicas cuyo manejo exclusivamente farmacológico resulta, "
        "con frecuencia, insuficiente para modificar el curso natural de la enfermedad.",
        styles['body']
    ))
    story.append(Paragraph(
        "La presente propuesta plantea la creación del <b>Centro de Medicina Integrativa "
        "Solidaria (CEMIS)</b> en el Hospital de la Solidaridad, dentro de la estructura "
        "orgánica del Sistema Metropolitano de la Solidaridad (SISOL). El CEMIS no "
        "sustituye ninguna especialidad existente; actúa como un puente clínico que "
        "complementa el tratamiento convencional mediante tres pilares terapéuticos "
        "con sustento científico: la biología del conflicto (Germanische Heilkunde), "
        "las terapias sistémicas familiares y la medicina funcional.",
        styles['body']
    ))

    key_points = [
        ("<b>Modelo complementario:</b> El CEMIS opera en coordinación directa con cada "
         "especialista derivador, generando un ciclo de retroalimentación bidireccional "
         "que enriquece el diagnóstico y el seguimiento clínico."),
        ("<b>Objetivos medibles:</b> Reducción del tiempo de enfermedad, disminución de "
         "la carga medicamentosa, menor tasa de rehospitalizaciones y mejora objetiva "
         "de la calidad de vida del paciente."),
        ("<b>Escalabilidad:</b> El modelo piloto —diseñado para el Hospital de la "
         "Solidaridad— es replicable en cualquier sede SISOL, multiplicando el impacto "
         "sobre los 120 millones de consultas acumuladas en el sistema."),
        ("<b>Evidencia internacional:</b> Brasil (PNPIC, 2006), la OMS (Estrategia de "
         "Medicina Tradicional y Complementaria 2019–2025), Cleveland Clinic, Johns "
         "Hopkins y Mayo Clinic cuentan con departamentos equivalentes integrados en "
         "su estructura institucional."),
        ("<b>Viabilidad financiera:</b> La proyección a capacidad operativa plena "
         "(15 pacientes/día) genera S/ 36,000/mes en facturación, alcanzando el "
         "punto de equilibrio operativo con 8–9 atenciones diarias."),
    ]
    for kp in key_points:
        story.append(Paragraph(f"\u25B8  {kp}", styles['bullet']))
    story.append(Spacer(1, 6))

    story += info_box(styles, [
        Paragraph(
            '"SISOL transformó la visión de un médico cirujano en 54 hospitales y '
            '120 millones de consultas. El CEMIS es la siguiente transformación: '
            'llevar medicina que sana desde la raíz a quienes más lo necesitan."',
            styles['quote']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)

    return story


# ──────────────────────────────────────────────
# SECTION 2 — EPIDEMIOLOGICAL CONTEXT
# ──────────────────────────────────────────────
def build_context(styles):
    story = []
    story += section_banner(styles, "2.  Contexto Epidemiológico y Necesidad Institucional")

    story.append(Paragraph("2.1  La Brecha en Salud Mental del Perú", styles['h1']))
    story.append(Paragraph(
        "El Perú presenta una de las brechas más amplias de América Latina entre la "
        "necesidad poblacional de atención en salud mental y la oferta asistencial "
        "disponible. Los datos del Ministerio de Salud y la Organización Panamericana "
        "de la Salud son elocuentes:",
        styles['body']
    ))

    stats_headers = ["Indicador", "Dato"]
    stats_rows = [
        ["Centros de Salud Mental Comunitarios faltantes a nivel nacional", "384"],
        ["Déficit solo en Lima Metropolitana", "141"],
        ["Peruanos con trastorno mental sin acceso a atención", "> 70%"],
        ["Nuevas sedes SISOL con psiquiatría (2025–2026)",
         "El Agustino · La Victoria · Camaná · Wanchaq"],
        ["Consultas acumuladas SISOL (histórico)", "120 millones"],
    ]
    story += data_table(styles, stats_headers, stats_rows,
                        [CONTENT_W * 0.72, CONTENT_W * 0.28])

    story.append(Paragraph(
        "SISOL ya ha reconocido esta necesidad y está respondiendo: la expansión de "
        "la psiquiatría en cuatro nuevas sedes durante el bienio 2025–2026 es una "
        "señal institucional inequívoca. El CEMIS se inscribe en esa misma dirección, "
        "ampliando la respuesta al componente psiconeurobiológico que la psiquiatría "
        "convencional no alcanza a cubrir en su totalidad.",
        styles['body']
    ))

    story.append(Paragraph("2.2  La Limitación Estructural del Modelo Biomédico Clásico",
                            styles['h1']))
    story.append(Paragraph(
        "El sistema médico moderno es extraordinariamente eficaz para la fase aguda "
        "de la enfermedad. El infarto se estabiliza, el tumor se reseca, la fractura "
        "se fija. No obstante, cuando el mismo paciente regresa —semanas, meses o "
        "años después— con la misma entidad nosológica o con comorbilidades nuevas, "
        "el modelo de una sola consulta, un diagnóstico y una prescripción se revela "
        "insuficiente.",
        styles['body']
    ))

    row2 = [
        [
            Paragraph("La paradoja crónica", styles['h3_teal']),
            Paragraph("La oportunidad integrativa", styles['h3_teal']),
        ],
        [
            Table(
                [[Paragraph(b, styles['bullet_small'])] for b in [
                    "\u2022  La medicación aumenta; la adherencia disminuye.",
                    "\u2022  El órgano recibe tratamiento; la persona, no.",
                    "\u2022  El paciente regresa. Y regresa. Y regresa.",
                    "\u2022  El sistema se fragmenta entre especialidades.",
                ]],
                colWidths=[(CONTENT_W / 2) - 0.8*cm]
            ),
            Table(
                [[Paragraph(b, styles['bullet_small'])] for b in [
                    "\u2022  Identificar el conflicto biológico que originó el síntoma.",
                    "\u2022  Incluir el sistema familiar en el mapa clínico.",
                    "\u2022  Regulación del terreno para potenciar el tratamiento.",
                    "\u2022  Retroalimentación bidireccional con el especialista.",
                ]],
                colWidths=[(CONTENT_W / 2) - 0.8*cm]
            ),
        ]
    ]
    col_w = CONTENT_W / 2
    t = Table(row2, colWidths=[col_w, col_w])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), TEAL_LIGHT),
        ('BACKGROUND', (1, 0), (1, 0), PEACH_LIGHT),
        ('BACKGROUND', (0, 1), (0, 1), WHITE),
        ('BACKGROUND', (1, 1), (1, 1), WHITE),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    story += info_box(styles, [
        Paragraph(
            "Esta no es una crítica al sistema convencional — que es el pilar "
            "indiscutible de SISOL. Es la identificación de una brecha clínica "
            "real, resuelta con éxito en los sistemas de salud más avanzados del "
            "mundo mediante la integración de ambas medicinas.",
            styles['body']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)

    return story


# ──────────────────────────────────────────────
# SECTION 3 — SCIENTIFIC FRAMEWORK
# ──────────────────────────────────────────────
def build_science(styles):
    story = []
    story += section_banner(styles, "3.  Marco Científico y Teórico")
    story.append(Paragraph(
        "El CEMIS se sustenta en disciplinas con creciente respaldo en la literatura "
        "médica indexada. No se trata de medicina alternativa: es ciencia publicada "
        "en revistas de primer nivel (PubMed, The Lancet, NEJM) que ha tardado en "
        "integrarse a la práctica clínica cotidiana por razones históricas y "
        "estructurales, no por falta de evidencia.",
        styles['body']
    ))

    story.append(Paragraph("3.1  Psiconeuroinmunología (PNI)", styles['h1']))
    story.append(Paragraph(
        "La psiconeuroinmunología es la disciplina que estudia la interacción "
        "bidireccional entre el sistema nervioso central, el sistema endocrino y "
        "el sistema inmune. Sus hallazgos fundamentales demuestran que:",
        styles['body']
    ))
    for b in [
        "El estado emocional del paciente modifica directamente la respuesta inmune, "
        "la producción hormonal y la actividad del sistema nervioso autónomo.",
        "El estrés crónico produce supresión inmunológica sostenida, aumentando la "
        "susceptibilidad a infecciones, enfermedades autoinmunes y neoplasias.",
        "La resolución del conflicto emocional se asocia con reactivación medible "
        "de la respuesta inmune en estudios prospectivos controlados.",
    ]:
        story.append(Paragraph(f"\u2022  {b}", styles['bullet']))

    story.append(Paragraph("3.2  El Eje Intestino–Cerebro–Psiquis", styles['h1']))
    story.append(Paragraph(
        "El microbioma intestinal es hoy reconocido como un órgano endocrino de "
        "primer orden. El 90% de la serotonina circulante es producida por las "
        "células enterocromafines del intestino, no por el sistema nervioso central. "
        "La evidencia establece que:",
        styles['body']
    ))
    for b in [
        "La disbiosis intestinal correlaciona con depresión, ansiedad, fatiga crónica "
        "y enfermedades autoinmunes en múltiples estudios longitudinales.",
        "La inflamación sistémica de bajo grado —frecuentemente originada en el "
        "intestino— es un denominador común en la mayoría de las enfermedades crónicas "
        "no transmisibles.",
        "Las intervenciones sobre la microbiota (dieta, probióticos, reducción de "
        "inflamación) producen mejoras clínicas documentadas en patología psiquiátrica "
        "y autoinmune.",
    ]:
        story.append(Paragraph(f"\u2022  {b}", styles['bullet']))

    story.append(Paragraph(
        "3.3  La Germanische Heilkunde (Nueva Medicina Germánica) — Dr. Ryke Geerd Hamer",
        styles['h1']
    ))
    story.append(Paragraph(
        "El Dr. Ryke Geerd Hamer (médico e investigador, Alemania) formuló las "
        "<b>5 Leyes Biológicas</b> a partir del estudio sistemático de más de "
        "20,000 historias clínicas oncológicas y de otras especialidades. "
        "Su hipótesis central sostiene que toda enfermedad orgánica tiene una causa "
        "biológica identificable: un conflicto emocional inesperado, dramático y "
        "vivido en aislamiento (<i>Dirk Hamer Syndrome, DHS</i>) que impacta "
        "primero una región específica del cerebro y, desde ahí, el órgano "
        "correspondiente según el esquema embriológico del tejido.",
        styles['body']
    ))

    hamer_timeline = [
        ["1978", "Su hijo Dirk muere de un disparo en el Mediterráneo. "
         "El Dr. Hamer permanece a su lado hasta el último momento."],
        ["1979", "Le diagnostican cáncer testicular. Jamás había padecido "
         "enfermedad orgánica previa. La coincidencia temporal desencadena "
         "su investigación sistemática."],
        ["1981", "Trabaja como médico en una clínica oncológica y estudia más "
         "de 20,000 casos. Identifica el mismo patrón en todos: conflicto "
         "inesperado → lesión cerebral tomográfica → respuesta orgánica localizada."],
        ["Hallazgo", "Enuncia las 5 Leyes Biológicas de la Germanische Heilkunde. "
         "Denomina el síndrome DHS (Dirk Hamer Syndrome) en honor a su hijo."],
    ]
    t = Table(hamer_timeline, colWidths=[2.2*cm, CONTENT_W - 2.2*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 2), TEAL),
        ('BACKGROUND', (0, 3), (0, 3), PEACH),
        ('TEXTCOLOR', (0, 0), (0, -1), WHITE),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('ROWBACKGROUNDS', (1, 0), (1, -1), [WHITE, HexColor('#F5F5F3')]),
        ('GRID', (0, 0), (-1, -1), 0.3, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "La Dra. Ximena Chirinos Orbegozo es especialista certificada en este "
        "método, lo que la posiciona como la profesional idónea para dirigir el "
        "departamento y garantizar la aplicación rigurosa y éticamente responsable "
        "de esta metodología en el contexto de la salud pública.",
        styles['body']
    ))
    return story


# ──────────────────────────────────────────────
# SECTION 4 — THREE PILLARS
# ──────────────────────────────────────────────
def build_pillars(styles):
    story = []
    story += section_banner(styles, "4.  Los Tres Pilares del Departamento CEMIS")
    story.append(Paragraph(
        "El modelo de atención del CEMIS se estructura sobre tres pilares "
        "complementarios que actúan de forma integrada, tanto en la evaluación "
        "diagnóstica como en el seguimiento terapéutico.",
        styles['body']
    ))

    # Pillar 1
    story.append(Paragraph(
        "Pilar 1 — Biología del Conflicto (Método Hamer / Biodecodificación Clínica)",
        styles['h1']
    ))
    story += info_box(styles, [
        Paragraph(
            "<b>Objetivo clínico:</b> Identificar el conflicto biológico de choque "
            "(DHS) que originó el síntoma orgánico. Comprender la lógica biológica "
            "detrás del síntoma, no solo suprimirlo.",
            styles['body_small']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)

    story += two_col_cards(styles, [
        ("Herramientas diagnósticas", [
            "Anamnesis expandida con identificación del DHS",
            "Biodecodificación clínica del síntoma",
            "Trabajo sobre el 'modo pensar' del paciente",
            "Identificación de la raíz-causa de la enfermedad",
        ]),
        ("Indicaciones principales", [
            "Enfermedades autoinmunes",
            "Patología oncológica (rol complementario)",
            "Dermatología con componente emocional",
            "Neurología funcional",
            "Condiciones crónicas sin respuesta al tratamiento convencional",
        ]),
    ], bg=TEAL_LIGHT, header_color=TEAL)

    # Pillar 2
    story.append(Paragraph(
        "Pilar 2 — Terapias Sistémicas Familiares (Constelaciones / Terapia Sistémica)",
        styles['h1']
    ))
    story += info_box(styles, [
        Paragraph(
            "<b>Objetivo clínico:</b> Ampliar la lectura diagnóstica al sistema "
            "familiar del paciente. Muchas enfermedades crónicas expresan conflictos "
            "no resueltos de generaciones anteriores; el abordaje sistémico permite "
            "intervenir en esa dimensión.",
            styles['body_small']
        )
    ], bg=PEACH_LIGHT, left_bar=PEACH)

    story += two_col_cards(styles, [
        ("Herramientas terapéuticas", [
            "Constelaciones familiares individuales y grupales",
            "Lectura del árbol genealógico como mapa de salud",
            "Terapia sistémica breve (individual)",
            "Trabajo con patrones de lealtad familiar",
        ]),
        ("Fundamento clínico", [
            "La enfermedad mejora cuando el sistema familiar mejora.",
            "Tratar solo al individuo sin entender su sistema es como "
            "apagar la alarma sin apagar el fuego.",
            "Indicado especialmente en cuadros crónico-recurrentes sin "
            "causa orgánica objetivable.",
        ]),
    ], bg=PEACH_LIGHT, header_color=PEACH)

    # Pillar 3
    story.append(Paragraph(
        "Pilar 3 — Medicina Funcional y Regulación del Terreno",
        styles['h1']
    ))
    story += info_box(styles, [
        Paragraph(
            "<b>Objetivo clínico:</b> Optimizar el terreno biológico del paciente "
            "para que las intervenciones de los pilares anteriores —y el tratamiento "
            "alopático del especialista— alcancen su máxima eficacia terapéutica.",
            styles['body_small']
        )
    ], bg=GREEN_LIGHT, left_bar=GREEN)

    story += two_col_cards(styles, [
        ("Herramientas de intervención", [
            "Dieta antiinflamatoria personalizada",
            "Protocolo de regulación de microbiota intestinal",
            "Abordaje del eje intestino–cerebro–psiquis",
            "Reflexología podal",
            "Acupuntura (como complemento)",
        ]),
        ("Principio rector", [
            "No es posible resolver un conflicto emocional en un cuerpo inflamado.",
            "El terreno biológico determina si la enfermedad florece o se resuelve.",
            "La medicina funcional prepara el cuerpo para sanar — y optimiza "
            "la respuesta al tratamiento convencional.",
        ]),
    ], bg=GREEN_LIGHT, header_color=GREEN)

    return story


# ──────────────────────────────────────────────
# SECTION 5 — MODEL & PATHWAY
# ──────────────────────────────────────────────
def build_model(styles):
    story = []
    story += section_banner(styles, "5.  Modelo de Atención — Flujo Clínico Integrado")
    story.append(Paragraph(
        "El CEMIS opera como un nodo complementario dentro de la red asistencial "
        "de SISOL. No compite con ninguna especialidad: <b>dialoga con cada médico "
        "que trata al mismo paciente</b>. El flujo de atención está diseñado para "
        "generar valor en ambas direcciones:",
        styles['body']
    ))

    pathway = [
        ["1", "Consulta médica convencional",
         "El especialista establece diagnóstico y tratamiento. "
         "Identifica candidatos a derivación (paciente crónico, polimedicado, "
         "baja adherencia, recidiva frecuente)."],
        ["2", "Derivación al CEMIS",
         "Criterios clínicos definidos en el protocolo interservicio. "
         "La derivación es voluntaria para el paciente y opcional para el médico."],
        ["3", "Evaluación Integrativa (90–120 min)",
         "Anamnesis expandida: biología del conflicto, historia familiar, "
         "terreno funcional. Identificación del DHS y mapa sistémico."],
        ["4", "Protocolo personalizado + seguimiento coordinado",
         "Sesiones individuales, talleres grupales (4–8 personas), "
         "ajuste dietético y funcional. Revisión quincenal de avance."],
        ["5", "Retroalimentación al especialista",
         "Informe clínico integrativo entregado al médico derivador. "
         "El especialista accede a la dimensión psiconeurobiológica del caso."],
    ]

    t = Table(
        [[Paragraph(n, styles['label_teal']),
          Paragraph(step, styles['h3_teal']),
          Paragraph(desc, styles['body_small'])]
         for n, step, desc in pathway],
        colWidths=[1*cm, 5.2*cm, CONTENT_W - 6.2*cm]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), TEAL),
        ('TEXTCOLOR', (0, 0), (0, -1), WHITE),
        ('BACKGROUND', (1, 0), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (1, 0), (-1, -1), [WHITE, HexColor('#F5F5F3')]),
        ('GRID', (0, 0), (-1, -1), 0.3, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, -1), 11),
        ('BACKGROUND', (0, 4), (-1, 4), TEAL_LIGHT),
        ('LINEBEFORE', (0, 4), (0, 4), 3, TEAL),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    story.append(Paragraph("5.1  Criterios de Inclusión para Derivación", styles['h1']))
    criterios = [
        "Enfermedad crónica no transmisible con más de 6 meses de evolución "
        "y respuesta parcial o nula al tratamiento convencional.",
        "Polimedicación (3 o más fármacos crónicos) con baja adherencia documentada.",
        "Recidivas frecuentes (más de 3 episodios en 12 meses) de la misma patología.",
        "Paciente que refiere componente emocional o de estrés asociado al inicio "
        "o exacerbación del cuadro clínico.",
        "Solicitud expresa del paciente tras información sobre el modelo.",
        "Cuadros con componente funcional predominante sin correlato orgánico claro.",
    ]
    for c in criterios:
        story.append(Paragraph(f"\u2022  {c}", styles['bullet']))

    return story


# ──────────────────────────────────────────────
# SECTION 6 — OBJECTIVES
# ──────────────────────────────────────────────
def build_objectives(styles):
    story = []
    story += section_banner(styles, "6.  Objetivos Clínicos e Indicadores de Resultados")

    story.append(Paragraph(
        "El CEMIS opera bajo un marco de evaluación de resultados basado en "
        "indicadores clínicos medibles desde el primer día de atención. La "
        "medición sistemática es condición indispensable para la credibilidad "
        "científica del modelo y para su escalabilidad institucional.",
        styles['body']
    ))

    obj_headers = ["Dimensión", "Objetivo", "Indicador de Medición"]
    obj_rows = [
        ["Adherencia terapéutica",
         "Mejorar el cumplimiento del tratamiento alopático prescrito",
         "% adherencia reportado en revisión a 3 y 6 meses"],
        ["Carga medicamentosa",
         "Reducir el número de fármacos crónicos activos",
         "N.° de fármacos en receta al inicio vs. 12 meses"],
        ["Tiempo de enfermedad",
         "Disminuir la duración de los episodios agudos",
         "Días de baja / días de crisis por periodo"],
        ["Rehospitalizaciones",
         "Reducir reingresos evitables por la misma causa",
         "Tasa de reingreso a 30, 90 y 180 días"],
        ["Calidad de vida",
         "Mejora objetiva en escalas validadas",
         "SF-36 o WHOQOL-BREF al inicio, 6 y 12 meses"],
        ["Satisfacción del médico derivador",
         "Utilidad percibida del informe integrativo",
         "Encuesta estructurada al especialista cada trimestre"],
        ["Morbilidad / mortalidad (largo plazo)",
         "Impacto sobre la historia natural de la enfermedad",
         "Análisis de cohorte a 18 meses vs. grupo control SISOL"],
    ]
    story += data_table(styles, obj_headers, obj_rows,
                        [3.2*cm, 5.5*cm, CONTENT_W - 8.7*cm])

    story += info_box(styles, [
        Paragraph(
            "Si el modelo reduce las rehospitalizaciones en tan solo un 10% en "
            "un sistema con 120 millones de consultas acumuladas, el impacto "
            "social —y el ahorro económico directo para SISOL— es transformador.",
            styles['callout']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)
    return story


# ──────────────────────────────────────────────
# SECTION 7 — DEPARTMENT NAME
# ──────────────────────────────────────────────
def build_naming(styles):
    story = []
    story += section_banner(styles, "7.  Propuesta de Nombre del Departamento")

    story.append(Paragraph(
        "La denominación del departamento tiene valor estratégico: debe ser "
        "científicamente rigurosa, institucionalmente coherente con la marca "
        "SISOL y accesible para el paciente general. Se presentan seis opciones "
        "evaluadas según tres criterios: recordabilidad, coherencia institucional "
        "y precisión clínica.",
        styles['body']
    ))

    names_headers = ["Opción", "Denominación", "Acrónimo", "Fortaleza principal"]
    names_rows = [
        ["★ Recomendada",
         "Centro de Medicina Integrativa Solidaria",
         "CEMIS",
         "Une la identidad SISOL con el concepto médico. Memorable y escalable."],
        ["2",
         "Departamento de Salud Integral y Bienestar",
         "DSIB",
         "Lenguaje de salud pública clásico. Conservador y de fácil adopción."],
        ["3",
         "Centro de Medicina Mente-Cuerpo-Familia",
         "CMCF",
         "Refleja los tres niveles del modelo. Comprensible para el paciente."],
        ["4",
         "Unidad de Medicina Complementaria y Biológica",
         "UMCB",
         "Científico y preciso. Distancia explícitamente de 'medicina alternativa'."],
        ["5",
         "Centro de Atención Integrativa SISOL",
         "CAIS",
         "Simple, institucional y replicable en todas las sedes."],
        ["6",
         "Área de Medicina Funcional e Integrativa",
         "AMFI",
         "Alineado con la terminología internacional (Functional Medicine)."],
    ]
    t_names = Table(
        [
            [Paragraph(h, styles['table_header']) for h in names_headers]
        ] + [
            [
                Paragraph(r[0], styles['table_cell_bold']
                          if '★' in r[0] else styles['table_cell']),
                Paragraph(r[1], styles['table_cell_bold']
                          if '★' in r[0] else styles['table_cell']),
                Paragraph(r[2], styles['label_teal']
                          if '★' in r[0] else styles['table_cell']),
                Paragraph(r[3], styles['body_small']),
            ]
            for r in names_rows
        ],
        colWidths=[2.5*cm, 5.5*cm, 2*cm, CONTENT_W - 10*cm],
        repeatRows=1
    )
    t_names.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, 1), HexColor('#D4EDEA')),
        ('ROWBACKGROUNDS', (0, 2), (-1, -1), [WHITE, HexColor('#F5F5F3')]),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
    ]))
    story.append(t_names)
    story.append(Spacer(1, 8))
    return story


# ──────────────────────────────────────────────
# SECTION 8 — BIO
# ──────────────────────────────────────────────
def build_bio(styles):
    story = []
    story += section_banner(styles, "8.  Perfil Profesional de la Directora Propuesta")

    story += info_box(styles, [
        Paragraph(
            '"No es una terapeuta. Es una médico que practica medicina desde la raíz."',
            styles['quote']
        )
    ], bg=PEACH_LIGHT, left_bar=PEACH)

    bio_data = [
        ["Nombre completo", "Dra. Ximena Chirinos Orbegozo"],
        ["Número de colegiatura", "CMP 36103 — Colegiada y habilitada"],
        ["Trayectoria principal",
         "Más de 15 años en Medicina Ocupacional — disciplina sistémica, "
         "preventiva, centrada en entornos y contextos de vida del paciente."],
        ["Especialización 1",
         "Nueva Medicina Germánica (Germanische Heilkunde) — "
         "Método del Dr. Ryke Geerd Hamer. Especialista certificada."],
        ["Especialización 2",
         "Constelaciones Familiares y Terapia Sistémica Familiar."],
        ["Especialización 3",
         "Medicina Funcional — microbiota, eje intestino-cerebro, "
         "medicina antiinflamatoria personalizada."],
        ["Centro de práctica",
         "Clínica Magga · La Molina, Lima · clinicamagga.com"],
    ]
    t = Table(bio_data, colWidths=[4*cm, CONTENT_W - 4*cm])
    t.setStyle(TableStyle([
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [HexColor('#F0FAFA'), WHITE]),
        ('GRID', (0, 0), (-1, -1), 0.3, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, -1), TEAL),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    story.append(Paragraph("8.1  Por qué ella es la persona adecuada", styles['h1']))
    story.append(Paragraph(
        "La Dra. Chirinos ocupa una posición singular en el panorama médico peruano: "
        "está en la intersección exacta entre la medicina convencional y la integrativa. "
        "No rechaza ninguna de las dos — las articula. Tiene el título, la habilitación "
        "colegial, la experiencia clínica en entornos sistémicos (Medicina Ocupacional) "
        "y las certificaciones especializadas en cada uno de los tres pilares del CEMIS.",
        styles['body']
    ))
    story.append(Paragraph(
        "Eso es precisamente lo que este departamento necesita: una directora que "
        "hable los dos idiomas médicos con igual fluidez, que pueda establecer "
        "protocolos conjuntos con los especialistas alopáticos y que tenga la "
        "credibilidad institucional para representar al CEMIS ante SISOL, el MINSA "
        "y la comunidad médica peruana.",
        styles['body']
    ))
    return story


# ──────────────────────────────────────────────
# SECTION 9 — IMPLEMENTATION PLAN
# ──────────────────────────────────────────────
def build_implementation(styles):
    story = []
    story += section_banner(styles, "9.  Plan de Implementación — 3 Fases / 18 Meses")
    story.append(Paragraph(
        "El plan de implementación contempla tres fases secuenciales diseñadas "
        "para minimizar el riesgo institucional, maximizar el aprendizaje operativo "
        "y garantizar la calidad asistencial desde el primer día de atención.",
        styles['body']
    ))

    phases = [
        {
            "title": "Fase 1 — Fundación (Meses 0–3)",
            "color": TEAL,
            "bg": TEAL_LIGHT,
            "style": "h3_teal",
            "cols": [
                ("Diseño del Departamento", [
                    "Protocolos de derivación con cada especialidad",
                    "Criterios de inclusión / exclusión de pacientes",
                    "Ficha clínica integrativa (historia expandida)",
                    "Indicadores de seguimiento y outcome",
                ]),
                ("Instalación Física", [
                    "2–3 consultorios en el Hospital de Salud Mental",
                    "Adquisición de equipamiento básico",
                    "Sistema de agendamiento integrado",
                    "Selección y onboarding del personal de apoyo",
                ]),
                ("Integración Institucional", [
                    "Presentación ante jefes de departamento",
                    "Protocolo de comunicación médico-médico",
                    "Capacitación básica del equipo SISOL sobre el modelo",
                ]),
            ]
        },
        {
            "title": "Fase 2 — Lanzamiento (Meses 3–9)",
            "color": HexColor('#C06030'),
            "bg": PEACH_LIGHT,
            "style": "h3_orange",
            "cols": [
                ("Primera Cohorte de Pacientes", [
                    "5–8 pacientes/día en etapa inicial",
                    "Prioridad: crónicos complejos ya atendidos en SISOL",
                    "Sesiones individuales (90 min) y grupales (4–8 personas)",
                    "Revisión quincenal con los especialistas derivadores",
                ]),
                ("Medición desde el Día 1", [
                    "Registro de outcomes: tiempo de enfermedad, medicación, "
                    "calidad de vida",
                    "Escala de satisfacción del paciente",
                    "Feedback del médico derivador",
                    "Comparativo con cohorte de control",
                ]),
                ("Talleres Grupales", [
                    "Psicoeducación: biología del conflicto para pacientes",
                    "Taller de dieta funcional y microbiota",
                    "Taller sistémico-familiar (introductorio)",
                    "Materiales accesibles para el público general",
                ]),
            ]
        },
        {
            "title": "Fase 3 — Expansión y Evidencia (Meses 9–18)",
            "color": GREEN,
            "bg": GREEN_LIGHT,
            "style": "h3_green",
            "cols": [
                ("Escala", [
                    "12–15 pacientes/día a plena capacidad",
                    "Extensión progresiva a otras sedes SISOL",
                    "Formación de un segundo médico integrativo",
                ]),
                ("Publicación de Resultados", [
                    "Sistematización de la data clínica (18 meses)",
                    "Informe de resultados para SISOL y MINSA",
                    "Posicionamiento como modelo de referencia nacional",
                    "Artículo para revista médica peruana indexada",
                ]),
                ("Alianzas Internacionales", [
                    "Conexión con redes de medicina integrativa en salud pública",
                    "OPS/OMS: alineamiento con Estrategia de Medicina "
                    "Tradicional y Complementaria 2019–2025",
                    "Intercambio con Brasil (PNPIC) y Argentina (CASID)",
                ]),
            ]
        },
    ]

    for ph in phases:
        title_t = Table(
            [[Paragraph(ph['title'], styles['section_title'])]],
            colWidths=[CONTENT_W]
        )
        title_t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), ph['color']),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(KeepTogether([title_t, Spacer(1, 4)]))

        col_w = (CONTENT_W / 3) - 0.3*cm
        row_cells = []
        for col_title, col_items in ph['cols']:
            cell_content = [Paragraph(col_title, styles[ph['style']])]
            for item in col_items:
                cell_content.append(Paragraph(f"\u2022  {item}",
                                               styles['bullet_small']))
            card = Table(
                [[c] for c in cell_content],
                colWidths=[col_w]
            )
            card.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), ph['bg']),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (0, 0), 8),
                ('BOTTOMPADDING', (0, -1), (0, -1), 8),
                ('TOPPADDING', (0, 1), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -2), 2),
            ]))
            row_cells.append(card)

        grid = Table([row_cells],
                     colWidths=[col_w + 0.3*cm, col_w + 0.3*cm, col_w + 0.3*cm])
        grid.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))
        story.append(grid)
        story.append(Spacer(1, 8))

    return story


# ──────────────────────────────────────────────
# SECTION 10 — INVESTMENT
# ──────────────────────────────────────────────
def build_investment(styles):
    story = []
    story += section_banner(styles, "10.  Estructura de Inversión y Proyección Financiera")
    story.append(Paragraph(
        "La inversión requerida para la implementación del CEMIS es notablemente "
        "contenida en comparación con el valor clínico y social que genera. "
        "El modelo está diseñado para alcanzar el punto de equilibrio operativo "
        "en la fase de lanzamiento, sin comprometer la calidad asistencial.",
        styles['body']
    ))

    story.append(Paragraph("10.1  Estructura del Departamento", styles['h1']))
    struct_headers = ["Ítem", "Modalidad", "Costo Estimado"]
    struct_rows = [
        ["Equipamiento inicial", "Inversión única",
         "S/ 15,000 – S/ 20,000"],
        ["Coordinadora administrativa", "Contrato mensual",
         "S/ 1,800 – S/ 2,200/mes"],
        ["Asistente clínica", "Contrato mensual",
         "S/ 1,500 – S/ 1,800/mes"],
        ["Materiales y consumibles", "Gasto operativo mensual",
         "S/ 800/mes"],
        ["Total costos operativos recurrentes", "",
         "S/ 4,100 – S/ 4,800/mes"],
    ]
    t_struct = Table(
        [[Paragraph(h, styles['table_header']) for h in struct_headers]] +
        [[Paragraph(r[0], styles['table_cell_bold']),
          Paragraph(r[1], styles['table_cell']),
          Paragraph(r[2], styles['table_cell_bold'] if r[0].startswith('Total')
                    else styles['table_cell'])]
         for r in struct_rows],
        colWidths=[6*cm, 4.5*cm, CONTENT_W - 10.5*cm],
        repeatRows=1
    )
    t_struct.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [WHITE, HexColor('#F5F5F3')]),
        ('BACKGROUND', (0, -1), (-1, -1), TEAL_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_struct)
    story.append(Spacer(1, 10))

    story.append(Paragraph("10.2  Compensación de la Directora del Departamento",
                            styles['h1']))
    comp_headers = ["Concepto", "Detalle"]
    comp_rows = [
        ["Título institucional", "Directora / Jefa del Departamento CEMIS"],
        ["Remuneración base mensual", "S/ 8,000 – S/ 10,000"],
        ["Revenue share variable",
         "15–20% sobre facturación mensual superior a S/ 25,000"],
        ["Presupuesto de investigación", "S/ 1,500/mes (publicaciones y congresos)"],
        ["Revisión contractual", "A los 6 meses según indicadores pactados"],
    ]
    t_comp = Table(
        [[Paragraph(h, styles['table_header']) for h in comp_headers]] +
        [[Paragraph(r[0], styles['table_cell_bold']),
          Paragraph(r[1], styles['table_cell'])]
         for r in comp_rows],
        colWidths=[5*cm, CONTENT_W - 5*cm],
        repeatRows=1
    )
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#C06030')),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor('#FDF5F2')]),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 10))

    story.append(Paragraph("10.3  Proyección de Ingresos y Punto de Equilibrio",
                            styles['h1']))
    rev_headers = ["Escenario", "Pacientes/día", "Días/mes",
                   "Tarifa promedio", "Facturación mensual"]
    rev_rows = [
        ["Punto de equilibrio", "8–9", "20", "S/ 120",
         "S/ 19,200 – S/ 21,600"],
        ["Capacidad inicial (Fase 2)", "10–12", "20", "S/ 120",
         "S/ 24,000 – S/ 28,800"],
        ["Capacidad plena (Fase 3)", "15", "20", "S/ 120",
         "S/ 36,000"],
    ]
    t_rev = Table(
        [[Paragraph(h, styles['table_header']) for h in rev_headers]] +
        [[Paragraph(r[0], styles['table_cell_bold' if i == 0 else 'table_cell'])
          for i, r in enumerate([(r[j], j) for j in range(len(r))])]
         for r in rev_rows],
        colWidths=[3.5*cm, 2.8*cm, 2.4*cm, 3.5*cm, CONTENT_W - 12.2*cm],
        repeatRows=1
    )
    t_rev.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, HexColor('#F5F5F3')]),
        ('BACKGROUND', (0, -1), (-1, -1), TEAL_LIGHT),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#E0E0E0')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(t_rev)
    story.append(Spacer(1, 8))

    story += info_box(styles, [
        Paragraph(
            "El CEMIS alcanza su punto de equilibrio operativo con 8–9 pacientes/día, "
            "equivalente al 60% de la capacidad inicial de Fase 2. "
            "A capacidad plena genera un margen operativo estimado de "
            "<b>S/ 22,000–25,000/mes</b> antes de considerar el componente "
            "académico y de formación.",
            styles['body']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)
    return story


# ──────────────────────────────────────────────
# SECTION 11 — INTERNATIONAL EVIDENCE
# ──────────────────────────────────────────────
def build_evidence(styles):
    story = []
    story += section_banner(styles, "11.  Evidencia Internacional y Marco Regulatorio")
    story.append(Paragraph(
        "La medicina integrativa no es una tendencia emergente: es una política "
        "de salud pública consolidada en los sistemas sanitarios más eficientes "
        "del mundo. El CEMIS no inventa un modelo; adapta al contexto peruano "
        "lo que otros sistemas de salud ya practican con evidencia documentada.",
        styles['body']
    ))

    evid_headers = ["Institución / País", "Modalidad", "Año de implementación",
                    "Referencia"]
    evid_rows = [
        ["Brasil — Sistema Único de Salud",
         "Política Nacional de Práticas Integrativas e Complementares (PNPIC)",
         "2006",
         "Ministerio de Salud de Brasil"],
        ["OMS — Global",
         "Estrategia de Medicina Tradicional y Complementaria 2019–2025",
         "2019",
         "WHO/HIS/TRM/19.1"],
        ["Cleveland Clinic (EE.UU.)",
         "Center for Integrative & Lifestyle Medicine",
         "Activo",
         "my.clevelandclinic.org"],
        ["Johns Hopkins Medicine (EE.UU.)",
         "Johns Hopkins Integrative Medicine & Digestive Center",
         "Activo",
         "hopkinsmedicine.org"],
        ["Mayo Clinic (EE.UU.)",
         "Complementary and Integrative Medicine Program",
         "Activo",
         "mayoclinic.org"],
        ["Argentina — CASID",
         "Cámara Argentina de Salud Integrativa y Disciplinas",
         "2010",
         "casid.com.ar"],
        ["Perú — MINSA",
         "R.M. N.° 724-2009/MINSA — Medicina Complementaria en EsSalud",
         "2009",
         "MINSA / EsSalud"],
    ]
    story += data_table(styles, evid_headers, evid_rows,
                        [3.5*cm, 5.5*cm, 2.5*cm, CONTENT_W - 11.5*cm])

    story.append(Paragraph(
        "De especial relevancia es el antecedente peruano: EsSalud cuenta desde "
        "2009 con centros de medicina complementaria en funcionamiento regular. "
        "SISOL tiene la oportunidad de ampliar ese precedente con un modelo más "
        "completo, más integrado y con mayor capacidad de medición de resultados.",
        styles['body']
    ))

    story += info_box(styles, [
        Paragraph(
            '"Brasil integró las terapias complementarias en su sistema público '
            'de salud en 2006. La OMS publicó su Estrategia de Medicina Tradicional '
            'y Complementaria en 2019. Cleveland Clinic, Johns Hopkins, Mayo Clinic '
            '— todos tienen departamentos de medicina integrativa. '
            'No inventamos nada. Llevamos al Perú lo que el mundo ya practica."',
            styles['quote']
        )
    ], bg=TEAL_LIGHT, left_bar=TEAL)
    return story


# ──────────────────────────────────────────────
# SECTION 12 — NEXT STEPS
# ──────────────────────────────────────────────
def build_next_steps(styles):
    story = []
    story += section_banner(styles, "12.  Próximos Pasos y Solicitud Formal")

    story.append(Paragraph(
        "La presente propuesta constituye el documento base para iniciar el "
        "proceso formal de creación del CEMIS. Se solicita respetuosamente al "
        "Dr. Luis Rubio Ramos, Presidente de SISOL, la evaluación de los "
        "siguientes pasos:",
        styles['body']
    ))

    steps = [
        ("Paso 1 — Aprobación del concepto",
         "Aprobación institucional del concepto de departamento de medicina "
         "integrativa como componente de la estrategia de salud pública de SISOL "
         "para el período 2025–2027."),
        ("Paso 2 — Reunión de diseño conjunto",
         "Reunión técnica entre la Dra. Chirinos y el equipo directivo de SISOL "
         "para definir: espacio físico disponible, recursos humanos de apoyo, "
         "cronograma de implementación de Fase 1 y estructura legal de la dirección."),
        ("Paso 3 — Marco contractual",
         "Definición de la estructura contractual de la Dirección del CEMIS: "
         "modalidad de vinculación, compensación, indicadores de desempeño y "
         "condiciones de la revisión semestral."),
        ("Paso 4 — Protocolo interservicio",
         "Diseño participativo del protocolo de derivación con los jefes de "
         "servicio de las especialidades con mayor volumen de pacientes crónicos."),
        ("Paso 5 — Lanzamiento oficial",
         "Comunicado institucional de apertura del CEMIS, orientado tanto al "
         "equipo médico interno como a los pacientes SISOL y a los medios de "
         "comunicación especializados en salud."),
    ]

    for title, desc in steps:
        step_t = Table(
            [[Paragraph(title, styles['h3_teal']),
              Paragraph(desc, styles['body_small'])]],
            colWidths=[4.5*cm, CONTENT_W - 4.5*cm]
        )
        step_t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), GRAY_BG),
            ('BACKGROUND', (0, 0), (0, 0), TEAL_LIGHT),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.3, HexColor('#E0E0E0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LINEBEFORE', (0, 0), (0, -1), 3, TEAL),
        ]))
        story.append(step_t)
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 16))

    # Closing statement
    closing_t = Table(
        [[Paragraph(
            "Usted llevó los hospitales a la calle.<br/>"
            "<b>Ahora llevemos la medicina completa a los hospitales.</b><br/><br/>"
            "Dr. Hamer transformó su pérdida en una nueva medicina.<br/>"
            "SISOL transformó una visión en 54 hospitales y 120 millones de consultas.<br/>"
            "Hoy proponemos la siguiente transformación:<br/>"
            "<b>medicina que sana desde la raíz.</b>",
            ParagraphStyle('closing', fontSize=11, textColor=DARK,
                           fontName='Helvetica', leading=18,
                           alignment=TA_CENTER)
        )]],
        colWidths=[CONTENT_W]
    )
    closing_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TEAL_LIGHT),
        ('LEFTPADDING', (0, 0), (-1, -1), 30),
        ('RIGHTPADDING', (0, 0), (-1, -1), 30),
        ('TOPPADDING', (0, 0), (-1, -1), 24),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 24),
        ('LINEBEFORE', (0, 0), (0, -1), 5, TEAL),
        ('LINEAFTER', (0, 0), (-1, -1), 5, TEAL),
    ]))
    story.append(closing_t)
    story.append(Spacer(1, 16))

    # Signature block
    sig_t = Table(
        [[
            Table(
                [
                    [Paragraph("<b>Dra. Ximena Chirinos Orbegozo</b>",
                               styles['body'])],
                    [Paragraph("CMP 36103", styles['body_small'])],
                    [Paragraph(
                        "Médico Integrativa · Directora Propuesta CEMIS",
                        styles['body_small']
                    )],
                    [Paragraph("Clínica Magga · La Molina, Lima",
                               styles['body_small'])],
                    [Paragraph("clinicamagga.com", styles['body_small'])],
                ],
                colWidths=[(CONTENT_W / 2) - 1*cm]
            ),
            Table(
                [
                    [Paragraph(f"Lima, Perú — {date.today().strftime('%d de %B de %Y')}",
                               styles['body_small'])],
                    [Spacer(1, 20)],
                    [HRFlowable(width=(CONTENT_W / 2) - 2*cm,
                                thickness=0.5, color=HexColor('#AAAAAA'))],
                    [Paragraph("Firma / Sello", styles['footer'])],
                ],
                colWidths=[(CONTENT_W / 2) - 1*cm]
            ),
        ]],
        colWidths=[CONTENT_W / 2, CONTENT_W / 2]
    )
    sig_t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(sig_t)
    return story


# ──────────────────────────────────────────────
# TABLE OF CONTENTS (simple)
# ──────────────────────────────────────────────
def build_toc(styles):
    story = []
    story += section_banner(styles, "Índice de Contenidos")

    toc_items = [
        ("1.", "Resumen Ejecutivo"),
        ("2.", "Contexto Epidemiológico y Necesidad Institucional"),
        ("3.", "Marco Científico y Teórico"),
        ("4.", "Los Tres Pilares del Departamento CEMIS"),
        ("5.", "Modelo de Atención — Flujo Clínico Integrado"),
        ("6.", "Objetivos Clínicos e Indicadores de Resultados"),
        ("7.", "Propuesta de Nombre del Departamento"),
        ("8.", "Perfil Profesional de la Directora Propuesta"),
        ("9.", "Plan de Implementación — 3 Fases / 18 Meses"),
        ("10.", "Estructura de Inversión y Proyección Financiera"),
        ("11.", "Evidencia Internacional y Marco Regulatorio"),
        ("12.", "Próximos Pasos y Solicitud Formal"),
    ]

    for num, title in toc_items:
        row_t = Table(
            [[Paragraph(num, styles['label_teal']),
              Paragraph(title, styles['body'])]],
            colWidths=[0.8*cm, CONTENT_W - 0.8*cm]
        )
        row_t.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, HexColor('#EEEEEE')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(row_t)

    story.append(PageBreak())
    return story


# ──────────────────────────────────────────────
# MAIN BUILD
# ──────────────────────────────────────────────
def build_pdf():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    canvas_obj = DocCanvas(
        "Propuesta CEMIS — Medicina Integrativa SISOL"
    )

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T + 0.8*cm,   # extra for header bar
        bottomMargin=MARGIN_B + 0.8*cm,
        title="Propuesta CEMIS — Departamento de Medicina Integrativa SISOL",
        author="Dra. Ximena Chirinos Orbegozo CMP 36103",
        subject="Propuesta de implementación del Centro de Medicina Integrativa Solidaria",
        creator="CEMIS Proposal Generator v1.0",
    )

    styles = build_styles()

    story = []
    story += build_cover(styles)
    story += build_toc(styles)
    story += build_executive_summary(styles)
    story.append(PageBreak())
    story += build_context(styles)
    story.append(PageBreak())
    story += build_science(styles)
    story.append(PageBreak())
    story += build_pillars(styles)
    story.append(PageBreak())
    story += build_model(styles)
    story.append(PageBreak())
    story += build_objectives(styles)
    story.append(PageBreak())
    story += build_naming(styles)
    story += build_bio(styles)
    story.append(PageBreak())
    story += build_implementation(styles)
    story.append(PageBreak())
    story += build_investment(styles)
    story.append(PageBreak())
    story += build_evidence(styles)
    story.append(PageBreak())
    story += build_next_steps(styles)

    doc.build(story,
              onFirstPage=canvas_obj.on_page,
              onLaterPages=canvas_obj.on_page)

    print(f"\n✓ PDF generated: {OUTPUT_PATH}")
    print(f"  Size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")


if __name__ == "__main__":
    build_pdf()
