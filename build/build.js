({
  "name": "d3",
  "out": "dist/d3.js",
  "baseUrl": "./",
  "optimize": "none",
  "onBuildWrite": function(moduleName, path, contents) {
    return contents
      .replace(/define\([^{]*?{/, "")
      .replace(/\}\);[^}\w]*$/, "");
  },
  "wrap": {
    "startFile": "d3/start.js",
    "endFile": "d3/end.js"
  },
  "paths": {
    "d3/base": "empty:"
  }
})
