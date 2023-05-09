all: SolvedExercises.pdf

SolvedExercises.pdf: *.tex refs.bib
	lualatex SolvedExercises
	# bibtex SolvedExercises
	# lualatex SolvedExercises
	# lualatex SolvedExercises

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.out
