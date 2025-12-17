#!/usr/bin/env python3
"""
Extract structured data from markdown files and store as JSON.
This script parses the markdown files for heroes, artifacts, spells, units, events, and abilities,
extracting structured data into JSON format.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional


class MarkdownExtractor:
    """Base class for extracting data from markdown files."""
    
    def __init__(self, docs_dir: Path):
        self.docs_dir = docs_dir
        
    def extract_title(self, content: str) -> str:
        """Extract the title from markdown content."""
        match = re.search(r'^# (.+)$', content, re.MULTILINE)
        return match.group(1).strip() if match else ""
    
    def extract_image(self, content: str, pattern: str) -> Optional[str]:
        """Extract image path from markdown content."""
        match = re.search(pattern, content)
        return match.group(1) if match else None
    
    def extract_section_content(self, content: str, section: str) -> Optional[str]:
        """Extract content under a specific section heading."""
        pattern = rf'^## {section}\s*$\n(.*?)(?=^## |\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else None
    
    def extract_list_items(self, content: str) -> List[str]:
        """Extract list items from markdown content."""
        items = re.findall(r'^\s*-\s+(.+)$', content, re.MULTILINE)
        return [item.strip() for item in items]
    
    def extract_centered_text(self, content: str, pattern: str) -> Optional[str]:
        """Extract text from centered paragraph."""
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else None


class HeroExtractor(MarkdownExtractor):
    """Extract hero data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract hero data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "image": self.extract_image(content, r'!\[.+?\]\((\.\./assets/heroes-.+?\.webp)\)'),
            "class": self.extract_hero_class(content),
            "town": self.extract_town(content),
            "stats": self.extract_stats(content),
            "starting_ability": self.extract_starting_ability(content),
            "specialty": self.extract_specialty(content),
            "notes": self.extract_notes(content),
            "appearances": self.extract_appearances(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_hero_class(self, content: str) -> Optional[str]:
        """Extract hero class (e.g., Knight, Wizard)."""
        match = re.search(r'\[:(?:might|magic):\s+([^\]]+)\]', content)
        return match.group(1).strip() if match else None
    
    def extract_town(self, content: str) -> Optional[str]:
        """Extract hero's town affiliation."""
        match = re.search(r'<p style="text-align: center;" markdown>\[([^\]]+)\]\(\.\./towns/[^\)]+\)</p>', content)
        return match.group(1).strip() if match else None
    
    def extract_stats(self, content: str) -> Dict[str, int]:
        """Extract hero statistics."""
        stats_match = re.search(
            r'\[:attack:\].*?&nbsp;(\d+).*?\[:defense:\].*?&nbsp;(\d+).*?\[:empower:\].*?&nbsp;(\d+).*?\[:skill:\].*?&nbsp;(\d+)',
            content, re.DOTALL
        )
        if stats_match:
            return {
                "attack": int(stats_match.group(1)),
                "defense": int(stats_match.group(2)),
                "power": int(stats_match.group(3)),
                "knowledge": int(stats_match.group(4))
            }
        return {}
    
    def extract_starting_ability(self, content: str) -> Optional[str]:
        """Extract starting ability."""
        match = re.search(r'<p style="text-align: center;" markdown>\[([^\]]+)\]\(\.\./abilities/[^\)]+\)</p>\s*___', content)
        return match.group(1).strip() if match else None
    
    def extract_specialty(self, content: str) -> Dict[str, Any]:
        """Extract specialty information."""
        specialty_section = self.extract_section_content(content, "Specialty")
        if not specialty_section:
            return {}
        
        # Extract specialty name from first tab
        name_match = re.search(r'=== "([^Ⅰ]+)', specialty_section)
        name = name_match.group(1).strip() if name_match else ""
        
        # Extract specialty images
        images = re.findall(r'!\[.+?\]\((\.\./assets/hero_specialties-.+?\.webp)\)', specialty_section)
        
        # Extract specialty levels table
        levels = {}
        table_match = re.search(r'\| Level \| Description \|\s*\n\|[:\-\s]+\|[:\-\s]+\|\s*\n((?:\|.*?(?:\n|$))+)', specialty_section, re.DOTALL)
        if table_match:
            table_rows = table_match.group(1)
            for row in re.finditer(r'\|\s*([ⅠⅣⅥ]+)\s*\|\s*(.+?)\s*\|(?:\n|$)', table_rows, re.DOTALL):
                level = row.group(1).strip()
                description = row.group(2).strip()
                # Clean up extra whitespace and newlines in description
                description = ' '.join(description.split())
                levels[level] = description
        
        return {
            "name": name,
            "images": images,
            "levels": levels
        }
    
    def extract_notes(self, content: str) -> List[str]:
        """Extract notes."""
        notes_section = self.extract_section_content(content, "Notes")
        if notes_section:
            return self.extract_list_items(notes_section)
        return []
    
    def extract_appearances(self, content: str) -> List[str]:
        """Extract scenario appearances."""
        appearances_section = self.extract_section_content(content, "Appearances As Player Hero")
        if appearances_section:
            return self.extract_list_items(appearances_section)
        return []
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class ArtifactExtractor(MarkdownExtractor):
    """Extract artifact data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract artifact data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "image": self.extract_image(content, r'!\[.+?\]\((\.\./assets/artifacts_.+?\.webp)\)'),
            "type": self.extract_artifact_type(content),
            "effect": self.extract_effect(content),
            "flavor_text": self.extract_flavor_text(content),
            "notes": self.extract_notes(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_artifact_type(self, content: str) -> Optional[str]:
        """Extract artifact type (e.g., Relic, Treasure)."""
        match = re.search(r'<p style="text-align: center;" markdown>\[([^\]]+Artifact[^\]]*)\]', content)
        return match.group(1).strip() if match else None
    
    def extract_effect(self, content: str) -> Optional[str]:
        """Extract artifact effect."""
        # The effect is in a centered paragraph after the artifact type but not in italics
        # Pattern: after "___", find centered paragraph without asterisks (italics)
        pattern = r'___\s*<p style="text-align: center;" markdown>([^*]+?)</p>'
        matches = re.findall(pattern, content, re.DOTALL)
        # Look for the effect paragraph (not the type)
        for match in matches:
            match_stripped = match.strip()
            # Skip if it's just a link to artifact type
            if not re.match(r'^\[.+?Artifact.*?\]\(.+?\)$', match_stripped):
                return match_stripped
        return None
    
    def extract_flavor_text(self, content: str) -> Optional[str]:
        """Extract flavor text (italicized text)."""
        match = re.search(r'<p style="text-align: center;" markdown>\*(.+?)\*</p>', content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def extract_notes(self, content: str) -> List[str]:
        """Extract notes."""
        notes_section = self.extract_section_content(content, "Notes")
        if notes_section:
            return self.extract_list_items(notes_section)
        return []
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class SpellExtractor(MarkdownExtractor):
    """Extract spell data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract spell data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "image": self.extract_image(content, r'!\[.+?\]\((\.\./assets/spells-.+?\.webp)\)'),
            "type": self.extract_spell_type(content),
            "effect": self.extract_effect(content),
            "notes": self.extract_notes(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_spell_type(self, content: str) -> Optional[str]:
        """Extract spell type (e.g., Basic Water Spell)."""
        # Try with link first
        match = re.search(r'<p style="text-align: center;" markdown>\[([^\]]+Spell)\]', content)
        if match:
            return match.group(1).strip()
        # Try without link (e.g., "Basic Spell")
        pattern = r'___\s*<p style="text-align: center;" markdown>([A-Z][^<:]+Spell)</p>'
        match = re.search(pattern, content)
        return match.group(1).strip() if match else None
    
    def extract_effect(self, content: str) -> Optional[str]:
        """Extract spell effect."""
        # Look for all centered paragraphs
        pattern = r'<p style="text-align: center;" markdown>(.+?)</p>'
        matches = re.findall(pattern, content, re.DOTALL)
        
        # For spells, the effect is the paragraph after the spell type
        # Skip any that look like spell type (either as link or plain text)
        for match in matches:
            match_stripped = match.strip()
            # Skip if it's a spell type link or just a spell type text (like "Basic Spell")
            if (not re.search(r'^\[.+?Spell\]', match_stripped) and 
                not re.match(r'^[A-Z][A-Za-z\s]+Spell$', match_stripped) and
                # Make sure it's not empty or too short
                len(match_stripped) > 20):
                return match_stripped
        return None
    
    def extract_notes(self, content: str) -> List[str]:
        """Extract notes."""
        notes_section = self.extract_section_content(content, "Notes")
        if notes_section:
            return self.extract_list_items(notes_section)
        return []
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class UnitExtractor(MarkdownExtractor):
    """Extract unit data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract unit data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "variants": self.extract_variants(content),
            "statistics": self.extract_unit_statistics(content),
            "notes": self.extract_notes(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_variants(self, content: str) -> List[str]:
        """Extract unit variants (Few, Pack, Neutral)."""
        variants = []
        for match in re.finditer(r'=== "([^"]+)"', content):
            variants.append(match.group(1))
        return variants
    
    def extract_unit_statistics(self, content: str) -> Dict[str, Any]:
        """Extract unit statistics table."""
        table_match = re.search(r'\| Statistics \|.*?\n\|.*?\n((?:\|.*?\n)+)', content, re.DOTALL)
        if not table_match:
            return {}
        
        stats = {}
        table_content = table_match.group(0)
        
        # Extract headers (variant names)
        header_match = re.search(r'\| Statistics \|(.*?)\|', table_content)
        if header_match:
            headers = [h.strip() for h in header_match.group(1).split('|') if h.strip()]
        else:
            return {}
        
        # Extract each row
        for row_match in re.finditer(r'\|\s*([^|]+?)\s*\|(.*?)\|(?:\n|$)', table_content):
            if 'Statistics' in row_match.group(1) or ':---' in row_match.group(1):
                continue
            
            stat_name = row_match.group(1).strip()
            values = [v.strip() for v in row_match.group(2).split('|')]
            
            if len(values) == len(headers):
                for i, header in enumerate(headers):
                    if header not in stats:
                        stats[header] = {}
                    stats[header][stat_name] = values[i]
        
        return stats
    
    def extract_notes(self, content: str) -> List[str]:
        """Extract notes."""
        notes_section = self.extract_section_content(content, "Notes")
        if notes_section:
            return self.extract_list_items(notes_section)
        return []
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class EventExtractor(MarkdownExtractor):
    """Extract event data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract event data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "image": self.extract_image(content, r'!\[.+?\]\((\.\./assets/events-.+?\.webp)\)'),
            "type": "Event",
            "effect": self.extract_effect(content),
            "flavor_text": self.extract_flavor_text(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_effect(self, content: str) -> Optional[str]:
        """Extract event effect."""
        pattern = r'___\s*<p style="text-align: center;" markdown>(.+?)</p>\s*___'
        matches = re.findall(pattern, content, re.DOTALL)
        if len(matches) >= 2:
            return matches[1].strip()
        return None
    
    def extract_flavor_text(self, content: str) -> Optional[str]:
        """Extract flavor text (italicized text)."""
        match = re.search(r'<p style="text-align: center;" markdown>\*(.+?)\*</p>', content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class AbilityExtractor(MarkdownExtractor):
    """Extract ability data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract ability data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "image": self.extract_image(content, r'!\[.+?\]\((\.\./assets/abilities-.+?\.webp)\)'),
            "type": "Ability",
            "effect": self.extract_effect(content),
            "expert_effect": self.extract_expert_effect(content),
            "heroes": self.extract_heroes_with_ability(content),
            "comes_with": self.extract_comes_with(content),
        }
        
        return data
    
    def extract_effect(self, content: str) -> Optional[str]:
        """Extract ability effect."""
        pattern = r'___\s*<p style="text-align: center;" markdown>(.+?)</p>\s*___'
        matches = re.findall(pattern, content, re.DOTALL)
        if len(matches) >= 2:
            return matches[1].strip()
        return None
    
    def extract_expert_effect(self, content: str) -> Optional[str]:
        """Extract expert effect."""
        pattern = r':expert:.*?<p style="text-align: center;" markdown>(.+?)</p>\s*___'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def extract_heroes_with_ability(self, content: str) -> List[str]:
        """Extract list of heroes with this starting ability."""
        heroes_section = self.extract_section_content(content, "Heroes With Starting Ability")
        if heroes_section:
            heroes = self.extract_list_items(heroes_section)
            return [re.sub(r'\[:(?:might|magic):\s+([^\]]+)\].*', r'\1', hero) for hero in heroes]
        return []
    
    def extract_comes_with(self, content: str) -> List[str]:
        """Extract expansion/content information."""
        comes_with_section = self.extract_section_content(content, "Comes With")
        if comes_with_section:
            items = self.extract_list_items(comes_with_section)
            return [re.sub(r'\[([^\]]+)\].*', r'\1', item) for item in items]
        return []


class StatisticExtractor(MarkdownExtractor):
    """Extract statistic data from markdown files."""
    
    def extract(self, filepath: Path) -> Dict[str, Any]:
        """Extract statistic data from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "name": self.extract_title(content),
            "variants": self.extract_stat_variants(content),
            "effects": self.extract_stat_effects(content),
        }
        
        return data
    
    def extract_stat_variants(self, content: str) -> List[str]:
        """Extract statistic variants (Regular, Empowered)."""
        variants = []
        for match in re.finditer(r'=== "([^"]+)"', content):
            variants.append(match.group(1))
        return variants
    
    def extract_stat_effects(self, content: str) -> Dict[str, Any]:
        """Extract statistic effects table."""
        table_match = re.search(r'\| Type \| Effect \|.*?\n\|.*?\n((?:\|.*?\n)+)', content, re.DOTALL)
        if not table_match:
            return {}
        
        effects = {}
        for row_match in re.finditer(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', table_match.group(1)):
            stat_type = row_match.group(1).strip()
            effect = row_match.group(2).strip()
            expert_effect = row_match.group(3).strip()
            effects[stat_type] = {
                "effect": effect,
                "expert_effect": expert_effect
            }
        
        return effects


def main():
    """Main extraction function."""
    # Get the base directory
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / "docs"
    data_dir = base_dir / "data"
    
    # Create data directories if they don't exist
    data_dir.mkdir(exist_ok=True)
    
    # Extract heroes
    print("Extracting heroes...")
    heroes_dir = docs_dir / "heroes"
    heroes_data_dir = data_dir / "heroes"
    heroes_data_dir.mkdir(exist_ok=True)
    
    hero_extractor = HeroExtractor(docs_dir)
    for md_file in heroes_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = hero_extractor.extract(md_file)
                json_file = heroes_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract artifacts
    print("\nExtracting artifacts...")
    artifacts_dir = docs_dir / "artifacts"
    artifacts_data_dir = data_dir / "artifacts"
    artifacts_data_dir.mkdir(exist_ok=True)
    
    artifact_extractor = ArtifactExtractor(docs_dir)
    for md_file in artifacts_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = artifact_extractor.extract(md_file)
                json_file = artifacts_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract spells
    print("\nExtracting spells...")
    spells_dir = docs_dir / "spells"
    spells_data_dir = data_dir / "spells"
    spells_data_dir.mkdir(exist_ok=True)
    
    spell_extractor = SpellExtractor(docs_dir)
    for md_file in spells_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = spell_extractor.extract(md_file)
                json_file = spells_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract units
    print("\nExtracting units...")
    units_dir = docs_dir / "units"
    units_data_dir = data_dir / "units"
    units_data_dir.mkdir(exist_ok=True)
    
    unit_extractor = UnitExtractor(docs_dir)
    for md_file in units_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = unit_extractor.extract(md_file)
                json_file = units_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract events
    print("\nExtracting events...")
    events_dir = docs_dir / "events"
    events_data_dir = data_dir / "events"
    events_data_dir.mkdir(exist_ok=True)
    
    event_extractor = EventExtractor(docs_dir)
    for md_file in events_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = event_extractor.extract(md_file)
                json_file = events_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract abilities
    print("\nExtracting abilities...")
    abilities_dir = docs_dir / "abilities"
    abilities_data_dir = data_dir / "abilities"
    abilities_data_dir.mkdir(exist_ok=True)
    
    ability_extractor = AbilityExtractor(docs_dir)
    for md_file in abilities_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = ability_extractor.extract(md_file)
                json_file = abilities_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    # Extract statistics
    print("\nExtracting statistics...")
    statistics_dir = docs_dir / "statistics"
    statistics_data_dir = data_dir / "statistics"
    statistics_data_dir.mkdir(exist_ok=True)
    
    statistic_extractor = StatisticExtractor(docs_dir)
    for md_file in statistics_dir.glob("*.md"):
        if md_file.name != "index.md":
            try:
                data = statistic_extractor.extract(md_file)
                json_file = statistics_data_dir / f"{md_file.stem}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Extracted: {md_file.name}")
            except Exception as e:
                print(f"  Error extracting {md_file.name}: {e}")
    
    print("\nExtraction complete!")


if __name__ == "__main__":
    main()
