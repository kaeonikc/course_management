#!/usr/bin/env python

import re
from read_mdfile import readfile

class tex:
    def __init__(self, texinfo):
        # self.texinfo = texinfo
        self.texinfo = []
        for k in texinfo:
            self.texinfo.append(k)
        # print(self.texinfo)
        # self.name = 'name'
        # self.author = 'Chakkrit Kaeonikhom'
        # self.texclass = texclass
   
    # def read_info(self, info):
    #     self.infoname = info
    #     try:
    #         with open(self.infoname, 'r', encoding='utf8') as rd:
    #             rdd = rd.readlines()
    #     except:
    #         rdd = []
    #         print('Error: file "%s" not found' % self.infoname)
    #         exit()
    #     return rdd
   
       # TODO 
    def add_lecture_contents(self):
        content = 'lect01.tex'
        content2 = 'lect02.tex'
        secs = [
            fr'\input{{{content}}}',
            fr'\input{{{content2}}}'
        ]
        # print(secs)
        return secs
        
    def append_main_TeX(self):
        txinfo = {}
        texkeys = ['texclass', 'title', 'author']
        texvals = self.texinfo
        # texdt = zip(texkeys, texvals)
        txinfo.update(zip(texkeys, texvals))
            
        # print(txinfo)
        lect = self.add_lecture_contents()[::-1]
        # print(lect)
        #TODO

        # lect = r'\input{lect01.tex}'
        lines = [fr'\documentclass[11pt,a4paper]{{{txinfo["texclass"]}}}',
                r'\input{../preamble.tex}',
                fr'\title{{{txinfo["title"]}}}',
                fr'\author{{{txinfo["author"]}}}',
                r'\begin{document}',
                r'\maketitle',
                r'\tableofcontents',
                fr'%---- begin lectures ----',
                fr'%---- end lectures ----',
                r'\end{document}'
        ]
        linesidx = [i for i, word in enumerate(lines) if re.search('end lecture',word)][0]
        for x in lect:
            lines.insert(linesidx, x)
        # print(lines)
        return lines # return main TeX with 'title'

