import re
import html
from pathlib import Path


CENTER_RE = re.compile(
    r"<\s*center\s*>(.*?)<\s*/\s*center\s*>",
    re.IGNORECASE | re.DOTALL,
)

IMG_RE = re.compile(
    r"<\s*img\b([^>]*)/?>",
    re.IGNORECASE | re.DOTALL,
)

P_RE = re.compile(
    r"<\s*p\b[^>]*>(.*?)<\s*/\s*p\s*>",
    re.IGNORECASE | re.DOTALL,
)

ATTR_RE = re.compile(
    r"""(\w+)\s*=\s*["'](.*?)["']""",
    re.DOTALL,
)


def strip_html(text: str) -> str:
    """Remove simple HTML tags and decode HTML entities."""
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def convert_center_block(match: re.Match) -> str:
    content = match.group(1)

    # Find image
    img_match = IMG_RE.search(content)
    if not img_match:
        return match.group(0)

    attrs = dict(ATTR_RE.findall(img_match.group(1)))

    src = attrs.get("src", "")
    alt = attrs.get("alt", "")
    style = attrs.get("style", "")

    # Extract width from style="width: 600px; ..."
    width_match = re.search(
        r"width\s*:\s*(\d+(?:\.\d+)?)px",
        style,
        re.IGNORECASE,
    )
    width = f"{width_match.group(1)}px" if width_match else None

    # Find caption
    p_match = P_RE.search(content)
    caption = strip_html(p_match.group(1)) if p_match else ""

    # Build MyST figure directive
    lines = [
        f":::{'{'}figure{'}'} {src}",
    ]

    if alt:
        lines.append(f":alt: {alt}")

    if width:
        lines.append(f":width: {width}")

    if caption:
        lines.extend(["", caption])

    lines.append(":::")

    return "\n".join(lines)


def convert_html_figures(text: str) -> str:
    return CENTER_RE.sub(convert_center_block, text)


def convert_file(input_file: str, output_file: str) -> None:
    source = Path(input_file)
    destination = Path(output_file)

    text = source.read_text(encoding="utf-8")
    converted = convert_html_figures(text)
    destination.write_text(converted, encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert centered HTML figures to MyST Markdown figures."
    )
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("output", help="Output Markdown file")

    args = parser.parse_args()

    convert_file(args.input, args.output)