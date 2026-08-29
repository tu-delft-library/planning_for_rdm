import re


def convert_html_links(text: str) -> str:
    """
    Convert HTML links:

        [Example](https://example.com/)

    to Markdown:

        [Example](https://example.com/)
    """

    pattern = re.compile(
        r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )

    def replace_link(match):
        url = match.group(1)
        label = match.group(2).strip()

        # Remove possible HTML tags inside the link text
        label = re.sub(r"<[^>]+>", "", label)

        return f"[{label}]({url})"

    return pattern.sub(replace_link, text)