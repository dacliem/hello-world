# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 00:25:31 2016

@author: LiemLD
"""

import csv

f_GDNA_MeasuredValues_ProdE_20160701  = open('D:/DSG/Git/hello-world/Time Series Analysis/GDNA_MeasuredValues_ProductE_20160701.csv', "rb")
reader_GDNA_MeasuredValues_ProdE_20160701  = csv.reader(f_GDNA_MeasuredValues_ProdE_20160701)

for row in reader_GDNA_MeasuredValues_ProdE_20160701:   # iterates the rows of the file in orders
        print row    # prints each row

f_GDNA_MeasuredValues_ProdE_20160701.close()

