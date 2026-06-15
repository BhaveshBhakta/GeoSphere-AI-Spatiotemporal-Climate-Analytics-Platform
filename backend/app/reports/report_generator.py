from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER
)


def generate_report(
    filename,
    report_data
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        spaceAfter=25
    )

    section_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        spaceBefore=10,
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        leading=18,
        spaceAfter=5
    )

    elements = []

    # -------------------------
    # TITLE
    # -------------------------

    elements.append(
        Paragraph(
            "Climate Intelligence Report",
            title_style
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # -------------------------
    # CONTENT
    # -------------------------

    for key, value in report_data.items():

        elements.append(
            Paragraph(
                key,
                section_style
            )
        )

        lines = str(value).split("\n")

        for line in lines:

            cleaned = line.strip()

            if cleaned:

                elements.append(
                    Paragraph(
                        cleaned,
                        body_style
                    )
                )

        elements.append(
            Spacer(1, 12)
        )

    doc.build(elements)