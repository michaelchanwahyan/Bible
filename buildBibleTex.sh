#!/bin/sh
python3 genBibleTexSrc.py
cd bible_out
# 1st XeLaTex build, presuming
# - failure in toc               if there does not have bible.toc
# - failure in hyperref from toc if there does not have bible.aux
#xelatex -syntax=1 bible.tex # will generate bible.toc , bible.aux
# 2nd XeLaTex build, supposing
# - success in toc               since there has bible.toc
# - success in hyperref from toc since there has bible.aux
xelatex -syntax=1 bible.tex #second build, with success in toc
rm -f bible.maf bible.mtc* bible.out bible.log
mv bible.pdf ../
# 3rd XeLaTex build, for small character version
cp  bible.aux  bible_small.aux
cp  bible.toc  bible_small.toc
cat bible.tex | sed 's/\\large/\\small/' > bible_small.tex
xelatex -syntax=1 bible_small.tex
rm -f bible_small.maf bible_small.mtc* bible_small.out bible_small.log
mv bible_small.pdf ../
cd ..
