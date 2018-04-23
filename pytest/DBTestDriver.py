#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Fri Apr 20 00:05:25 2018
@author     : Sourabh
"""

# %%

import sys

sys.path.insert(0, '../../')

from pyutils.db import DatabaseManager
from pyutils.db import Field

# %%

class DBTestDriver:
    
    def __init__(self):
        self.dbm = DatabaseManager()
    
    def testCreateTable1(self):
        print('-' * 20, 'DB Create Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        sector = Field('sector', 'varchar(32)')
        file = Field('file_name', 'varchar(256)')
        schema = [sector, file]
        self.dbm.connectDB(dbLoc)
        self.dbm.deleteTable(table)
        self.dbm.createTable(table, schema)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testCreateTable2(self):
        print('-' * 20, 'DB Create Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'employees'
        empid = Field('empid', 'int(6)', 'not null')
        name = Field('name', 'char(20)', 'not null')
        age = Field('age', 'int(6)')
        gender = Field('gender', 'char(1)')
        income = Field('income', 'float')
        schema = [empid, name, age, gender, income]
        self.dbm.connectDB(dbLoc)
        self.dbm.deleteTable(table)
        self.dbm.createTable(table, schema)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testUpdateTable1(self):
        print('-' * 20, 'DB Update Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        items = [('Aviation', 'S01_A0001.txt'),
             ('Infrastructure', 'S02_A0010.txt'),
             ('Telecommunication', 'S03_A0100.txt'),
             ('Power', 'S04_A1000.txt'),
             ]
        self.dbm.connectDB(dbLoc)
        self.dbm.insertIntoTable(table, items)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testUpdateTable2(self):
        print('-' * 20, 'DB Update Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'employees'
        items = [
                (456789, 'Frodo', 45, 'M', 100000.0),
                (987654, 'Drago', 34, 'M', 10000.0),
                (12345, 'Pixie', 12, 'F', 50000.0),
                (54321, 'Jasper', 22, 'M', 550000.0),
                (765432, 'Roxie', 25, 'F', 100500.0),
                (123456, 'John', 25, 'M', 50000.0),
                (234651, 'Juli', 35, 'F', 75000.0),
                (345121, 'Fred', 48, 'M', 125000.0),
                (562412, 'Rosy', 28, 'F', 52000.0),
                (654221, 'Brandy', 15, 'F', 1100.0),
             ]
        self.dbm.connectDB(dbLoc)
        self.dbm.insertIntoTable(table, items)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testReadTable1(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        self.dbm.connectDB(dbLoc)
        records = self.dbm.fetchAllFromTable(table)
        self.dbm.closeDB()
        print('Result:')
        if records is not None:
            for record in records:
                print(record)
    
    def testReadTable2(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'employees'
        self.dbm.connectDB(dbLoc)
        records = self.dbm.fetchAllFromTable(table)
        self.dbm.closeDB()
        print('Result:')
        if records is not None:
            for record in records:
                print(record)
    
    def testReadTableWithQuery(self):
        print('-' * 20, 'DB Read Test With Query', '-' * 20)
        dbLoc = 'testdb.sqlite'
        query = '''
        select * from articles
        where sector is not 'Power'
        order by file_name desc
        '''
        self.dbm.connectDB(dbLoc)
        self.dbm.executeQuery(query)
        records = self.dbm.fetchAll()
        self.dbm.closeDB()
        print('Result:')
        if records is not None:
            for record in records:
                print(record)
    
    def testListTables(self):
        print('-' * 20, 'DB List Of Tables Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        self.dbm.connectDB(dbLoc)
        tables = self.dbm.listTables()
        self.dbm.closeDB()
        print('Result:')
        if tables is not None:
            for table in tables:
                print(table)
    
    def testExportAllTables(self):
        print('-' * 20, 'DB Export All Tables Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        self.dbm.connectDB(dbLoc)
        savedFiles = self.dbm.exportDB()
        self.dbm.closeDB()
        if savedFiles is not None:
            print('Following files were created after export:')
            for filePath in savedFiles:
                print(filePath)
    
    def testExportSomeTables(self):
        print('-' * 20, 'DB Export Some Tables Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        self.dbm.connectDB(dbLoc)
        savedFiles = self.dbm.exportDB(tables=['employees'])
        self.dbm.closeDB()
        if savedFiles is not None:
            print('Following files were created after export:')
            for filePath in savedFiles:
                print(filePath)

if __name__ == '__main__':
    dbtd = DBTestDriver()
    dbtd.testCreateTable1()
    print()
    dbtd.testCreateTable2()
    print()
    dbtd.testUpdateTable1()
    print()
    dbtd.testUpdateTable2()
    print()
    dbtd.testReadTable1()
    print()
    dbtd.testReadTable2()
    print()
    dbtd.testReadTableWithQuery()
    print()
    dbtd.testListTables()
    print()
    #dbtd.testExportAllTables()
    #print()
    dbtd.testExportSomeTables()
    print()
