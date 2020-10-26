#!/usr/bin/python3
# use the command to apply to raw txt
# %s/[0-9]\+://g
# %s/.Listen to .*Chapter.*Chapter.*//g
import os
import re
_ = os.system('clear')
fname = '2Ch.txt'
rawfname = fname[:3]+'_raw.txt'
_ = os.system('mv '+fname+' '+rawfname)
fp = open(rawfname,'r')
lines = fp.readlines()
fp.close()

useful_string = ''
verse_num_prev = 1
verse_num_curr = 1
chapter_num = 1
for line in lines:
    line = line.strip()
    res = re.split('(\d+)', line)
    for r in res:
        if len(r) > 0:
            if re.match(r'([0-9]+)', r):
                verse_num_curr = int(r.strip())
                if (verse_num_curr < verse_num_prev):
                    print(verse_num_curr, verse_num_prev)
                    chapter_num = chapter_num + 1
                verse_num_prev = verse_num_curr
                useful_string = useful_string + str(chapter_num) + '.' + r.strip() + ' '
            else:
                useful_string = useful_string + r.strip() + '\n'
print(useful_string)
fp = open(fname,'w')
fp.write(useful_string)
fp.close()
