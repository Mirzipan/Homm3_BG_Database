#!/usr/bin/env bash

LANGUAGE=$1


git restore docs/

find docs -name "*.pl.md" -delete
find docs -name "*.es.md" -delete
find docs -name "*.fr.md" -delete

if [[ $LANGUAGE == "en" ]]; then
  git restore mkdocs.yml
  exit
fi

po4a --no-update po4a.cfg --target-lang "${LANGUAGE}"

find docs/ -name "*.$LANGUAGE.md"| while IFS= read -r file; do
  target="${file::-5}md"
  echo "Moving file: $file -> $target"
  mv "$file" "$target"
done

cp "navigation.$LANGUAGE.yml" docs/.nav.yml

sed -i -e "s/language: en/language: $LANGUAGE/" \
    -e "s/alternate.*-round/alternate: $LANGUAGE-round/" \
  mkdocs.yml
