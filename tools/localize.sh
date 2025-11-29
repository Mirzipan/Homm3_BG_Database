#!/usr/bin/env bash

LANGUAGE=$1


git restore docs/

find docs -name "*.pl.md" -delete
find docs -name "*.es.md" -delete
rm -f docs/.nav.yml

if [[ $LANGUAGE == "en" ]]; then
  exit
fi

sed -i 's/pl es/'"$LANGUAGE"'/' po4a.cfg
po4a --no-update po4a.cfg
git restore po4a.cfg

find docs/ -name "*.$LANGUAGE.md"| while IFS= read -r file; do
  target="${file::-5}md"
  echo "Moving file: $file -> $target"
  mv "$file" "$target"
done

cp "navigation.$LANGUAGE.yml" docs/.nav.yml
