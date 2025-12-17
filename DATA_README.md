# Card Data Management System

This repository uses a data-driven approach to manage card information for the Heroes of Might & Magic III: The Board Game database.

## Quick Start

### Extract data from existing markdown files:
```bash
python3 tools/extract_data.py
```

### Generate markdown files from data:
```bash
python3 tools/generate_markdown.py
```

## System Overview

The card database is split into two main components:

1. **Structured Data** (`data/` directory)
   - All card information stored as JSON files
   - One JSON file per card
   - Organized by card type (heroes, artifacts, spells, units, events, abilities, statistics)

2. **Markdown Templates** (`templates/` directory)
   - Templates define the structure of generated markdown files
   - One template per card type
   - Use token replacement for dynamic content

## Why This Approach?

### Benefits

- **Data Integrity**: Centralized data storage makes it easier to validate and maintain consistency
- **Bulk Operations**: Update multiple cards at once by modifying JSON files
- **Automation**: Generate markdown automatically from structured data
- **Translation Support**: Structured data can be easily translated and regenerated
- **Version Control**: JSON diffs are clearer than markdown diffs
- **Validation**: JSON schema validation ensures data quality

### Workflow

```
┌─────────────────┐
│  Edit JSON Data │
│   in data/      │
└────────┬────────┘
         │
         v
┌──────────────────────────┐
│  Run generate_markdown.py │
│                          │
│  Reads: data/*.json      │
│  Uses: templates/*.template│
└────────┬─────────────────┘
         │
         v
┌─────────────────────┐
│ Generated Markdown  │
│    in docs/         │
└─────────────────────┘
         │
         v
┌─────────────────────┐
│  MkDocs renders     │
│  to website         │
└─────────────────────┘
```

## Directory Structure

```
.
├── data/                       # Source of truth for all card data
│   ├── heroes/                 # 65 hero cards
│   ├── artifacts/              # 73 artifact cards
│   ├── spells/                 # 54 spell cards
│   ├── units/                  # 95 unit cards
│   ├── events/                 # 21 event cards
│   ├── abilities/              # 28 ability cards
│   └── statistics/             # 4 statistic cards
│
├── templates/                  # Markdown templates with tokens
│   ├── hero.md.template
│   ├── artifact.md.template
│   ├── spell.md.template
│   ├── unit.md.template
│   ├── event.md.template
│   ├── ability.md.template
│   └── statistic.md.template
│
├── tools/                      # Scripts for data management
│   ├── extract_data.py        # Extract JSON from existing markdown
│   └── generate_markdown.py   # Generate markdown from JSON + templates
│
└── docs/                       # Generated markdown files (do not edit directly!)
    ├── heroes/
    ├── artifacts/
    ├── spells/
    ├── units/
    ├── events/
    ├── abilities/
    └── statistics/
```

## Common Tasks

### Adding a New Card

1. Create a new JSON file in the appropriate `data/` subdirectory:
   ```bash
   # Example: Adding a new hero
   nano data/heroes/my_new_hero.json
   ```

2. Fill in the card data using the appropriate schema (see DEVELOPMENT.md)

3. Generate the markdown file:
   ```bash
   python3 tools/generate_markdown.py
   ```

4. Commit both the JSON and generated markdown:
   ```bash
   git add data/heroes/my_new_hero.json docs/heroes/my_new_hero.md
   git commit -m "Add new hero: My New Hero"
   ```

### Updating an Existing Card

1. Edit the JSON file:
   ```bash
   nano data/heroes/adelaide.json
   ```

2. Regenerate the markdown:
   ```bash
   python3 tools/generate_markdown.py
   ```

3. Commit the changes:
   ```bash
   git add data/heroes/adelaide.json docs/heroes/adelaide.md
   git commit -m "Update Adelaide hero card"
   ```

### Bulk Update Cards

Use `jq` or a Python script to modify multiple JSON files at once:

```bash
# Example: Update all heroes from a specific expansion
for file in data/heroes/*.json; do
  jq '.comes_with = ["Updated Expansion"]' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
done

# Regenerate all markdown
python3 tools/generate_markdown.py
```

### Extract Data from Modified Markdown

If you've manually edited markdown files and want to extract the data back to JSON:

```bash
python3 tools/extract_data.py
```

**Warning**: This will overwrite existing JSON files. Make sure to back them up if needed!

## Template System

Templates use a simple token replacement syntax:

### Basic Tokens
```markdown
{{name}}          # Replaced with the card name
{{stats.attack}}  # Access nested properties with dot notation
```

### Conditional Blocks
```markdown
{{#notes}}
## Notes
{{#notes_list}}
- {{.}}
{{/notes_list}}
{{/notes}}
```

This block is only rendered if `notes` exists in the data.

### Lists
```markdown
{{#comes_with_list}}
- [{{.}}](../content/{{slug}}.md)
{{/comes_with_list}}
```

Iterates over each item in `comes_with_list` and replaces `{{.}}` with the current item.

## Data Validation

To ensure data quality, follow these guidelines:

1. **Required Fields**: Every card type has required fields. Check DEVELOPMENT.md for schemas.
2. **Consistent Formatting**: Use the same format for similar fields across cards
3. **Valid References**: Ensure all links point to existing files
4. **Image Paths**: Verify all image paths are correct and relative
5. **Special Characters**: Properly escape special characters in JSON strings

## Tips and Best Practices

### For Data Editors

- **Edit JSON, not Markdown**: Always edit the JSON files in `data/`, not the markdown files in `docs/`
- **Use a JSON editor**: Tools like VS Code with JSON extensions can validate syntax as you type
- **Test locally**: Run `generate_markdown.py` locally before committing to verify changes
- **Check diffs**: Review the generated markdown diff to ensure your JSON changes produce the expected output

### For Developers

- **Template changes affect all cards**: Modifying a template will regenerate all cards of that type
- **Keep extraction in sync**: If you change the markdown format, update `extract_data.py` accordingly
- **Document schema changes**: Update DEVELOPMENT.md when adding new fields to the data schema
- **Preserve original data**: The `data/` directory is the source of truth; don't lose it!

## Troubleshooting

### "File not found" errors during generation

- Check that all JSON files are valid and properly formatted
- Verify template files exist in the `templates/` directory
- Ensure output directories exist (they're created automatically)

### Generated markdown looks wrong

- Verify the JSON data is correct
- Check the template for the card type
- Look for syntax errors in the template (mismatched `{{` or missing `}}`)

### Extraction doesn't capture all data

- The extractor uses regex patterns to parse markdown
- Complex markdown formatting may not be fully captured
- Consider manually creating JSON for new cards instead of extracting

## Contributing

When contributing card data:

1. **Follow the schema**: Use the correct data structure for each card type
2. **Validate before committing**: Run `generate_markdown.py` and check the output
3. **Commit both files**: Always commit both the JSON file and generated markdown together
4. **Write clear commit messages**: Describe what card was added or changed

## Getting Help

- See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed documentation
- Check existing JSON files for examples
- Open an issue if you encounter problems with the scripts

## License

The data extraction and generation scripts are part of the Homm3_BG_Database project.
See the main README.md for license information.
