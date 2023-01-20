#!/bin/python3
import os
os.system("clear")

# Generate Front Page
os.system("cat bible_out/prefix.tex | " + \
        "sed 's/聖經/舊約聖經/' | " + \
        "sed 's/新漢譯(CCV) //' | " + \
        "sed 's/希臘文(SBLGNT) //' | " + \
        "sed 's/%remove comment for OT cover%//'" + \
        " > ot_out/ot.tex") ;

# Generate Bible TOC

# cross referencing index to be added
# by 1 whenever there is a new section
xrefCnt     = 1
xbkCnt      = 0

# Generate OT
with open("otIndex.txt", "r") as fp:
    ot_index = fp.readlines()
fp.close()
fp = open( "ot_out/ot.tex" , "a" )
for otBook in ot_index :
    xbkCnt += 1
    if xbkCnt == 1:
        fp.write("\\part{$\\mathcal{OT}$ Torah}\n")
    if xbkCnt == 6:
        fp.write("\\part{$\\mathcal{OT}$ Neviim}\n")
    if xbkCnt == 27:
        fp.write("\\part{$\\mathcal{OT}$ Ketuvim}\n")
    words = otBook.strip().split()
    # -------------------------------------------------------------------
    # words[0] words[1] words[2] words[3] Chi title abrev Eng title abrev
    # -------------------------------------------------------------------
    print( "----------------------------" )
    print( words[0] + " " + words[2]      )
    print( "----------------------------" )
    # -------------------
    # open the bible in different versions
    # -------------------
    fp_cuv1 = open( "bible_src/cuv1/"    + words[3] + ".txt" ) ; content_cuv1 = fp_cuv1.readlines() ; fp_cuv1.close()
    fp_lzzv = open( "bible_src/lzz/"     + words[3] + ".txt" ) ; content_lzzv = fp_lzzv.readlines() ; fp_lzzv.close()
    fp_kjvv = open( "bible_src/kjv/"     + words[3] + ".txt" ) ; content_kjvv = fp_kjvv.readlines() ; fp_kjvv.close()
    fp_cuv2 = open( "bible_src/cuv2/"    + words[3] + ".txt" ) ; content_cuv2 = fp_cuv2.readlines() ; fp_cuv2.close()
    fp_cnvv = open( "bible_src/cnv/"     + words[3] + ".txt" ) ; content_cnvv = fp_cnvv.readlines() ; fp_cnvv.close()
    fp_nrsv = open( "bible_src/nrsv/"    + words[3] + ".txt" ) ; content_nrsv = fp_nrsv.readlines() ; fp_nrsv.close()
    fp_wenl = open( "bible_src/wenl/"    + words[3] + ".txt" ) ; content_wenl = fp_wenl.readlines() ; fp_wenl.close()
    fp_tcv19= open( "bible_src/tcv19/"   + words[3] + ".txt" ) ; content_tcv19= fp_tcv19.readlines(); fp_tcv19.close()
    fp_ccbv = open( "bible_src/ccb/"     + words[3] + ".txt" ) ; content_ccbv = fp_ccbv.readlines() ; fp_ccbv.close()
    fp_msgv = open( "bible_src/msg/"     + words[3] + ".txt" ) ; content_msgv = fp_msgv.readlines() ; fp_msgv.close()
    fp_jpsv = open( "bible_src/jps1917/" + words[3] + ".txt" ) ; content_jpsv = fp_jpsv.readlines() ; fp_jpsv.close()
    # -----------------------------------------------------
    # [ GEN LATEX ] : create \chapter{} for current segment
    # -----------------------------------------------------
    print( words[0]+words[2] )
    fp.write( "\\chapter{"+words[0]+" "+words[2]+"}\n" )
    fp.write( "\\label{subsec:book"+str(xbkCnt)+"}\n"  )
    fp.write( "\\begin{multicols}{2}\n"                )
    fp.write( "\\minitoc\n"                            )
    fp.write( "\\end{multicols}\n"                     )
    # ------------------------------------------
    # check total chapter number in this segment
    # ------------------------------------------
    # -------
    # cuv1
    # -------
    sentenceNum = len( content_cuv1 )
    print("sentence no. in cuv1 "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cuv1[ sentenceNum - 1 ].split(".")[0] )
    print("cuv1 "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # lzzv
    # -------
    sentenceNum = len( content_lzzv )
    print("sentence no. in lzzv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_lzzv[ sentenceNum - 1 ].split(".")[0] )
    print("lzzv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # kjvv
    # -------
    sentenceNum = len( content_kjvv )
    print("sentence no. in kjvv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_kjvv[ sentenceNum - 1 ].split(".")[0] )
    print("kjvv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # cuv2
    # -------
    sentenceNum = len( content_cuv2 )
    print("sentence no. in cuv2 "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cuv2[ sentenceNum - 1 ].split(".")[0] )
    print("cuv2 "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # cnvv
    # -------
    sentenceNum = len( content_cnvv )
    print("sentence no. in cnvv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cnvv[ sentenceNum - 1 ].split(".")[0] )
    print("cnvv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # nrsv
    # -------
    sentenceNum = len( content_nrsv )
    print("sentence no. in nrsv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_nrsv[ sentenceNum - 1 ].split(".")[0] )
    print("nrsv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # wenl
    # -------
    sentenceNum = len( content_wenl )
    print("sentence no. in wenl "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_wenl[ sentenceNum - 1 ].split(".")[0] )
    print("wenl "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # tcv19
    # -------
    sentenceNum = len( content_tcv19 )
    print("sentence no. in tcv19 "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_tcv19[ sentenceNum - 1 ].split(".")[0] )
    print("tcv19 "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # ccbv
    # -------
    sentenceNum = len( content_ccbv )
    print("sentence no. in ccbv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_ccbv[ sentenceNum - 1 ].split(".")[0] )
    print("ccbv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # msgv
    # -------
    sentenceNum = len( content_msgv )
    print("sentence no. in msgv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_msgv[ sentenceNum - 1 ].split(".")[0] )
    print("msgv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # jpsv
    # -------
    sentenceNum = len( content_jpsv )
    print("sentence no. in jpsv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_jpsv[ sentenceNum - 1 ].split(".")[0] )
    print("jpsv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -----------------------------
    # -----------------------------
    colorIntensity        = 100
    colorArr              =['CUV1LightRed'   , \
                            'LZZVLightGray'  , \
                            'KJVVLightGreen' , \
                            'CUV2LightYellow', \
                            'CNVVLightBrown' , \
                            'NRSVLightBlue'  , \
                            'WENLLightPurple', \
                            'TCV19PaleGreen' , \
                            'CCBVRichBlue'   , \
                            'MSGVLightWhite' , \
                            'JPS1917LightYellow']
    for chapterIdx in range(1,chapterNum+1,1) :
        # <<<< when a new version is added, no. of "c" in tabular requires adjustment >>>>
        bibleStr = "\section{"+words[0]+" "+words[2]+" "+str(chapterIdx)+"}" \
                   +" \hyperlink{toc}{[返主目錄]} \hyperref[subsec:book"+str(xbkCnt)+"]{[返卷目錄]}~\\begin{tabular}{ccccccccccc}\\cellcolor{" \
                   +colorArr[ 0]+"!"+str(colorIntensity)+"}{\\small CUV}&\\cellcolor{"     \
                   +colorArr[ 1]+"!"+str(colorIntensity)+"}{\\small LZZ}&\\cellcolor{"     \
                   +colorArr[ 2]+"!"+str(colorIntensity)+"}{\\small KJV}&\\cellcolor{"     \
                   +colorArr[ 3]+"!"+str(colorIntensity)+"}{\\small CUVR}&\\cellcolor{"    \
                   +colorArr[ 4]+"!"+str(colorIntensity)+"}{\\small CNV}&\\cellcolor{"     \
                   +colorArr[ 5]+"!"+str(colorIntensity)+"}{\\small NRSV}&\\cellcolor{"    \
                   +colorArr[ 6]+"!"+str(colorIntensity)+"}{\\small WLV}&\\cellcolor{"     \
                   +colorArr[ 7]+"!"+str(colorIntensity)+"}{\\small TCV2019}&\\cellcolor{" \
                   +colorArr[ 8]+"!"+str(colorIntensity)+"}{\\small CCBV}&\\cellcolor{"    \
                   +colorArr[ 9]+"!"+str(colorIntensity)+"}{\\small MSGV}&\\cellcolor{"    \
                   +colorArr[10]+"!"+str(colorIntensity)+"}{\\small JPSV1917}"             \
                   +"\\end{tabular}"                                                       \
                   +"\\label{sec:"+str(xrefCnt)+"}"                                        \
                   +"\n"
        fp.write( bibleStr )
        fp.write( "\\newline\n" )
        fp.write( "\\hyperref[sec:"+str(xrefCnt-1)+"]{< < < PREV CHAPTER < < <} ~~~ \\hyperref[sec:"+str(xrefCnt+1)+"]{> > > NEXT CHAPTER > > >} \\newline \n" )
        xrefCnt += 1
        for sentenceIdx in range(0,sentenceNum,1) :
            if ( chapterIdx < 10 and int(content_cuv1[sentenceIdx].split(".")[0]) == chapterIdx ) or \
               ( chapterIdx > 9  and int(content_cuv1[sentenceIdx].split(".")[0]) == chapterIdx ) :
                bibleStr = "\\begin{tabularx}{\\textwidth}{|c|c||X|}\n"; fp.write( bibleStr )
                bibleStr = "\hline\n"                                  ; fp.write( bibleStr )
                # obtain chapter_verse string
                ch_vsStr = content_cuv1[sentenceIdx].replace("\n","").split(" ",1)[0].replace(".",":")
                # <<<< when a new version is added, argument in "multirow" requires adjustment >>>>
                bibleStr = "\\multirow{10}{*}{\\rotatebox[origin=c]{90}{\\hfill "+words[1]+" "+words[3]+" $"+ch_vsStr+"$ \\hfill}}\n"
                fp.write( bibleStr )
                # ---------------------------------------------------
                # add the content of cuv1 to 1st row
                # ---------------------------------------------------
                bibleStr = content_cuv1[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr= " & " \
                        +"\\cellcolor{"+colorArr[0]+"!"+str(colorIntensity)+"}"+"\\scriptsize{和合本}"+" & " \
                        +"\\cellcolor{"+colorArr[0]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of lzzv to 2nd row
                # ----------------------------------------------------
                bibleStr = content_lzzv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[1]+"!"+str(colorIntensity)+"}"+"\\scriptsize{呂振中本}"+" & " \
                        +"\\cellcolor{"+colorArr[1]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of kjvv to 3rd row
                # ----------------------------------------------------
                bibleStr = content_kjvv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[2]+"!"+str(colorIntensity)+"}"+"\\scriptsize{King James}"+" & " \
                        +"\\cellcolor{"+colorArr[2]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr ) ;
                # ----------------------------------------------------
                # add the content of cuv2 to 4th row
                # ----------------------------------------------------
                bibleStr = content_cuv2[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[3]+"!"+str(colorIntensity)+"}"+"\\scriptsize{和合修定}"+" & " \
                        +"\\cellcolor{"+colorArr[3]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of cnvv to 5th row
                # ----------------------------------------------------
                bibleStr = content_cnvv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[4]+"!"+str(colorIntensity)+"}"+"\\scriptsize{新譯本}"+" & " \
                        +"\\cellcolor{"+colorArr[4]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of nrsv to 6th row
                # ----------------------------------------------------
                bibleStr = content_nrsv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[5]+"!"+str(colorIntensity)+"}"+"\\scriptsize{New Rev St}"+" & " \
                        +"\\cellcolor{"+colorArr[5]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ---------------------------------------------------
                # add the content of wenl to 7th row
                # ---------------------------------------------------
                bibleStr = content_wenl[sentenceIdx].replace("\n","")
                bibleStr1 = []
                for c in bibleStr :
                    if ( not c.isdigit() ) and ( not c == "." ) :
                        bibleStr1.append(c)
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[6]+"!"+str(colorIntensity)+"}"+"\\scriptsize{文理本}"+" & " \
                        +"\\cellcolor{"+colorArr[6]+"!"+str(colorIntensity)+"}"+''.join(bibleStr1)+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of tcv19 to 8th row
                # ----------------------------------------------------
                bibleStr = content_tcv19[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[7]+"!"+str(colorIntensity)+"}"+"\\scriptsize{現中2019}"+" & " \
                        +"\\cellcolor{"+colorArr[7]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of ccbv to 9th row
                # ----------------------------------------------------
                bibleStr = content_ccbv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[8]+"!"+str(colorIntensity)+"}"+"\\scriptsize{當代譯本修訂}"+" & " \
                        +"\\cellcolor{"+colorArr[8]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of msgv to 10th row
                # ----------------------------------------------------
                bibleStr = content_msgv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[9]+"!"+str(colorIntensity)+"}"+"\\scriptsize{Message}"+" & " \
                        +"\\cellcolor{"+colorArr[9]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of jpsv1917 to 11th row
                # ----------------------------------------------------
                bibleStr = content_jpsv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr_hebrew = " ".join(
                                "    ".join(
                                    bibleStr.split("    ")[0:-1])\
                                        .replace("{פ}","\{ פ \}")\
                                        .replace("{ס}","\{ ס \}")\
                                        .replace("{ש}","\{ ש \}")\
                                        .replace("{ר}","\{ ר \}") \
                                        .split(" ")[::-1])
                bibleStr_english = bibleStr.split("    ")[-1]\
                                       .replace("{P}","\{ P \}")\
                                       .replace("{S}","\{ S \}")
                bibleStr = "{\\sblgoodhebrew " + bibleStr_hebrew + " } " + bibleStr_english
                bibleStr = " & " \
                        +"\\cellcolor{"+colorArr[10]+"!"+str(colorIntensity)+"}"+"\\scriptsize{\\makecell{Masoretic \\\\ JPSV1917}}"+" & " \
                        +"\\cellcolor{"+colorArr[10]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n"
                fp.write( bibleStr )
                # ---------------------------------------------------
                # end current sentence
                # ---------------------------------------------------
                bibleStr = "\hline\n"                                 ; fp.write( bibleStr )
                bibleStr = "\end{tabularx}\n"                         ; fp.write( bibleStr )
fp.close()
os.system("cat bible_out/afterword.tex >> ot_out/ot.tex")
os.system("cat bible_out/postfix.tex >> ot_out/ot.tex")
