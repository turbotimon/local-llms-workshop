# Minimal example: how to create HTML and PDF from a Marp slide deck
SLIDES = slides.md
STEM = $(SLIDES:.md=)

# Marp CLI: use globally installed marp, or npx (no install, recommended)
#MARP = marp
MARP = npx @marp-team/marp-cli

all: pdf pptx

# Mermaid CLI writes <name>-1.svg for the first diagram in a markdown file
diagram: resources/ingredients.md
	npx -y @mermaid-js/mermaid-cli -i resources/ingredients.md -o resources/ingredients.svg -b transparent
	mv resources/ingredients-1.svg resources/ingredients.svg

html: $(SLIDES)
	$(MARP) $(SLIDES) --allow-local-files --theme-set theme/ost.css -o $(STEM).html

pdf: html
	$(MARP) $(SLIDES) --allow-local-files --theme-set theme/ost.css -o $(STEM).pdf

pptx: html
	$(MARP) $(SLIDES) --allow-local-files --theme-set theme/ost.css -o $(STEM).pptx
