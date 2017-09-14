#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib

class Spider:
    def __init__(self):
        url = "https://www.qiushibaike.com/imgrank/"
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
        self.downLoad(url,header)
    def getHtml(self,url,header):
        req = urllib2.Request(url,headers = header)
        respon = urllib2.urlopen(req)
        html = respon.read()
        return html
    def test(self,url,header):
        html = self.getHtml(url,header)
        soup = BeautifulSoup(html, "lxml")
        print soup.encode('gbk')
        return soup.find_all('img', class_="illustration")
        # for img_list in soup.find_all('img',class_="illustration"):
        #     # print img_list.get('alt')
        #     # print img_list.get('src')
        #     title = img_list.get('alt')+'.jpg'
        #     url = 'https:'+img_list.get('src')
        #     urllib.urlretrieve(url,title)
    def downLoad(self,url,header):
        img_list = self.test(url,header)
        for img in img_list:
            print type(img)
            title = img.get('alt')+'.jpg'
            print type(title)
            url = 'https:'+img.get('src')
            urllib.urlretrieve(url,title)

app = Spider()