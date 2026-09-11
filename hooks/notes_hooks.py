import re

# ---------- Regex patterns ----------

RED_PATTERN = re.compile(r"<Red>(.*?)</Red>", re.DOTALL)
BLUE_PATTERN = re.compile(r"<Blue>(.*?)</Blue>", re.DOTALL)

# BOX_PATTERN = re.compile(
#     r":::box\s+(left|right)\s*\n(.*?)\n:::",
#     re.DOTALL
# )

BOX_PATTERN = re.compile(r"::box\s*\n(.*?)\n::", re.DOTALL)

ROW_GROUP_PATTERN = re.compile(
    r'(?:<div class="note-box[^>]*>.*?</div>\s*){2,}',
    re.DOTALL
)

PAGE_BREAK_PATTERN = re.compile(r"::page break::")


def replace_page_markers(text: str) -> str:
    return PAGE_BREAK_PATTERN.sub('<div class="page-marker"></div>', text)


def replace_red(text: str) -> str:
    return RED_PATTERN.sub(r'<span class="note-red">\1</span>', text)


def replace_blue(text: str) -> str:
    return BLUE_PATTERN.sub(r'<span class="note-blue">\1</span>', text)


def replace_boxes(text: str) -> str:
    def box_sub(match):
        content = match.group(1).strip()

        if "```" in content:
            return f'<div class="note-box" markdown="1">\n\n{content}\n\n</div>'

        content_html = content.replace("\n", "<br>")
        return f'<div class="note-box"><div class="note-box-content">{content_html}</div></div>'

    return BOX_PATTERN.sub(box_sub, text)

def wrap_rows(text: str) -> str:
    def row_sub(match):
        block = match.group(0).strip()
        return f'<div class="notes-row">\n{block}\n</div>\n'
    return ROW_GROUP_PATTERN.sub(row_sub, text)


def on_page_markdown(markdown, page, config, files):
    text = markdown
    text = replace_red(text)
    text = replace_blue(text)
    text = replace_boxes(text)
    text = replace_page_markers(text)
    text = wrap_rows(text)
    return text