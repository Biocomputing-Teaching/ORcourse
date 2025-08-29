# Change the output directory for PDFs to ../pdfs
SHELL := /bin/bash

SESSIONS := $(wildcard session*.tex)
NUMS := $(patsubst session%.tex,%,$(SESSIONS))
TARGETS := $(addprefix ../pdfs/S, $(addsuffix .pdf, $(NUMS)))

TEX_MAIN := ORCourseLectures.tex
PDF_OUT := ../pdfs/ORCourseLectures.pdf
TEX_SRCS := $(wildcard session*.tex)
COMMON_SRCS := $(wildcard ../common/*)

all: sessions book

sessions: $(TARGETS)
book: $(PDF_OUT)

$(PDF_OUT): $(TEX_MAIN) $(TEX_SRCS) $(COMMON_SRCS) | ../pdfs
	latexmk -pdf -interaction=nonstopmode -output-directory=../pdfs $(TEX_MAIN)

../pdfs/ORCourseLectures.pdf: $(TEX_MAIN) $(TEX_SRCS) $(COMMON_SRCS) | ../pdfs
	latexmk -pdf -interaction=nonstopmode -output-directory=../pdfs $(TEX_MAIN)

../pdfs:
	mkdir -p ../pdfs

# Directly generate the temporary tex file in ../pdfs and remove after PDF creation
../pdfs/S%.pdf: session%.tex | ../pdfs
	echo '\documentclass[10pt, a4paper, twoside]{article}' > ../pdfs/S$*.tex
	echo '\input{common.tex}' >> ../pdfs/S$*.tex
	echo '' >> ../pdfs/S$*.tex
	echo '\begin{document}' >> ../pdfs/S$*.tex
	echo '' >> ../pdfs/S$*.tex
	echo '\input{session$*}' >> ../pdfs/S$*.tex
	echo '' >> ../pdfs/S$*.tex
	echo '\bibliographystyle{plain} % We choose the "plain" reference style' >> ../pdfs/S$*.tex
	echo '\bibliography{refs} % Entries are in the refs.bib file' >> ../pdfs/S$*.tex
	echo '' >> ../pdfs/S$*.tex
	echo '\end{document}' >> ../pdfs/S$*.tex
	latexmk -pdf -quiet -output-directory=../pdfs ../pdfs/S$*.tex
	rm -f ../pdfs/S$*.tex

clean:
	latexmk -C -output-directory=../pdfs
	rm -f S*.tex S*.pdf S*.aux S*.log S*.bbl S*.blg S*.fdb_latexmk S*.fls
	rm -f ../pdfs/ORCourseLectures.pdf

.PHONY: all clean sessions book
