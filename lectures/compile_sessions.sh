#!/bin/bash

mkdir -p scratch

for i in 1 2 3 4 6 7 9 10 12 13 15 16 17
do

cat <<EOF > S$i.tex

\documentclass[10pt, a4paper, twoside]{article}
\input{common.tex}

\begin{document}

\input{session$i}

\bibliographystyle{plain} % We choose the "plain" reference style
\bibliography{refs} % Entries are in the refs.bib file

\end{document}
EOF
latexmk S$i.tex
mv S$i* scratch
done

