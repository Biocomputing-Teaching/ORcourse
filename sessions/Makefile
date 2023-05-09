TEXFILES := $(wildcard *.tex)
PDFFILES := $(TEXFILES:.tex=.pdf)

all: $(PDFFILES)
	@echo "Done!"
	@echo "Compiled PDFs:" $(PDFFILES) 
	 
%.pdf: %.tex ../tools/Biblio.tex ../tools/Refs.tex
	lualatex $< 
#	lualatex $< 

 .PHONY: clean 

 clean: 
	rm -f *.aux *.log *.out *.nav *.snm *.toc

 cleanpdf: 
	rm -f *.pdf