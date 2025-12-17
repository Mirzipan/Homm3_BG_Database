#!/bin/bash
# Regenerate all markdown files from JSON data
# This script runs the markdown generator for all card types

cd "$(dirname "$0")/.."

echo "========================================="
echo " Regenerating all markdown files"
echo "========================================="
echo ""

python3 tools/generate_markdown.py

echo ""
echo "========================================="
echo " Generation complete!"
echo "========================================="
echo ""
echo "Review the changes with: git diff docs/"
echo "If everything looks good, commit with: git add data/ docs/ && git commit -m 'Update card data'"
