import material.extensions.emoji
from xml.etree.ElementTree import Element

def glyph_svg(*a, **kv):
    name = a[1].strip(':')
    result = Element("span", {"class": "glyph"})
    result.append(material.extensions.emoji.to_svg(*a, **kv))
    text = Element("span", {"class": "glyph-text"})
    text.text = f"&lt;{name}&gt;"
    result.append(text)
    return result
