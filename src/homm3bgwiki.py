import functools
import re
from xml.etree.ElementTree import Element

from markdown import Markdown
from pymdownx import emoji


# copied from material.extensions.emoji.to_svg but stripping some extra whitespace
def to_svg(
    index: str,
    shortname: str,
    alias: str,
    uc: str | None,
    alt: str,
    title: str,
    category: str,
    options: object,
    md: Markdown,
):
    if not uc:
        icons = md.inlinePatterns["emoji"].emoji_index["emoji"]

        # Create and return element to host icon
        el = Element("span", {"class": options.get("classes", index)})
        el.text = md.htmlStash.store(_load(icons[shortname]["path"]))
        return el

    # Delegate to `pymdownx.emoji` extension
    return emoji.to_svg(index, shortname, alias, uc, alt, title, category, options, md)


@functools.cache
def _load(file: str):
    with open(file, encoding="utf-8") as f:
        s = f.read()
        return re.sub(r"\s+", " ", s).strip()


def glyph_svg(*args, **kwargs):
    name = args[1].strip(":")
    result = Element("span", {"class": "glyph"})
    result.append(to_svg(*args, **kwargs))
    text = Element("span", {"class": "glyph-text"})
    text.text = f"&lt;{name}&gt;"
    result.append(text)
    return result
