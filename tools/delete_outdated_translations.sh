#!/usr/bin/env bash

for f in $(ls translations); do
  if [[ -z $(find docs/ -name $f) ]]; then
    echo "Not found original files for $f, deleting"
    rm -rf translations/$f
  fi
done
