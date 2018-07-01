# Bible
This is a project working on Bible that includes its several common versions in English and Chinese.
It intends to show the text of each version in a line-by-line manner for, maybe not better reading but, better comparison.

## Getting Started
objective: compile bible.pdf

### Prerequisites and Remarks
- Operating System                : Unix-based
- Software Library                : LaTeX (OSX: MacTex; others: tex-live)
- special LaTeX packages required : xeCJK, BiauKai (for Chinese Character typesettings)
- LaTeX Engine                    : XeLaTex
- LaTeX build option              : syntax=1


## Usage

```
python3 genBibleTexSrc.py
/bin/sh buildBibleTex.sh
```
and finally the output file "bible.pdf" should be ready.

// remark : bible_small.pdf is small-characters version of

//          the bible that greatly reduces the number of pages

## Current Bible Version Supported
- CUV  (Chinese Union Version)
- WL   (Wenli Version)
- LZZ  (Lu Zhen Zhong Bible Translation)
- KJV  (King James Version)
- CNV  (Chinese New Version)
- NRSV (New Revised Standard Version)
- MSGV (The Message Bible by Eugene Peterson)

## Editor
contact person : Michael via chchan@link.cuhk.edu.hk

