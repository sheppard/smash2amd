#!/bin/sh
S2A=smash2amd/
$S2A/reorganize.sh
git commit -m "reorganize filesystem"
$S2A/smash2amd.py d3.js
$S2A/smash2amd.py d3/
git add d3.js d3/
git commit -m "smash2amd"
cp -p $S2A/build/* .
mv base bin/
git add bin/base build.js build.amd.js Makefile package.json
git commit -m "use r.js for build"
make
git add d3/base.js dist/
git commit -m "update build"
git add README.md
git commit -m "update README"
