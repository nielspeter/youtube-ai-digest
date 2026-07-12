.PHONY: install seed run resolve dry dev build preview clean

# No venv, no pip, no activate. `uv run` reads the dependencies from the
# script header (PEP 723), builds a cached env, and fetches Python if needed.
DIGEST := uv run scripts/digest.py

install:            ## Install site deps (Python env is handled on-demand by uv)
	npm install

seed:               ## Mark current feed items as seen (no summaries)
	$(DIGEST) --seed

run:                ## Fetch new videos, summarize, write markdown
	$(DIGEST)

resolve:            ## Resolve + cache channel IDs, then exit
	$(DIGEST) --resolve

dry:                ## Full run without persisting state/index
	$(DIGEST) --dry-run

dev:                ## VitePress dev server (live preview)
	npm run docs:dev

build:              ## Build the static site into docs/.vitepress/dist
	npm run docs:build

preview:            ## Preview the built site
	npm run docs:preview

clean:              ## Remove build output and caches
	rm -rf docs/.vitepress/dist docs/.vitepress/cache
