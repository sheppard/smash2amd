#!/usr/bin/env python
import sys
import os
import re

def smash2amd(filename):
    name = os.path.splitext(os.path.basename(filename))[0]
    if name in ('start', 'end'):
        return
    definere = re.compile(r'^define\(')
    importre = re.compile(r'^import "(.+)";')
    exportre1 = re.compile(r'^(d3.%s) = ' % name)
    exportre2 = re.compile(r'^function (d3_%s)\(' % name)

    code = open(filename).read()
    rows = []
    deps = []
    export = ""
    base = ""
    for row in code.split('\n'):
        if definere.match(row):
            print "Already AMD!"
            return
        match = importre.match(row)
        if match:
            # This line of the file contains an import
            dep = match.group(1)

            # These deps are only in d3.js
            if dep == "d3/end":
                continue
            if dep == "d3/start":
                dep = "d3/base"
                export = "d3"
                base = "d3"

            # For other deps, convert SMASH paths to AMD-compatible versions
            if not dep.startswith("../") and not dep.startswith("d3"):
                dep = "./%s" % dep
            if dep.endswith('/'):
                dep += "index"
            deps.append(dep)
        else:
            # This line of the file does not contain an import; check for 
            # something that looks like an export
            match = exportre1.match(row)
            if match:
                export = match.group(1)
                deps.insert(0, "d3/base")
                base = "d3"
            else:
                match = exportre2.match(row)
                if match and not export.startswith('d3.'):
                    export = match.group(1)
                
            rows.append(row)
    
    if export:
        export = "\nreturn %s;" % export

    if len(deps) > 0:
        depstr = "[%s], " % (",".join(map(lambda d: '"%s"' % d, deps)))
    else:
        depstr = ""

    out = open(filename, 'w')
    out.write(
"""define(%sfunction(%s) {
%s%s
});
""" % (
        depstr,
        base,
        "\n".join(rows),
        export
    ))
    

def run(path):
    if not os.path.isdir(path):
        print path
        smash2amd(path)
        return
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if not filename.endswith('.js'):
                continue 
            path = os.path.join(root, filename)
            print path
            smash2amd(path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'
    run(path)
