<div align="center">
  <h1>Heroes of Might & Magic III: The Board Game<br>Cards Database</h1>

  <p align="center">
    <img src="https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white">
    <a href="https://discord.gg/Y4uM9pPWF6"><img src="https://dcbadge.limes.pink/api/server/Y4uM9pPWF6"></a>
  </p>

  <h1><a href="https://homm3bg.wiki/">👉 GO TO THE WEBSITE 👈</a></h1>
</div>

## ⚔️ What Is This?
A simple collection of cards contained within the Heroes of Might and Magic 3: The Board Game, that also offers extra explanations for how some cards work or interact with others.

Every now and then I want to see what some cards do, either while theorycrafting about what to play, or even during play, when I want to check or reference something. This database is meant to provide an easy way to find any card contained within the game, including a visual reference and extra information where necessary or applicable.

## 📊 Data-Driven Architecture

This database uses a modern data-driven approach where card information is stored as structured JSON files and markdown documentation is generated from templates. This makes it easier to:

- **Update multiple cards** at once with bulk operations
- **Maintain consistency** across all card documentation
- **Validate data** before publishing
- **Track changes** with clear diffs in version control
- **Support translations** by regenerating from the same data

### For Contributors

- **Quick Start**: See [DATA_README.md](DATA_README.md) for an overview of the system
- **Examples**: Check [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md) for step-by-step examples
- **Technical Details**: Read [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for in-depth documentation

### Key Files

- `data/` - Structured card data (JSON format) - **edit these files**
- `docs/` - Generated markdown files - **do not edit directly**
- `templates/` - Markdown templates with placeholders
- `tools/extract_data.py` - Extract data from markdown to JSON
- `tools/generate_markdown.py` - Generate markdown from JSON + templates

## 🛡️ Other Community Projects
Here are some projects within the homm3bg community that are definitely worth a visit.

- [Rulebook Rewrite Project](https://github.com/Heegu-sama/Homm3BG)
- [Fan-Made Mission Book](https://github.com/qwrtln/Homm3BG-mission-book)
- [Factory Rule Book](https://github.com/piotrbruzda/Homm3BG-FactoryRulebook)
- [Scenario Map Editor](https://github.com/zedero/HoMM3Boardgame)
