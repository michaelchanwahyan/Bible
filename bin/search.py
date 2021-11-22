#!/usr/bin/python3
import os
with open("input.txt", "r") as fp:
    lines = fp.readlines()
ls = []
for l in lines:
    for l_ in l.strip().split(' '):
        ls.append(l_)

booklist = ["Gen","Exo","Lev","Num","Deu",
        "Jos","Jug","Rut","1Sa","2Sa","1Ki","2Ki",
        "1Ch","2Ch","Ezr","Neh",
        "Est","Job","Psa","Pro","Ecc","Son",
        "Isa","Jer","Lam","Eze","Dan",
        "Hos","Joe","Amo","Oba","Jon","Mic",
        "Nah","Hab","Zep","Hag","Zec","Mal",
        "Mat","Mak","Luk","Jhn","Act",
        "Rom","1Co","2Co","Gal","Eph","Phl",
        "Col","1Ts","2Ts","1Ti","2Ti","Tit","Phm",
        "Heb","Jas","1Pe","2Pe",
        "1Jn","2Jn","3Jn","Jud","Rev"]
#if bibleversion == 'sblgnt':
#    booklist = booklist[39:]
keywordNum = len(ls)
bvlist = ['cuv1', 'cuv2', 'cnv', 'lzz', 'tcv19', 'wenl', 'nrsv', 'kjv']
# bvlist := bible version list
for book in booklist:
    lines = {}
    for bv in bvlist:
        fullbookpath = "../src/bible_src/" + bv + "/" + book + ".txt"
        with open(fullbookpath, "r") as fp:
            lines[bv] = fp.readlines()
        fp.close()
    lineNum = len(lines['cuv1']) # assume all versions have the same no of line
    for lineIdx in range(lineNum):
        for bv in bvlist:
            lines[bv][lineIdx] = lines[bv][lineIdx].strip()
            if all(keyword in lines[bv][lineIdx] for keyword in ls):
                print(book + "  " + bv + "  " + lines[bv][lineIdx])
                break

