# amd3
An experimental fork of [d3](http://d3js.org) implemented as a collection of AMD modules.  

This repo's version of `d3.js` (in dist/) should be functionally identical to [mbostock's master version](https://github.com/mbostock/d3), but is built via [r.js](https://github.com/jrburke/r.js) instead of [SMASH](https://github.com/mbostock/smash).  The `Makefile` utilizes r.js' `onBuildWrite` feature to remove the AMD definitions from the built file, thus achieving [SMASH's goal](https://github.com/mbostock/smash/wiki) of keeping injected modules in the same scope as their caller.  The built file currently contains no AMD calls or dependencies.

There is also an experimental `amd/d3.js` that preserves the AMD overhead and is meant for use with an AMD loader like [RequireJS](http://requirejs.org).  `amd/d3.js` currently doesn't work, as I still need sort out some internal dependency issues.

The immediate goal of this project is to make it possible for me to selectively integrate submodules from d3 (dsv, geo, etc) into an AMD project workflow, with a single build containing both d3 and project-specific code.  The longer term goal is to explore the possibility of migrating the upstream project over to AMD.  In the meantime, if you just want to use stock d3 in an AMD project, you could use a [shim config](http://stackoverflow.com/questions/13157704/how-to-integrate-d3-with-require-js) or [add a define() wrapper directly to d3.js](https://github.com/wq/wq.app/blob/master/js/lib/d3.js).

See [mbostock/smash#12](https://github.com/mbostock/smash/issues/12) for background discussion.  Conversion from SMASH modules to AMD modules via [smash2amd](https://github.com/sheppard/smash2amd).  `onBuildWrite` trickery inspired by [jQuery](https://github.com/jquery/jquery).

# Data-Driven Documents

**D3.js** is a JavaScript library for manipulating documents based on data. **D3** helps you bring data to life using HTML, SVG and CSS. D3’s emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a proprietary framework, combining powerful visualization components and a data-driven approach to DOM manipulation.

Want to learn more? [See the wiki.](https://github.com/mbostock/d3/wiki)

For examples, [see the gallery](https://github.com/mbostock/d3/wiki/Gallery) and [mbostock’s bl.ocks](http://bl.ocks.org/mbostock).
