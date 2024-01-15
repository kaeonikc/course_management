#!/usr/bin/env python

import re
class tex:
    """
    This module is to create LaTeX code, 
    and appending the code to main LaTeX file.
    
    Attributes
    ----------
    texinfo: list
        list of strings with length three. 
        It must be [<texclass>, <course name>, <author>]
        
        texclass: str
            a LaTeX class e.g., article, memior, report etc.
        course name: str
            title of lecture
        author: str
            name of the author
    
    
    Methods
    ----------
    append_main_TeX():
        return a list of lines that to append 
        in the main LaTeX file. 
    
    """
    def __init__(self, texinfo):
        """
        Constructs all the necessary attributes for the tex object.

        Args
        ----------
            texinfo (list): list must be [<texclass>, <course name>, <author>]
        
            texclass: str
                a LaTeX class e.g., article, memior, report etc.
            course name: str
                title of lecture
            author: str
                name of the author
        """
        self.texinfo = []
        for k in texinfo:
            self.texinfo.append(k)
   
    def add_lecture_contents(self):
        tex_body = ['lec1','lec2','lec3']
        secs = []
        for k in tex_body:
            secs.append('\input{'+k+'}')
        
        return secs
        
    def append_main_TeX(self):
        txinfo = {}
        texkeys = ['texclass', 'title', 'author']
        texvals = self.texinfo
        txinfo.update(zip(texkeys, texvals))
            
        lect = self.add_lecture_contents()

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

        return lines

