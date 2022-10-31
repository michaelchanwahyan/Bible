#!/bin/sh
python3 genOtTexSrc.py
cd ot_out
# 1st XeLaTex build, presuming
# - failure in toc               if there does not have ot.toc
# - failure in hyperref from toc if there does not have ot.aux
#xelatex ot.tex # will generate ot.toc , ot.aux
# 2nd XeLaTex build, supposing
# - success in toc               since there has ot.toc
# - success in hyperref from toc since there has ot.aux
xelatex ot.tex #second build, with success in toc
rm -f ot.maf ot.mtc* ot.out ot.log
mv ot.pdf ../../
# 3rd XeLaTex build, for small character version
cp  ot.aux  ot_small.aux
cp  ot.toc  ot_small.toc
cat ot.tex | sed 's/\\large/\\small/' > ot_small.tex
xelatex ot_small.tex
rm -f ot_small.maf ot_small.mtc* ot_small.out ot_small.log
mv ot_small.pdf ../../
cd ..
