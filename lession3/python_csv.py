#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:
    def __init__(self):
        url = "http://www.quanshuwang.com/book/9/9055/"
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
        self.getInfo(url,header)

    def getInfo(self,url,header):
        chap_list = []
        info_list=["chapname","url"]
        html = requests.get(url,headers = header)
        soup = BeautifulSoup(html.content,"lxml")
        print soup.encode('gbk')
        name_info = soup.find_all("div",class_ = "chapName")[0]
        print name_info
        name = name_info.strong.string
        chap_info = soup.find_all("div",class_ = "clearfix dirconone")[0]
        chap_all = chap_info.find_all("a")
        for chap in chap_all:
            # chapname = chap.string.encode('utf-8') #编码
            chapname = chap.string
            chapurl = "http://www.quanshuwang.com/book/9/9055/" + chap["href"]
            a = (chapname,chapurl) #将信息存储到元组中
            chap_list.append(a) #将信息添加到列表中，因为写入的时候对象要是列表
            del a  #因为元组的值不能改变，所以需要删了重新建立
        print chap_list
        with open(name+'.csv','wb') as fd:
            f_csv = csv.writer(fd)
            f_csv.writerow(info_list) #写入每一列 的头
            f_csv.writerows(chap_list)#写入每一列的信息
        fd.close()
app = Spider()