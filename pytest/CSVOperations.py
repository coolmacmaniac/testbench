#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Mon Apr 23 22:15:22 2018
@author     : Sourabh
"""

# %%

import csv, sys

# %%

class CSVOperations:
    
    def readCSV(self, filepath):
        with open(filepath, mode='rt', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel')
            try:
                for row in reader:
                    print(row)
            except csv.Error as e:
                print('file {}, line {}: {}'.format(
                        filepath, reader.line_num, e))
                raise e
    
    def writeCSV(self, filepath, headers, rows):
        with open(filepath, mode='wt', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel')
            try:
                writer.writerow(headers)
                writer.writerows(rows)
            except csv.Error as e:
                print('file {}, line {}: {}'.format(
                        filepath, writer.line_num, e))
                raise e

if __name__ == '__main__':
    csvop = CSVOperations()
    
    option = sys.argv[1]
    
    if option != '-r' and \
        option != '-w' and \
        option != '-rw' and \
        option != '-wr' :
        sys.exit('Usage: python {} -[r|w|rw\wr] {}'.format(
                        sys.argv[0], ' '.join(sys.argv[2:])))
    
    if 'w' in option:
        for filepath in sys.argv[2:]:
            print('-' * 20, 'Writing :', filepath, '-' * 20)
            headers = ['name', 'age']
            rows = [
                    ['Sourabh', '32'],
                    ['Saksham', '2'],
                    ['¡™¢∞§¶•ªºœ∑´®†¥', '55']
                    ]
            csvop.writeCSV(filepath, headers, rows)
            print('Done')
    
    if 'r' in option:
        for filepath in sys.argv[2:]:
            print('-' * 20, 'Reading :', filepath, '-' * 20)
            csvop.readCSV(filepath)
