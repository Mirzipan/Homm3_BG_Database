#!/usr/bin/env bash

EXCLUDE="\.pl\.md"

temp_file=$(mktemp)
trap 'rm -f -- "$temp_file"' EXIT

find docs/ -name "*.md" | grep -v $EXCLUDE | sort | while read file; do
  echo "[type: markdown] $file \$lang:${file::-3}.\$lang.md" >> $temp_file
done

START='# PO4A TARGETS - START'
END='# PO4A TARGETS - END'

sed -i "/$START/,/$END/!b;//!d;/$START/r $temp_file" po4a.cfg
