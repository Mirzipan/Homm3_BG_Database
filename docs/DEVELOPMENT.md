# Development Guide

This document explains how the card data is structured and how to work with the data extraction and markdown generation system.

## Overview

The database uses a two-part system:

1. **Data Storage**: Card information is stored as structured JSON files in the `data/` directory
2. **Markdown Generation**: Markdown files in `docs/` are generated from templates and JSON data

This separation allows for:
- Easier data management and validation
- Consistent formatting across all cards
- Automated generation of translated content
- Easier bulk updates and corrections

## Directory Structure

```
Homm3_BG_Database/
├── data/                    # Structured data (JSON)
│   ├── heroes/             # Hero card data
│   ├── artifacts/          # Artifact card data
│   ├── spells/             # Spell card data
│   ├── units/              # Unit card data
│   ├── events/             # Event card data
│   ├── abilities/          # Ability card data
│   └── statistics/         # Statistic card data
├── templates/              # Markdown templates
│   ├── hero.md.template
│   ├── artifact.md.template
│   ├── spell.md.template
│   ├── unit.md.template
│   ├── event.md.template
│   ├── ability.md.template
│   └── statistic.md.template
├── tools/                  # Scripts
│   ├── extract_data.py    # Extract data from markdown files
│   └── generate_markdown.py # Generate markdown from data and templates
└── docs/                   # Generated markdown files
    ├── heroes/
    ├── artifacts/
    ├── spells/
    ├── units/
    ├── events/
    ├── abilities/
    └── statistics/
```

## Data Schema

### Hero Data

Hero data is stored in JSON format with the following structure:

```json
{
  "name": "Adelaide",
  "image": "../assets/heroes-castle-magic-adelaide.webp",
  "class": "Cleric",
  "town": "Castle",
  "stats": {
    "attack": 1,
    "defense": 0,
    "power": 2,
    "knowledge": 2
  },
  "starting_ability": "Wisdom",
  "specialty": {
    "name": "Frost Ring",
    "images": [
      "../assets/hero_specialties-castle-adelaide-1.webp",
      "../assets/hero_specialties-castle-adelaide-4.webp",
      "../assets/hero_specialties-castle-adelaide-7.webp"
    ],
    "levels": {
      "Ⅰ": ":instant: Discard 1 card. Target a space on the Combat board...",
      "Ⅳ": ":instant: Select 1 [Spell](../spells/index.md)...",
      "Ⅵ": ":instant: Discard 2 cards. Target a space on the Combat board..."
    }
  },
  "notes": [
    "**Ⅰ and Ⅵ** - The :damage: from Frost Ring also applies to friendly units.",
    "These specialties can be played as *instant* effects at any time during Combat..."
  ],
  "appearances": [],
  "comes_with": [
    "Tower Expansion"
  ]
}
```

### Artifact Data

```json
{
  "name": "Angel Wings",
  "image": "../assets/artifacts_relic-angel_wings.webp",
  "type": "Relic Artifact",
  "effect": ":effect_map: Chosen [Hero](../heroes/index.md) gain +1 :movement:...",
  "flavor_text": "Not really wanting to know where the Angel...",
  "notes": [
    "After playing Angel Wings, the hero may move through borders..."
  ],
  "comes_with": [
    "Core Game"
  ]
}
```

### Spell Data

```json
{
  "name": "Bless",
  "image": "../assets/spells-bless.webp",
  "type": "Basic Water Spell",
  "effect": ":instant: The selected :unit_ground: or :unit_flying: unit...",
  "notes": [
    "If no Attack die is rolled during the attack..."
  ],
  "comes_with": [
    "Core Game"
  ]
}
```

### Unit Data

```json
{
  "name": "Archangels",
  "variants": ["Few", "Pack", "Neutral"],
  "statistics": {
    "Few": {
      "Town": "[Castle](../towns/castle.md)",
      "Tier": ":golden:",
      "Type": "[:unit_flying:](../keywords/flying_unit.md)",
      ":attack:": "6",
      ":defense:": "3",
      ":health_points:": "8",
      ":initiative:": "12",
      "Cost": "20 :gold:<br>1 :valuables:",
      "Abilities": ":unit_passive: When combat begins, draw 1 card."
    },
    ...
  },
  "notes": [
    "**Pack** - The passive ability can be used at the moment..."
  ],
  "comes_with": [
    "Core Game"
  ]
}
```

## Working with the System

### Extracting Data from Existing Markdown

If you need to extract data from existing markdown files (e.g., after manual edits):

```bash
python3 tools/extract_data.py
```

This will:
- Parse all markdown files in `docs/`
- Extract structured data
- Save JSON files to `data/`

### Generating Markdown from Data

To generate markdown files from JSON data and templates:

```bash
python3 tools/generate_markdown.py
```

This will:
- Read all JSON files from `data/`
- Apply templates from `templates/`
- Generate markdown files in `docs/`

### Adding a New Card

1. Create a JSON file in the appropriate `data/` subdirectory
2. Fill in all required fields following the schema
3. Run `python3 tools/generate_markdown.py` to generate the markdown file

Example:

```bash
# Create new hero data file
cat > data/heroes/new_hero.json << 'EOF'
{
  "name": "New Hero",
  "image": "../assets/heroes-castle-might-new_hero.webp",
  "class": "Knight",
  "town": "Castle",
  "stats": {
    "attack": 2,
    "defense": 2,
    "power": 1,
    "knowledge": 1
  },
  "starting_ability": "Leadership",
  "specialty": {
    "name": "Power Strike",
    "images": [
      "../assets/hero_specialties-castle-new_hero-1.webp",
      "../assets/hero_specialties-castle-new_hero-4.webp",
      "../assets/hero_specialties-castle-new_hero-7.webp"
    ],
    "levels": {
      "Ⅰ": ":instant: Your selected [unit](../units/index.md) gains +1 :attack:",
      "Ⅳ": ":instant: Your selected [unit](../units/index.md) gains +2 :attack:",
      "Ⅵ": ":instant: Your selected [unit](../units/index.md) gains +3 :attack:"
    }
  },
  "notes": [],
  "appearances": [],
  "comes_with": [
    "Core Game"
  ]
}
EOF

# Generate markdown
python3 tools/generate_markdown.py
```

### Updating an Existing Card

1. Edit the JSON file in the `data/` directory
2. Run `python3 tools/generate_markdown.py` to regenerate the markdown file

**Note**: Do not edit the markdown files directly in `docs/` as they will be overwritten!

### Modifying Templates

Templates are stored in the `templates/` directory and use a simple token replacement system:

- `{{token}}` - Replaced with the value of `token` from the data
- `{{#section}}...{{/section}}` - Conditional block, rendered if `section` exists
- `{{#list}}...{{/list}}` - Loop over items in `list`

Example template snippet:

```markdown
# {{name}}

![{{name}}]({{image}}){ width="340" align=right }

## Stats

- Attack: {{stats.attack}}
- Defense: {{stats.defense}}

{{#notes}}
## Notes

{{#notes_list}}
- {{.}}
{{/notes_list}}
{{/notes}}
```

## Best Practices

1. **Always work with JSON data first**: Make changes to the JSON files, not the markdown files
2. **Validate your JSON**: Use a JSON validator before generating markdown
3. **Keep templates consistent**: Ensure all cards of the same type use the same template structure
4. **Use descriptive keys**: Make JSON field names clear and consistent
5. **Document special cases**: Add notes to cards that have unusual mechanics or interactions

## Troubleshooting

### Markdown file not updating

1. Make sure you edited the JSON file, not the markdown file
2. Run `python3 tools/generate_markdown.py` to regenerate
3. Check for errors in the console output

### Missing fields in generated markdown

1. Verify the field exists in the JSON data
2. Check the template includes the field
3. Ensure the template syntax is correct (e.g., `{{field}}` not `{field}`)

### JSON parsing errors

1. Validate your JSON using a linter
2. Check for missing commas, quotes, or brackets
3. Ensure all strings are properly escaped

## Future Enhancements

Potential improvements to the system:

- JSON Schema validation
- Automated testing of generated markdown
- Linting and formatting tools for JSON data
- Support for multiple languages/translations
- Web-based editor for card data
- Automated image validation
