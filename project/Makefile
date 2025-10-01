# Nom del fitxer markdown i de sortida
MD_FILE = OptimizationProject.md
PDF_FILE = OptimizationProject.pdf

# Directori del repositori de la web (canvia-ho pel camí real)
WEB_REPO = ../../../WEB/ORweb/docs/projects

# Compila el markdown a PDF amb pandoc (només si cal)
$(PDF_FILE): $(MD_FILE)
	pandoc $(MD_FILE) -o $(PDF_FILE)

# Copia el markdown i el pdf al repo de la web
copy: $(MD_FILE) $(PDF_FILE)
	cp $(MD_FILE) $(WEB_REPO)
	cp $(PDF_FILE) $(WEB_REPO)

# Workflow complet: compilar i copiar
all: $(PDF_FILE) copy

clean:
	rm -f $(PDF_FILE)

.PHONY: all copy clean
