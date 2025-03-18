#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import os

class ReadFileLists():
    """
    ----------------------------------
    This is help for reading CSV:
    econding: gbk,gb18030,UTF-16LE...
    delimiter: None,\\t...
    engine:python,c...
    ----------------------------------
    """
    def __init__(self,dir,suffix):
        self.dir = dir
        self.suffix = suffix
        
    def getFiles(self):# 查找根目录，文件后缀 
        res = []
        for root, directory, files in os.walk(self.dir):# =>当前根,根下目录,目录下的文件
            for filename in files:
                name,suf = os.path.splitext(filename)# =>文件名,文件后缀
                if suf == self.suffix:
                    res.append(os.path.join(root,filename))# =>吧一串字符串组合成路径
        return res

class ReadFiles(ReadFileLists):#读取Excel文件
    def __init__(self,dir,suffix):
        super().__init__(dir,suffix)
         
    def readFileNameExcel(self,Filename):
        filelist = []
        data = []
        for file in super().GetFiles():
            if Filename in file:
                filelist.append(file)
        for file in filelist:
            data.append(pd.read_excel(file))
        return pd.concat(data)
         
    def readFileNameCSV(self,Filename,Encoding,Engine,Skiprows,Delimiter):#读取文件
        filelist = []
        data = []
        for file in super().GetFiles():
            if Filename in file:
                filelist.append(file)
        for file in filelist:
            data.append(pd.read_csv(file,encoding=Encoding,delimiter=Delimiter,engine=Engine,skiprows=Skiprows))

        return pd.concat(data)



