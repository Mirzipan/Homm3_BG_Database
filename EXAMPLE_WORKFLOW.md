# Example Workflow: Adding and Updating Cards

This document provides step-by-step examples of common workflows when working with the card database.

## Example 1: Adding a New Hero Card

Let's add a new hero called "Maximus" to the database.

### Step 1: Create the JSON data file

Create `data/heroes/maximus.json`:

```json
{
  "name": "Maximus",
  "image": "../assets/heroes-castle-might-maximus.webp",
  "class": "Knight",
  "town": "Castle",
  "stats": {
    "attack": 3,
    "defense": 1,
    "power": 1,
    "knowledge": 1
  },
  "starting_ability": "Offense",
  "specialty": {
    "name": "Charge",
    "images": [
      "../assets/hero_specialties-castle-maximus-1.webp",
      "../assets/hero_specialties-castle-maximus-4.webp",
      "../assets/hero_specialties-castle-maximus-7.webp"
    ],
    "levels": {
      "Ⅰ": ":instant: Your selected [unit](../units/index.md) gains +1 :attack: for this combat.",
      "Ⅳ": ":instant: Your selected [unit](../units/index.md) gains +2 :attack: and +1 :initiative: for this combat.",
      "Ⅵ": ":instant: Your selected [unit](../units/index.md) gains +3 :attack: and +2 :initiative: for this combat."
    }
  },
  "notes": [
    "The bonus applies immediately and lasts until the end of the current combat."
  ],
  "appearances": [],
  "comes_with": [
    "Castle Expansion"
  ]
}
```

### Step 2: Generate the markdown file

```bash
python3 tools/generate_markdown.py
```

This creates `docs/heroes/maximus.md` with properly formatted markdown.

### Step 3: Verify and commit

```bash
# Check the generated file
cat docs/heroes/maximus.md

# Stage and commit both files
git add data/heroes/maximus.json docs/heroes/maximus.md
git commit -m "Add new hero: Maximus"
```

## Example 2: Updating an Existing Card

Let's say we need to update Adelaide's specialty description for level Ⅵ.

### Step 1: Edit the JSON file

Edit `data/heroes/adelaide.json`:

```bash
nano data/heroes/adelaide.json
```

Find the `"Ⅵ"` level in the specialty and update the description.

### Step 2: Regenerate the markdown

```bash
python3 tools/generate_markdown.py
```

Or use the convenience script:

```bash
./tools/regenerate_all.sh
```

### Step 3: Review and commit

```bash
# See what changed
git diff docs/heroes/adelaide.md

# If it looks good, commit
git add data/heroes/adelaide.json docs/heroes/adelaide.md
git commit -m "Update Adelaide specialty level Ⅵ description"
```

## Example 3: Bulk Update - Changing Expansion Names

Let's say we need to rename "Tower Expansion" to "Tower & Dungeon Expansion" across all cards.

### Step 1: Update all JSON files

Use `jq` to update all files:

```bash
# For heroes
for file in data/heroes/*.json; do
  jq '.comes_with = [if .comes_with[] == "Tower Expansion" then "Tower & Dungeon Expansion" else .comes_with[] end]' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
done

# Repeat for other card types...
```

Or use a Python script:

```python
import json
from pathlib import Path

def update_expansion_name(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    if 'comes_with' in data:
        data['comes_with'] = [
            "Tower & Dungeon Expansion" if x == "Tower Expansion" else x
            for x in data['comes_with']
        ]
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Process all card types
for card_type in ['heroes', 'artifacts', 'spells', 'units', 'events', 'abilities']:
    for json_file in Path(f'data/{card_type}').glob('*.json'):
        update_expansion_name(json_file)
        print(f"Updated {json_file}")
```

### Step 2: Regenerate all markdown files

```bash
python3 tools/generate_markdown.py
```

### Step 3: Review and commit

```bash
# See what changed
git diff data/ docs/

# Commit everything
git add data/ docs/
git commit -m "Rename Tower Expansion to Tower & Dungeon Expansion"
```

## Example 4: Fixing a Typo in Multiple Cards

Let's fix a common typo in notes across multiple spell cards.

### Step 1: Find affected files

```bash
# Find all spell JSON files with the typo
grep -r "attck" data/spells/*.json
```

### Step 2: Fix using sed or a script

```bash
# Use sed to fix in all files
for file in data/spells/*.json; do
  sed -i 's/attck/attack/g' "$file"
done
```

Or more carefully with Python:

```python
import json
from pathlib import Path

def fix_typo(json_file):
    with open(json_file, 'r') as f:
        content = f.read()
    
    if 'attck' in content:
        content = content.replace('attck', 'attack')
        
        with open(json_file, 'w') as f:
            f.write(content)
        
        return True
    return False

fixed_count = 0
for json_file in Path('data/spells').glob('*.json'):
    if fix_typo(json_file):
        print(f"Fixed typo in {json_file}")
        fixed_count += 1

print(f"\nFixed {fixed_count} files")
```

### Step 3: Regenerate and commit

```bash
python3 tools/generate_markdown.py
git add data/spells/ docs/spells/
git commit -m "Fix typo: attck -> attack in spell descriptions"
```

## Example 5: Extracting Data from Manually Edited Markdown

If someone accidentally edited a markdown file directly instead of the JSON:

### Step 1: Run the extractor

```bash
python3 tools/extract_data.py
```

This will parse all markdown files and update the JSON files.

### Step 2: Review the changes

```bash
# Check what changed in the JSON files
git diff data/

# Make sure the extraction worked correctly
```

### Step 3: Regenerate markdown to ensure consistency

```bash
python3 tools/generate_markdown.py
```

### Step 4: Commit

```bash
git add data/ docs/
git commit -m "Extract data from manually edited markdown files"
```

## Tips and Best Practices

### Always Edit JSON First

**Do this:**
```bash
nano data/heroes/adelaide.json
python3 tools/generate_markdown.py
```

**Don't do this:**
```bash
nano docs/heroes/adelaide.md  # Will be overwritten!
```

### Test Locally Before Committing

```bash
# Generate markdown
python3 tools/generate_markdown.py

# Check the output
git diff docs/

# Only commit if it looks correct
git add data/ docs/
git commit -m "Your change description"
```

### Use Version Control Effectively

```bash
# Create a branch for your changes
git checkout -b add-new-cards

# Make your changes
# ... edit JSON files ...
python3 tools/generate_markdown.py

# Review
git diff

# Commit
git add data/ docs/
git commit -m "Add new hero cards"

# Push and create pull request
git push origin add-new-cards
```

### Validate JSON Before Generating

```bash
# Check if JSON is valid
python3 -m json.tool data/heroes/new_hero.json > /dev/null && echo "Valid JSON" || echo "Invalid JSON"
```

### Keep Data and Docs in Sync

Always commit both `data/` and `docs/` changes together:

```bash
# Good
git add data/heroes/adelaide.json docs/heroes/adelaide.md
git commit -m "Update Adelaide"

# Bad - out of sync
git add data/heroes/adelaide.json
git commit -m "Update Adelaide data"
# (forgot to regenerate and commit markdown)
```

## Troubleshooting

### "My changes aren't showing up in the markdown"

1. Make sure you edited the JSON file, not the markdown file
2. Run `python3 tools/generate_markdown.py`
3. Check that the script completed without errors

### "The generator created weird formatting"

1. Check your JSON for syntax errors: `python3 -m json.tool data/heroes/yourfile.json`
2. Verify field values don't contain unexpected characters
3. Look at similar cards' JSON for reference

### "I accidentally edited markdown instead of JSON"

1. Run `python3 tools/extract_data.py` to extract changes back to JSON
2. Review the extracted JSON to ensure it's correct
3. Run `python3 tools/generate_markdown.py` to regenerate with correct formatting

## Additional Resources

- [DATA_README.md](DATA_README.md) - System overview and quick reference
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) - Detailed technical documentation
- [JSON Schema](https://json-schema.org/) - Learn about JSON schema validation
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) - Documentation theme in use
