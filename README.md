# Bible
This is a project working on Bible that includes its several common versions in English and Chinese.
It intends to show the text of each version in a line-by-line manner for, maybe not better reading but, better comparison.

## Getting Started
objective: compile bible.pdf

```bash
git clone --depth 1 https://github.com/michaelchanwahyan/Bible.git
cd Bible
git submodule init
git submodule update --depth 1
```

### Prerequisites and Remarks
- Operating System                : Unix-based
- Software Library                : LaTeX (OSX: MacTex; others: tex-live)
- special LaTeX packages required : xeCJK, BiauKai (for Chinese Character typesettings)
- LaTeX Engine                    : XeLaTex
- LaTeX build option              : syntax=1


## Usage

```bash
python3 genBibleTexSrc.py
/bin/sh buildBibleTex.sh
```
and finally the output file "bible.pdf" should be ready.

// remark : bible_small.pdf is small-characters version of

//          the bible that greatly reduces the number of pages

// remark : as of 2021, ot and nt (Old and New Testament) are to be packed with
original Hebrew and Greek from openly accessible original texts)

## Current Bible Version Supported
- CCV  (新漢語譯本)
- CUV  (Chinese Union Version 和合本)
- LZZ  (Lu Zhen Zhong Bible Translation 呂振中譯本)
- KJV  (King James Version)
- CUVR (Chinese Union Version Revised 和合本修定版)
- CNV  (Chinese New Version 新譯本)
- NRSV (New Revised Standard Version)
- WL   (Wenli Version 文理本)
- MSGV (The Message Bible by Eugene Peterson)
- NETS (New English Translation of Septuagint)
- SBLGNT (Society of Biblical Literature Greek New Testament)
- JPSV1917 (Tanakh 1917 edition according to the Masoretic Text, Jewish Publication Society)
- TCV2019 (Today's Chinese Version 2019 現代中文譯本2019)

## Notice:
for Masoretic typesetting, assistance font shall be downloaded and installed from SBL (Society of Biblical Literature), namely the font file :
```
SBL BibLit.ttf
```
from https://www.sbl-site.org/educational/BiblicalFonts_SBLBibLit.aspx


## Editor
contact person : Michael via chchan@link.cuhk.edu.hk

