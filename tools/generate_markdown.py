#!/usr/bin/env python3
"""
Generate markdown files from JSON data and templates.
This script reads the extracted JSON data and generates markdown files
using templates with token replacement.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional


# Constants
MAX_CONSECUTIVE_NEWLINES = 2
MIGHT_HERO_CLASSES = ['Knight', 'Ranger', 'Death Knight', 'Beastmaster', 'Barbarian', 'Overlord', 'Planeswalker', 'Alchemist']
SPELL_SCHOOLS = {
    'Water': ('School of Water Magic', 'school_of_water_magic'),
    'Fire': ('School of Fire Magic', 'school_of_fire_magic'),
    'Air': ('School of Air Magic', 'school_of_air_magic'),
    'Earth': ('School of Earth Magic', 'school_of_earth_magic'),
}


def slugify(text: str) -> str:
    """Convert text to slug format."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '_', text)
    return text


def render_template(template: str, data: Dict[str, Any]) -> str:
    """
    Simple template renderer that replaces {{tokens}} with values.
    Supports basic conditionals and loops.
    """
    result = template
    
    # Handle conditional blocks {{#key}} ... {{/key}}
    def replace_conditional(match):
        key = match.group(1)
        content = match.group(2)
        
        # Get the value from data
        value = data.get(key)
        
        # If value exists and is truthy, render the content
        if value:
            if isinstance(value, list):
                # If it's a list, render for each item
                if key.endswith('_list'):
                    rendered = []
                    for item in value:
                        item_content = content
                        if isinstance(item, dict):
                            item_content = render_template(content, item)
                        else:
                            # For simple values, replace {{.}} with the value
                            item_content = content.replace('{{.}}', str(item))
                        rendered.append(item_content)
                    return ''.join(rendered)
                else:
                    # Render the content once with the list data
                    rendered = []
                    for item in value:
                        if isinstance(item, dict):
                            rendered.append(render_template(content, item))
                        else:
                            rendered.append(content.replace('{{.}}', str(item)))
                    return ''.join(rendered)
            elif isinstance(value, str):
                # For strings, replace {{.}} with the value
                return content.replace('{{.}}', value)
            else:
                # Render the content as-is
                return render_template(content, data)
        return ''
    
    # Process conditional blocks
    result = re.sub(r'\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}', replace_conditional, result, flags=re.DOTALL)
    
    # Handle simple token replacement {{key}}
    def replace_token(match):
        key = match.group(1)
        
        # Handle nested keys like stats.attack
        if '.' in key:
            keys = key.split('.')
            value = data
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k)
                else:
                    return ''
            return str(value) if value is not None else ''
        
        value = data.get(key)
        return str(value) if value is not None else ''
    
    result = re.sub(r'\{\{([^#/\}]+)\}\}', replace_token, result)
    
    return result


class MarkdownGenerator:
    """Base class for generating markdown files from JSON data."""
    
    def __init__(self, templates_dir: Path, data_dir: Path, output_dir: Path):
        self.templates_dir = templates_dir
        self.data_dir = data_dir
        self.output_dir = output_dir
    
    def load_template(self, template_name: str) -> str:
        """Load a template file."""
        template_path = self.templates_dir / template_name
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def load_data(self, data_file: Path) -> Dict[str, Any]:
        """Load JSON data file."""
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_markdown(self, content: str, output_file: Path):
        """Save generated markdown to file."""
        # Clean up excessive newlines
        content = re.sub(rf'\n{{{MAX_CONSECUTIVE_NEWLINES + 1},}}', '\n' * MAX_CONSECUTIVE_NEWLINES, content)
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)


class HeroGenerator(MarkdownGenerator):
    """Generate hero markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for a hero."""
        data = self.load_data(json_file)
        template = self.load_template('hero.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Determine class icon (might or magic)
        class_name = data.get('class', '')
        template_data['class_icon'] = 'might' if class_name in MIGHT_HERO_CLASSES else 'magic'
        
        # Town slug
        template_data['town_slug'] = slugify(data.get('town', ''))
        
        # Starting ability slug
        template_data['starting_ability_slug'] = slugify(data.get('starting_ability', ''))
        
        # Specialty tabs
        specialty = data.get('specialty', {})
        if specialty:
            specialty_name = specialty.get('name', '')
            images = specialty.get('images', [])
            levels_dict = specialty.get('levels', {})
            
            # Create tabs for each specialty level
            tabs = []
            level_names = ['Ⅰ', 'Ⅳ', 'Ⅵ']
            for i, level in enumerate(level_names):
                if i < len(images):
                    tabs.append({
                        'name': specialty_name,
                        'level': level,
                        'image': images[i]
                    })
            template_data['specialty_tabs'] = tabs
            
            # Create specialty levels list
            specialty_levels = []
            for level, description in levels_dict.items():
                specialty_levels.append({
                    'level': level,
                    'description': description
                })
            template_data['specialty_levels'] = specialty_levels
        
        # Notes
        if data.get('notes'):
            template_data['notes'] = True
            template_data['notes_list'] = data['notes']
        
        # Appearances
        if data.get('appearances'):
            template_data['appearances'] = True
            template_data['appearances_list'] = data['appearances']
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class ArtifactGenerator(MarkdownGenerator):
    """Generate artifact markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for an artifact."""
        data = self.load_data(json_file)
        template = self.load_template('artifact.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Type slug
        artifact_type = data.get('type', '')
        template_data['type_slug'] = slugify(artifact_type.replace(' ', '_'))
        
        # Notes
        if data.get('notes'):
            template_data['notes'] = True
            template_data['notes_list'] = data['notes']
        
        # Flavor text
        if data.get('flavor_text'):
            template_data['flavor_text'] = data['flavor_text']
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class SpellGenerator(MarkdownGenerator):
    """Generate spell markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for a spell."""
        data = self.load_data(json_file)
        template = self.load_template('spell.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Extract school from type
        spell_type = data.get('type', '')
        school_found = False
        for school_keyword, (school_name, school_slug) in SPELL_SCHOOLS.items():
            if school_keyword in spell_type:
                template_data['school_name'] = school_name
                template_data['school_slug'] = school_slug
                school_found = True
                break
        
        if not school_found:
            template_data['school_name'] = 'List of Spells'
            template_data['school_slug'] = 'index'
        
        # Notes
        if data.get('notes'):
            template_data['notes'] = True
            template_data['notes_list'] = data['notes']
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class UnitGenerator(MarkdownGenerator):
    """Generate unit markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for a unit."""
        data = self.load_data(json_file)
        template = self.load_template('unit.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Variants
        variants = data.get('variants', [])
        template_data['variants'] = [
            {'name': variant, 'variant_name': f"{variant} {data['name']}", 'image': ''}
            for variant in variants
        ]
        
        # Statistics table
        statistics = data.get('statistics', {})
        if statistics:
            headers = list(statistics.keys())
            template_data['stat_headers'] = ' | '.join(headers)
            template_data['stat_header_align'] = ' | '.join([':---:'] * len(headers))
            
            # Get all stat row names
            stat_names = set()
            for variant_stats in statistics.values():
                stat_names.update(variant_stats.keys())
            
            # Create rows
            rows = []
            for stat_name in sorted(stat_names):
                values = [statistics[header].get(stat_name, '') for header in headers]
                rows.append({
                    'row_name': stat_name,
                    'values': ' | '.join(str(v) for v in values)
                })
            template_data['stat_rows'] = rows
        
        # Notes
        if data.get('notes'):
            template_data['notes'] = True
            template_data['notes_list'] = data['notes']
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class EventGenerator(MarkdownGenerator):
    """Generate event markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for an event."""
        data = self.load_data(json_file)
        template = self.load_template('event.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Flavor text
        if data.get('flavor_text'):
            template_data['flavor_text'] = data['flavor_text']
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class AbilityGenerator(MarkdownGenerator):
    """Generate ability markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for an ability."""
        data = self.load_data(json_file)
        template = self.load_template('ability.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Expert effect
        if data.get('expert_effect'):
            template_data['expert_effect'] = data['expert_effect']
        
        # Heroes
        heroes = data.get('heroes', [])
        if heroes:
            template_data['heroes'] = True
            template_data['heroes_list'] = [
                {'name': hero, 'icon': 'might', 'slug': slugify(hero)}
                for hero in heroes
            ]
        
        # Comes with
        comes_with = data.get('comes_with', [])
        template_data['comes_with_list'] = [
            {'text': f"[{item}](../content/{slugify(item)}.md)", 'name': item, 'slug': slugify(item)}
            for item in comes_with
        ]
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


class StatisticGenerator(MarkdownGenerator):
    """Generate statistic markdown files."""
    
    def generate(self, json_file: Path) -> str:
        """Generate markdown for a statistic."""
        data = self.load_data(json_file)
        template = self.load_template('statistic.md.template')
        
        # Prepare data for template
        template_data = data.copy()
        
        # Variants
        variants = data.get('variants', [])
        template_data['variants'] = [
            {'name': variant, 'variant_name': f"{variant} {data['name']}", 'image': ''}
            for variant in variants
        ]
        
        # Effects
        effects = data.get('effects', {})
        if effects:
            effects_list = []
            for effect_type, effect_data in effects.items():
                effects_list.append({
                    'type': effect_type,
                    'effect': effect_data.get('effect', ''),
                    'expert_effect': effect_data.get('expert_effect', '')
                })
            template_data['effects'] = effects_list
        
        # Render template
        markdown = render_template(template, template_data)
        
        # Save to output
        output_file = self.output_dir / f"{json_file.stem}.md"
        self.save_markdown(markdown, output_file)
        
        return markdown


def main():
    """Main generation function."""
    # Get the base directory
    base_dir = Path(__file__).parent.parent
    templates_dir = base_dir / "templates"
    data_dir = base_dir / "data"
    docs_dir = base_dir / "docs"
    
    # Generate heroes
    print("Generating heroes...")
    heroes_data_dir = data_dir / "heroes"
    heroes_output_dir = docs_dir / "heroes"
    
    hero_generator = HeroGenerator(templates_dir, heroes_data_dir, heroes_output_dir)
    for json_file in heroes_data_dir.glob("*.json"):
        try:
            hero_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate artifacts
    print("\nGenerating artifacts...")
    artifacts_data_dir = data_dir / "artifacts"
    artifacts_output_dir = docs_dir / "artifacts"
    
    artifact_generator = ArtifactGenerator(templates_dir, artifacts_data_dir, artifacts_output_dir)
    for json_file in artifacts_data_dir.glob("*.json"):
        try:
            artifact_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate spells
    print("\nGenerating spells...")
    spells_data_dir = data_dir / "spells"
    spells_output_dir = docs_dir / "spells"
    
    spell_generator = SpellGenerator(templates_dir, spells_data_dir, spells_output_dir)
    for json_file in spells_data_dir.glob("*.json"):
        try:
            spell_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate units
    print("\nGenerating units...")
    units_data_dir = data_dir / "units"
    units_output_dir = docs_dir / "units"
    
    unit_generator = UnitGenerator(templates_dir, units_data_dir, units_output_dir)
    for json_file in units_data_dir.glob("*.json"):
        try:
            unit_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate events
    print("\nGenerating events...")
    events_data_dir = data_dir / "events"
    events_output_dir = docs_dir / "events"
    
    event_generator = EventGenerator(templates_dir, events_data_dir, events_output_dir)
    for json_file in events_data_dir.glob("*.json"):
        try:
            event_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate abilities
    print("\nGenerating abilities...")
    abilities_data_dir = data_dir / "abilities"
    abilities_output_dir = docs_dir / "abilities"
    
    ability_generator = AbilityGenerator(templates_dir, abilities_data_dir, abilities_output_dir)
    for json_file in abilities_data_dir.glob("*.json"):
        try:
            ability_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    # Generate statistics
    print("\nGenerating statistics...")
    statistics_data_dir = data_dir / "statistics"
    statistics_output_dir = docs_dir / "statistics"
    
    statistic_generator = StatisticGenerator(templates_dir, statistics_data_dir, statistics_output_dir)
    for json_file in statistics_data_dir.glob("*.json"):
        try:
            statistic_generator.generate(json_file)
            print(f"  Generated: {json_file.stem}.md")
        except Exception as e:
            print(f"  Error generating {json_file.name}: {e}")
    
    print("\nGeneration complete!")


if __name__ == "__main__":
    main()
