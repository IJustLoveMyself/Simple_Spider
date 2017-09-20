#!/usr/bin/env python
# -*- coding:utf-8 -*-


from URLManager import URLManager
from HtmlParser import HtmlParser
from HtmlDownload import HtmlDownload
from DataManager import DataManager

# url = 'http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2?limit=30&index=1&offset=0#gotoList'
class MainSpider:
    def __init__(self):
        self.urlmanager = URLManager()
        self.htmlparser = HtmlParser()
        self.htmldownload = HtmlDownload()
        self.datamanager = DataManager()
        self.spider()
    def spider(self):
        for i in range(1,4):
            url = 'http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2?limit=30&index='+str(i)+'&offset=0#gotoList'
            html = self.htmldownload.htmlDownload(url)
            urls = self.htmlparser.url_Get(html)
            if urls != None:
                self.urlmanager.add_new_urls(urls)
        with open('baike.csv','wb') as fd:
            while self.urlmanager.has_new_url():
                url = self.urlmanager.get_new_url()
                html = self.htmldownload.htmlDownload(url)
                data = self.htmlparser.data_Get(url,html)
                if data != None:
                    self.datamanager.dataManager(fd,data)
        fd.close()
app = MainSpider()
