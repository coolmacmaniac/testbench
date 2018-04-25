#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 00:41:21 2018
@author     : Sourabh
"""

# %%

import sys

# add modules path before importing them
sys.path.insert(0, '../../')

from pyutils.io import FileManager as fm

class FileTestDriver:
    
    def __init__(self):
        pass
    
    def testFileRead(self):
        print('-' * 20, 'Read Test', '-' * 20)
        fileLoc = 'Sample.txt'
        contents = fm.read(fileLoc)
        if contents is not None:
            print(contents)
    
    def testFileWrite(self):
        print('-' * 20, 'Write Test', '-' * 20)
        fileLoc = 'Sample.txt'
        contents = 'This is purely a dummy text.\nModi lies...\n'
        fm.write(fileLoc, contents)
    
    def testCSVFileRead(self):
        print('-' * 20, 'Read CSV Test', '-' * 20)
        fileLoc = 'employees.csv'
        headers, records = fm.readCSV(fileLoc)
        if headers is not None:
            print(headers)
        if records is not None:
            for row in records:
                print(row)
    
if __name__ == '__main__':
    ftd = FileTestDriver()
#    ftd.testFileRead()
#    print()
#    ftd.testFileWrite()
#    print()
    ftd.testCSVFileRead()
    print()
