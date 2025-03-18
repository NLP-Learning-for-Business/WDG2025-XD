#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
import pandas as pd
import datetime,time,os

root = tk.Tk()
root.withdraw()
Folderpath = filedialog.askdirectory() #获得选择好的文件夹
# Date = Folderpath.split('/')[-1]
# Date2 = datetime.date(int(str(datetime.datetime.now().year)), int(Date.split('.')[0]), int(Date.split('.')[1])).strftime('%Y-%m-%d')
# #Date2 = datetime.date(2021, int(Date.split('.')[0]), int(Date.split('.')[1])).strftime('%Y-%m-%d')
# Date4 = Date2.split('-')[0] + Date2.split('-')[1] + Date2.split('-')[2]
Path_list = os.listdir(Folderpath)
def getfile(keywords):
    for filename in Path_list:
        if keywords in filename:
            return Folderpath + "/" + filename

