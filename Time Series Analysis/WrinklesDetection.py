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

============
import pandas as pd
import os.path
  
pathName = "D:/LiemLD/DSG/Toppan-Gunma/From_Toppan/Sensors_data/GDNA_GS52/Pre-processed/CSV/"
fileName = "GDNA_SettingValues_E_EN.csv"
filePath = os.path.join(pathName, fileName)   
dfSetting = pd.read_csv(filePath)
dates = pd.to_datetime(dfSetting['S_Timestamp'])
dfSetting['S_Timestamp'] = dates
