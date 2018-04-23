# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

def connectdb():
    db = pymysql.connect(host='localhost',user='root',passwd='',db='test1',charset='utf8')
    return db

def createtable(db):
    cursor = db.cursor()
    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS ARTICLES")

    sql = """CREATE TABLE ARTICLES (
             author CHAR(20) ,
             pageview INT,
             id INT PRIMARY KEY, 
             reply INT,
             seed INT DEFAULT "2" ,
             seedTime INT, 
             sourceID CHAR(20) UNIQUE,
             title CHAR(50))"""
    cursor.execute(sql)

def insertdb(db,sql):
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

def closedb(db):
    db.close()



class YingdiPipeline(object):
    def __init__(self):
        self.db = connectdb()
        createtable(self.db)

    def process_item(self, item, spider):

        l=dict(item)
        sql = "INSERT INTO ARTICLES(author,pageview,id,reply,seed,seedTime,sourceID,title) " \
              "VALUES('%s', '%s', '%d', '%d', '%d','%d','%s','%s')" % \
              (l["author"], l["pageview"], l["id"], l["reply"], l["seed"], l["seedTime"], l["sourceID"], l["title"])
        insertdb(self.db, sql)
        return item



    def close_spider(self,spider):
        closedb(self.db)
