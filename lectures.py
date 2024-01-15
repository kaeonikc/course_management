#!/usr/bin/env python

import os
import argparse
from pathlib import Path
import pathlib
from appendtex import tex

def parse_args():
    parser = argparse.ArgumentParser(description=
    """
    Create a LaTeX-lecture note template from a given name.
    ------------------------------
    Eample: python lectures.py Foo 
    
    This will basically create the file 'main_Foo.tex' template inside Foo directory.
    The Foo directory will be created inside 'lecture_notes' directory.
    """, formatter_class=argparse.RawTextHelpFormatter, prog='lecture.py')

    parser.add_argument('course_name', nargs='+', help='Course name.')
    parser.add_argument('--overwrite', action='store_true', help='overwrite main tex file if exist')
    args = parser.parse_args()
    
    return args

class Lectures:
    """
    This module is for creating lecture note template in LaTeX.
    
    Attributes
    ----------
    name: str
        name of the being created directory and of the course.
    
    Methods
    ----------
    new_lecture():
        create a course-name directory in lecture_note directory, 
        create a main-tex file template and prerequisite LaTeX command in the file.
    
    """
    def __init__(self, name):
        self.dir_name = 'lecture_notes'
        self.dir_img_name = 'images'
        self.name = name
        self.texclass = 'memoir'
        self.lecture_title = name
        self.author = 'ckk'
        
    def mk_dir(self):
        """Create lecture note directories"""
        impath = os.path.join(self.dir_name, self.name, self.dir_img_name)
        p = Path(impath)
        p.mkdir(exist_ok=True, parents=True)
    
    def mk_mdfile(self, lec_content):
        mdpath = os.path.join(self.dir_name, self.name, self.name+'.md')
        try:
            Path(mdpath).touch(exist_ok=False)
            Path(mdpath).write_text(lec_content)
        except FileExistsError:
            print(pathlib.PurePath(mdpath).name + ' already exists')

    
    #TODO
    # read lecturename.md and append content in main_lecture.tex    
    
    def write_TeX(self, file_path, file_content):
        """
            This function is to create main-tex file, 
            and write prerequisite LaTeX code in the file.
            
            Args
            ----------
            file_path: str
            file_content: str
        """ 
        try:
            if parse_args().overwrite:
                Path(file_path).touch(exist_ok=True)
                Path(file_path).write_text(file_content)
                print('Overwrote %s!.' %self.name)
            else:
                Path(file_path).touch(exist_ok=False)
                Path(file_path).write_text(file_content)
                print('Lecture note on %s created.' %self.name)
        except FileExistsError:
            print(pathlib.PurePath(file_path).name + ' already exists')
    
    def write_TeX_content(self, file_path):
        # Create files corresponding to the code in the main-tex body
        try:
            if parse_args().overwrite:
                Path(file_path).touch(exist_ok=True)
            else:
                Path(file_path).touch(exist_ok=False)
        except FileExistsError:
            print(pathlib.PurePath(file_path).name + ' already exists')
    
    def new_lecture(self):

        self.mk_dir()

        texdir = os.path.join(self.dir_name, self.name)
        main_filepath = os.path.join(texdir, 'main_'+self.name+'.tex')

        texinfo = [self.texclass, self.lecture_title, self.author]
        
        lns = tex(texinfo).append_main_TeX()
        filecontent = '\n\n'.join(lns)
        
        self.write_TeX(main_filepath, filecontent)
        
        content_path = os.path.join(texdir, 'lect01.tex')
        self.write_TeX_content(content_path)

        
if __name__=="__main__":
    nx = parse_args().course_name
    for i in nx:
        Lectures(i).new_lecture()
