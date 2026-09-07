import re

# ---------- Regex patterns ----------

RED_PATTERN = re.compile(r"<Red>(.*?)</Red>", re.DOTALL)

BOX_PATTERN = re.compile(
    r":::box\s+(left|mid|right|full)\s*(#[\w\-]+)?\s*\n(.*?)\n:::",
    re.DOTALL
)

ARROW_PATTERN = re.compile(r":::arrow:::")

ROW_GROUP_PATTERN = re.compile(
    r'(?:<div class="note-box[^>]*>.*?</div>\s*|<div class="note-arrow">.*?</div>\s*){2,}',
    re.DOTALL
)


PAGE_BREAK_PATTERN = re.compile(r"::page break::")



def replace_page_markers(text: str) -> str:
    text = PAGE_BREAK_PATTERN.sub('<div class="page-marker"></div>', text)
    return text


def replace_red(text: str) -> str:
    return RED_PATTERN.sub(r'<span class="note-red">\1</span>', text)


def replace_boxes(text: str) -> str:
    def box_sub(match):
        position = match.group(1)
        box_id = match.group(2)[1:] if match.group(2) else ""
        content = match.group(3).strip()
        content_html = content.replace("\n", "<br>")
        id_attr = f' id="{box_id}"' if box_id else ""
        return (
            f'<div class="note-box pos-{position}"{id_attr}>'
            f'<div class="note-box-content">{content_html}</div>'
            f'</div>'
        )
    return BOX_PATTERN.sub(box_sub, text)


def replace_arrows(text: str) -> str:
    return ARROW_PATTERN.sub('<div class="note-arrow">&#8594;</div>', text)


def wrap_rows(text: str) -> str:
    def row_sub(match):
        block = match.group(0).strip()
        return f'<div class="notes-row">\n{block}\n</div>\n'
    return ROW_GROUP_PATTERN.sub(row_sub, text)


def on_page_markdown(markdown, page, config, files):
    text = markdown
    text = replace_red(text)
    text = replace_boxes(text)
    text = replace_arrows(text)
    text = replace_page_markers(text)
    text = wrap_rows(text)
    return text