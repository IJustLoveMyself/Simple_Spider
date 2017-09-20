#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json


class Spider:
    def __init__(self):
        url = "http://www.quanshuwang.com/book/9/9055/"
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
        self.getInfo(url,header)

    def getInfo(self,url,header):
        chap_list = []
        a={}
        html = requests.get(url,headers = header)
        soup = BeautifulSoup(html.content,"lxml")
        print soup.encode('gbk')
        name_info = soup.find_all("div",class_ = "chapName")[0]
        print name_info
        name = name_info.strong.string
        chap_info = soup.find_all("div",class_ = "clearfix dirconone")[0]
        chap_all = chap_info.find_all("a")
        # fd = open(name+'.json','wb')
        for chap in chap_all:
            a['chapname'] = chap.string
            a["url"] = "http://www.quanshuwang.com/book/9/9055/" + chap["href"]
            chap_list.append(a)
            # json.dump(chap_list, fp = fd)
        with open(name+'.json','wb') as fd:
            json.dump(chap_list,fp=fd)
        fd.close()
app = Spider()