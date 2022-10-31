#!/bin/sh
python3 genNtTexSrc.py
cd nt_out
# 1st XeLaTex build, presuming
# - failure in toc               if there does not have nt.toc
# - failure in hyperref from toc if there does not have nt.aux
#xelatex nt.tex # will generate nt.toc , nt.aux
# 2nd XeLaTex build, supposing
# - success in toc               since there has nt.toc
# - success in hyperref from toc since there has nt.aux
xelatex nt.tex #second build, with success in toc
rm -f nt.maf nt.mtc* nt.out nt.log
mv nt.pdf ../../
# 3rd XeLaTex build, for small character version
cp  nt.aux  nt_small.aux
cp  nt.toc  nt_small.toc
cat nt.tex | sed 's/\\large/\\small/' > nt_small.tex
xelatex nt_small.tex
rm -f nt_small.maf nt_small.mtc* nt_small.out nt_small.log
mv nt_small.pdf ../../
cd ..
