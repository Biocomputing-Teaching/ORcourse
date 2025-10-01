# Nom del fitxer markdown i de sortida
MD_FILE=OptimizationProject.md
PDF_FILE=OptimizationProject.pdf

# Directori del repositori de la web (canvia-ho pel camí real)
WEB_REPO=../../../WEB/ORweb/docs/projects

# Compila el markdown a PDF amb pandoc
pdf:
	pandoc $(MD_FILE) -o $(PDF_FILE)

# Copia el markdown al repo de la web
copy:
	cp $(MD_FILE) $(WEB_REPO)
	cp $(PDF_FILE) $(WEB_REPO)

# Workflow complet: compilar i copiar
all: pdf copy
