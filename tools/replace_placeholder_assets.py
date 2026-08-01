"""Repoint placeholder card images to the real assets added in expansion/assets.

Placeholders:
  ../assets/player-deck-back.webp   (generic card back)
  ../assets/units-blank-{tier}.webp (blank unit card, tier = card-back colour)

For every .md under docs/{abilities,spells,artifacts,war_machines,heroes,units}
(index.md skipped), each placeholder image src is rewritten to the real asset
computed from the page/category/tab -- but only when that asset actually exists
in docs/assets/. Unresolved placeholders (missing or ambiguous art) are left
untouched and reported. Idempotent; safe to re-run.
"""

import os
import re
import sys
import glob
from pathlib import Path

ASSETS_DIR = "docs/assets"
CATEGORIES = ("abilities", "spells", "war_machines", "artifacts", "heroes", "units",
              "astrologers_proclaim")

# Matches a markdown image whose src is a placeholder, capturing the src path.
IMG_RE = re.compile(
    r'(\.\./assets/(?:player-deck-back|units-blank-\w+|astrologers_proclaim-back)\.webp)')
TAB_RE = re.compile(r'\s*=== "(.+)"')
BLANK_TIER_RE = re.compile(r'units-blank-(\w+)\.webp')
TOWN_RE = re.compile(r'\.\./towns/([a-z_]+)\.md')


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '_', (text or '').strip().lower()).strip('_')


def asset_exists(name):
    return os.path.isfile(os.path.join(ASSETS_DIR, name))


def glob_unique(pattern):
    """Return the sole basename matching pattern, else None (missing/ambiguous)."""
    hits = [os.path.basename(p) for p in glob.glob(os.path.join(ASSETS_DIR, pattern))]
    return hits[0] if len(hits) == 1 else None


def hero_town_class(lines):
    town = cls = None
    for l in lines:
        m = TOWN_RE.search(l)
        if m and town is None:
            town = m.group(1)
        if cls is None:
            if ':might:' in l:
                cls = 'might'
            elif ':magic:' in l:
                cls = 'magic'
    return town, cls


def resolve_target(category, slug, line, tab, in_specialty, spec_index, lines):
    """Compute the real asset filename for a placeholder, or None if unresolved."""
    if category == 'spells':
        name = f'spells-{slug}.webp'
        return name if asset_exists(name) else None

    if category == 'war_machines':
        name = f'war_machines-{slug}.webp'
        return name if asset_exists(name) else None

    if category == 'astrologers_proclaim':
        name = f'astrologers_proclaim-{slug}.webp'
        return name if asset_exists(name) else None

    if category == 'abilities':
        empowered = tab and 'empower' in tab.lower()
        name = f'abilities-{slug}-empowered.webp' if empowered else f'abilities-{slug}.webp'
        return name if asset_exists(name) else None

    if category == 'artifacts':
        # A few assets drop the "the" the page slug keeps (plate_of_the_dying_light).
        for s in (slug, slug.replace('_the_', '_')):
            hit = glob_unique(f'artifacts_*-{s}.webp')
            if hit:
                return hit
        return None

    if category == 'heroes':
        hslug = 'tarnum' if slug.startswith('tarnum') else slug
        town, cls = hero_town_class(lines)
        if town is None:
            return None
        if in_specialty:
            level = [1, 4, 7][min(spec_index - 1, 2)] if spec_index >= 1 else 1
            name = f'hero_specialties-{town}-{hslug}-{level}.webp'
            return name if asset_exists(name) else None
        # Portrait. A few cards file the art under the opposite class from the
        # glyph shown on the page (e.g. monere), so fall back to the other class.
        for c in ([cls] if cls else []) + ['might', 'magic']:
            name = f'heroes-{town}-{c}-{hslug}.webp'
            if asset_exists(name):
                return name
        return None

    if category == 'units':
        m = BLANK_TIER_RE.search(line)
        tier = m.group(1) if m else None
        label = (tab or '').lower()
        if not tier:
            return None
        if 'few' in label:
            return glob_unique(f'units-*-{tier}-{slug}*-few.webp')
        if 'pack' in label:
            return glob_unique(f'units-*-{tier}-{slug}*-pack.webp')
        if 'neutral' in label or tab is None:
            # Some neutral cards are printed with the singular slug (air_elemental
            # vs the air_elementals page), so fall back to dropping a trailing "s".
            for s in (slug, slug[:-1] if slug.endswith('s') else slug):
                name = f'units-neutral-{tier}-{s}.webp'
                if asset_exists(name):
                    return name
            return None
        # any other tab => creature bank / dwelling variant
        name = f'creature_banks-{slugify(tab)}-{slug}.webp'
        return name if asset_exists(name) else None

    return None


def process_file(path, unresolved):
    category = path.parts[1] if len(path.parts) > 1 else ''
    slug = path.stem
    lines = path.read_text(encoding='utf-8').split('\n')

    tab = None
    in_specialty = False
    spec_index = 0
    changed = 0
    new_lines = []

    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('## '):
            in_specialty = stripped.lower().startswith('## specialty')
        tm = TAB_RE.match(line)
        if tm:
            tab = tm.group(1)
            if in_specialty:
                spec_index += 1

        if IMG_RE.search(line):
            target = resolve_target(category, slug, line, tab, in_specialty,
                                    spec_index, lines)
            if target:
                line = IMG_RE.sub(f'../assets/{target}', line)
                changed += 1
            else:
                unresolved.append((str(path), lineno, IMG_RE.search(line).group(1)))
        new_lines.append(line)

    if changed:
        path.write_text('\n'.join(new_lines), encoding='utf-8')
        print(f"✓ {path}: {changed} replaced")
    return changed


def main(root):
    unresolved = []
    total_changed = 0
    total_files = 0

    for category in CATEGORIES:
        for path in sorted(Path(root, 'docs', category).glob('*.md')):
            if path.name.lower() == 'index.md':
                continue
            n = process_file(path, unresolved)
            if n:
                total_files += 1
                total_changed += n

    print(f"\n{'=' * 60}")
    print(f"Replaced {total_changed} placeholders across {total_files} files.")
    print(f"Unresolved (left untouched): {len(unresolved)}")
    if unresolved:
        print(f"{'-' * 60}")
        for f, ln, src in unresolved:
            print(f"  {f}:{ln}  {src}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    # allow passing either repo root or the docs dir
    if os.path.basename(os.path.normpath(root)) == 'docs':
        root = os.path.dirname(os.path.normpath(root)) or '.'
    main(root)
