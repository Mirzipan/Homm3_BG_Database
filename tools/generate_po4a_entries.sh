#!/usr/bin/env bash

EXCLUDE="\.pl\.md"

echo "BEFORE GENERATION:"
grep "artifacts\.\|units\." po4a.cfg

temp_file=$(mktemp)
trap 'rm -f -- "$temp_file"' EXIT

echo "ALL THE FILES:"
find docs/ -name "*.md" | grep -v $EXCLUDE

echo "ALL THE FILES SORTED:"
find docs/ -name "*.md" | grep -v $EXCLUDE | sort

echo "NOW PROCESSING:"
find docs/ -name "*.md" | grep -v $EXCLUDE | sort | while read file; do
  echo "[type: markdown] $file \$lang:${file::-3}.\$lang.md"
  echo "[type: markdown] $file \$lang:${file::-3}.\$lang.md" >> $temp_file
done

START='# PO4A TARGETS - START'
END='# PO4A TARGETS - END'

echo "BEFORE SED:"
grep "artifacts\.\|units\." $temp_file

sed -i "/$START/,/$END/!b;//!d;/$START/r $temp_file" po4a.cfg

echo "AFTER SED:"
grep "artifacts\.\|units\." po4a.cfg
