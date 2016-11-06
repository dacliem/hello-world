# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 00:25:31 2016

@author: LiemLD
"""


import pandas as pd
import os.path
  
pathName = "D:/DSG/Git/hello-world/Time Series Analysis/"
fileName = "GDNA_MeasuredValues_ProductE_20160701.csv"
filePath = os.path.join(pathName, fileName)   
frame_Measured_E_0701 = pd.read_csv(filePath)


