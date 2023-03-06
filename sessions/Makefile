TEXFILES := $(wildcard *.tex)
PDFFILES := $(TEXFILES:.tex=.pdf)

all: $(PDFFILES)
	@echo "Done!"
	@echo "Compiled PDFs:" $(PDFFILES) 
	 
%.pdf: %.tex 
	lualatex $< 

 .PHONY: clean 

 clean: 
	rm -f *.aux *.log *.out 