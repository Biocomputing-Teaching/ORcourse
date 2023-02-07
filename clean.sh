#clean garbage in git
for type in fls log aux pro auxlock bbl bcf blg idx snm nav vrb toc ilg ind loe out aux fdb_latexmk xml gz pro log md5
do
 echo "Processing *.$type"
 git rm -f *.$type
 rm -f *.$type
 echo "Processing */*.$type"
 git rm -f */*.$type
 rm -f */*.$type
done
