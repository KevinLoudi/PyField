# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 10:33:17 2018

@author: kevin
"""

import csv

def Read_with_Delim(file):
    with file:
        reader = csv.reader(file, delimiter=",")
        
        for row in reader:
            for e in row:
                print(e)
                
def Read_with_DictKey(file):
    with file:
        reader = csv.DictReader(file)
        
        for row in reader:
            print(row['min'], row['avg'], row['max'])
        
        

if __name__ == '__main__': 
    f = open('numbers.csv')
#    Read_with_Delim(f)
    Read_with_DictKey(f)