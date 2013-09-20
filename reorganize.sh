#!/bin/sh

git rm *.js
git mv src d3
git mv d3/d3.js ./
sed -i 's/import "/import "d3\//' d3.js
