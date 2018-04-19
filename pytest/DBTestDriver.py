#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Fri Apr 20 00:05:25 2018
@author     : Sourabh
"""

# %%

import sys

# add modules path before importing them
sys.path.insert(0, '../../')

from pyutils.db import DatabaseManager

class DBTestDriver:
    
    def __init__(self):
        self.dbm = DatabaseManager()
    
    def testDBRead(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        fileLoc = 'test.db'
        self.dbm.connectDB(fileLoc)
        query = 'select * from EMPLOYEE'
        self.dbm.executeQuery(query)
        records = self.dbm.fetchAll()
        if records is not None:
            print(records)
        self.dbm.closeDB()

if __name__ == '__main__':
    dbtd = DBTestDriver()
    dbtd.testDBRead()
    print()
    pass
