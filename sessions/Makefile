TEXFILES := $(wildcard Unit*.tex)
PDFFILES := $(patsubst %.tex,../pdfs/%.pdf,$(TEXFILES))

all: $(PDFFILES)
	@echo "Done!"
	@echo "Compiled PDFs:" $(PDFFILES)

# regla genèrica
../pdfs/%.pdf: %.tex Biblio.tex Refs.tex OR_Common.tex
	@echo "Compilant $< → $@"
	latexmk -pdf -output-directory=../pdfs $<

%: ../pdfs/%.pdf
	@true

.PHONY: clean cleanpdf

clean:
	latexmk -C
	rm -f ../pdfs/*.aux ../pdfs/*.log ../pdfs/*.bbl ../pdfs/*.blg ../pdfs/*.out ../pdfs/*.nav ../pdfs/*.snm ../pdfs/*.toc ../pdfs/*.fls ../pdfs/*.fdb_latexmk 

cleanpdf:
	rm -f ../pdfs/Unit*.pdf
	
copy: $(PDFFILES)
		@echo "Copying PDFs to ../../../WEB/ORweb/sessions"
		cp ../pdfs/Unit*.pdf ../../../WEB/ORweb/docs/sessions/
