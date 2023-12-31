#!/usr/bin/env python
"""
lectures.py is for creating lecture note template in LaTeX
"""
import os
import argparse
from pathlib import Path
import pathlib
from appendtex import tex

def parse_args():
    parser = argparse.ArgumentParser(description=
    """
    Create a LaTeX-lecture note template from a given name arguments.
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
    def __init__(self, name):
        self.dir_name = 'lecture_notes'
        self.dir_img_name = 'images'
        self.name = name
        
    def mk_dir(self):
        """Create lecture note directories"""
        impath = os.path.join(self.dir_name, self.name, self.dir_img_name)
        p = Path(impath)
        p.mkdir(exist_ok=True, parents=True)

    # def mk_maintex_path(self):
    #     #---- Create main tex path ----
    #     self.texdir = os.path.join(self.dir_name, self.name)
    #     self.mk_dir()
    #     texpath = os.path.join(self.texdir, 'main_'+self.name+'.tex')

        # return texpath
    
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
        try:
            if parse_args().overwrite:
                Path(file_path).touch(exist_ok=True)
            else:
                Path(file_path).touch(exist_ok=False)
        except FileExistsError:
            print(pathlib.PurePath(file_path).name + ' already exists')
    
    def new_lecture(self):
        # self.mk_dir()
        texclass = 'memoir'
        lecture_title = self.name
        author = 'ckk'
        self.mk_dir()

        self.texdir = os.path.join(self.dir_name, self.name)
        main_filepath = os.path.join(self.texdir, 'main_'+self.name+'.tex')

        texinfo = [texclass, lecture_title, author]
        
        lns = tex(texinfo).append_main_TeX()
        filecontent = '\n\n'.join(lns)
        
        self.write_TeX(main_filepath, filecontent)
        
        # create file 'lect01.tex'
        content_path = os.path.join(self.texdir, 'lect01.tex')
        self.write_TeX_content(content_path)

        
if __name__=="__main__":
    nx = parse_args().course_name
    for i in nx:
        Lectures(i).new_lecture()
