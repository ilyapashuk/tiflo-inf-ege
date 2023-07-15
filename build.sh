#!/bin/bash
# this script is only used for local test builds
set -e
mkdir output
pandoc -o output/index.html docs/index.md
pandoc -o output/info.html docs/info.md
pandoc -o output/braille.html docs/braille.md
pandoc -o output/softrec.html docs/softrec.md
mkdir output/tasks
pandoc -o output/tasks/3.html docs/tasks/3.md
pandoc -o output/tasks/2.html docs/tasks/2.md
cp docs/tasks/2.py output/tasks/2.py
pandoc -o output/tasks/6.html docs/tasks/6.md
pandoc -o output/tasks/gm.html docs/tasks/gm.md
7z a 6s.7z ./6s
mv ./6s.7z ./output/tasks/
7z a gm.7z ./gm
mv ./gm.7z ./output/tasks/
7z a gm2.7z ./gm2
mv ./gm2.7z ./output/tasks/
