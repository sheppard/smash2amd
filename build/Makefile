LOCALE ?= en_US

GENERATED_FILES = \
	dist/d3.js \
	dist/d3.min.js \
	dist/amd/d3.js \
	d3/format/format-localized.js \
	d3/time/format-localized.js \
	bower.json \
	component.json

all: $(GENERATED_FILES)

.PHONY: clean all test

test:
	@npm test

benchmark: all
	@node test/geo/benchmark.js

d3/format/format-localized.js: bin/locale d3/format/format-locale.js
	LC_NUMERIC=$(LOCALE) LC_MONETARY=$(LOCALE) locale -ck LC_NUMERIC LC_MONETARY | bin/locale d3/format/format-locale.js > $@

d3/time/format-localized.js: bin/locale d3/time/format-locale.js
	LC_TIME=$(LOCALE) locale -ck LC_TIME | bin/locale d3/time/format-locale.js > $@

d3/start.js: package.json bin/start
	bin/start > $@

d3/base.js: package.json bin/base
	bin/base > $@

dist/amd/d3.js: d3/base.js d3/format/format-localized.js d3/time/format-localized.js package.json
	@rm -f $@
	node_modules/.bin/r.js -o build.amd.js

dist/d3.js: d3/base.js d3/format/format-localized.js d3/time/format-localized.js package.json
	@rm -f $@
	node_modules/.bin/r.js -o build.js

dist/d3.min.js: dist/d3.js bin/uglify
	@rm -f $@
	bin/uglify $< > $@

%.json: bin/% package.json
	@rm -f $@
	bin/$* > $@
	@chmod a-w $@

clean:
	rm -f -- $(GENERATED_FILES)
