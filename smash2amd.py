#!/usr/bin/env python
import os
import re

def smash2amd(filename):
    name = os.path.splitext(os.path.basename(filename))[0]
    definere = re.compile(r'^define\(')
    importre = re.compile(r'^import "(.+)";')
    exportre1 = re.compile(r'^(d3.%s) = ' % name)
    exportre2 = re.compile(r'^function (d3_%s)\(' % name)

    code = open(filename).read()
    rows = []
    deps = []
    export = ""
    for row in code.split('\n'):
        if definere.match(row):
            print "Already AMD!"
            return
        match = importre.match(row)
        if match:
            dep = match.group(1)
            if not dep.startswith("../"):
                dep = "./%s" % dep
            if dep.endswith('/'):
                dep += "index"
            deps.append(dep)
        else:
            match = exportre1.match(row)
            if match:
                export = match.group(1)
            else:
                match = exportre2.match(row)
                if match and not export.startswith('d3.'):
                    export = match.group(1)
                
            rows.append(row)
    
    base = ''
    if export:
        if export.startswith('d3.'):
            deps.insert(0, 'base')
            base = 'd3'
        export = "\nreturn %s;" % export

    if len(deps) > 0:
        depstr = "[%s], " % (",".join(map(lambda d: '"%s"' % d, deps)))
    else:
        depstr = ""

    out = open(filename, 'w')
    out.write(
"""/* start amd */
define(%sfunction(%s) {
/* end amd */
%s
/* start amd */%s
});
/* end amd */""" % (
        depstr,
        base,
        "\n".join(rows),
        export
    ))
    

def run(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if not filename.endswith('.js'):
                continue 
            smash2amd(os.path.join(root, filename))

if __name__ == '__main__':
    run('.')
