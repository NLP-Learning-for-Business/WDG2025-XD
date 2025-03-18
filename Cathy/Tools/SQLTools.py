#!/usr/bin/env python
# coding: utf-8

# In[67]:


from sqlalchemy import create_engine  
import pymysql
import pandas as pd
import MySQLdb

class ConnectSQL():
    """
    ----------------------------------
    UpdateSQL中query里面填写SQL语句
    #A = ConnectSQL('yejin4','carlkin03','rm-uf67x3t1e92rs91il2o.mysql.rds.aliyuncs.com','3306','normal_business')
    #A.UpLoadSQL(Table,'contactvolume_test','append')
    #A.DownLoadSQL('contactvolume_test')
    #A.UpdateSQL('UPDATE `contactvolume_test` SET `Total RFC Contacts`  = 10000 WHERE `Date` = "2021-06-25 00:00:00"')
    #A.SelectSQL('SELECT * FROM contactvolume_test WHERE Date>"2021-06-20 00:00:00"')
    ----------------------------------
    """
    def __init__(self,root,passwd,host,port,db):
        self.host = host
        self.port = port
        self.root = root
        self.passwd = passwd
        self.db = db
    #用Created Engine的方式上传数据
    def upLoadSQL(self,Table,Sql_Table,UpLoad_Type):
        engine = create_engine('mysql://'+self.root+':'+self.passwd+'@'+self.host+':'+self.port+'/'+self.db+'?charset=utf8mb4')
        try:
            Table.to_sql(Sql_Table, engine, if_exists=UpLoad_Type,index=None)
        except Exception:
            Table.to_sql(Sql_Table, engine, if_exists=UpLoad_Type,index=None)
    #读取数据库完整表单数据
    def downLoadSQL(self,Table):
        engine = create_engine('mysql://'+self.root+':'+self.passwd+'@'+self.host+':'+self.port+'/'+self.db+'?charset=utf8mb4')
        return pd.read_sql(Table,engine)
    #SQL更新数据
    def updateSQL(self,query):
        db = MySQLdb.connect(
            host=self.host,
            port=int(self.port), 
            user=self.root, 
            passwd=self.passwd, 
            db=self.db,
            charset='utf8mb4')
        cursor = db.cursor()
        try:
            cursor.execute(query)
            db.commit()
        except:
            db.rollback()
        cursor.close()
        # 关闭数据库连接
        db.close()
    def selectSQL(self,query):
        db = MySQLdb.connect(
            host=self.host,
            port=int(self.port), 
            user=self.root, 
            passwd=self.passwd, 
            db=self.db,
            charset='utf8mb4')
        cursor = db.cursor()
        Table = []
        Columns = []
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            #获取表数据
            for row in rows:
                Table.append(row)
            # 获取表头
            for item in cursor.description:
                Columns.append(item[0])
        except:
            db.rollback()
        cursor.close()
        # 关闭数据库连接
        db.close()
        Table = pd.DataFrame(Table)
        Table.columns=Columns
        return Table
    
    def readSQL(self,query):
        db = MySQLdb.connect(
            host=self.host,
            port=int(self.port), 
            user=self.root, 
            passwd=self.passwd, 
            db=self.db,
            charset='utf8mb4')
        cursor = db.cursor()
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
        except:
            db.rollback()
        cursor.close()
        # 关闭数据库连接
        db.close()
        return rows

