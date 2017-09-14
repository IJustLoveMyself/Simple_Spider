#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import re
import sys
import urllib


reload(sys)
sys.setdefaultencoding('utf8')

class Spider:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        self.first_url = "https://www.qiushibaike.com/imgrank/"
        self.getImage(self.first_url,self.headers)

    def getHtml(self,url,headers):
        request = urllib2.Request(url,headers = headers)
        respon = urllib2.urlopen(request)
        html = respon.read()
        return html
    def saveImage(self,Imagename,data):
        fd = open((Imagename+".jpg"), 'wb')
        fd.write(data)

    def getImage(self, url, header):
        html = self.getHtml(url, headers=header)
        info = re.findall(r'<img (.*?)class', html)
        for image in info:
            image_url = "https:"+ re.findall(r'src="(.*?)"', image)[0]
            name = re.findall(r'alt="(.*?)"',image)
            print type(name[0])
            name = name[0].encode("gbk")
            print name.decode('gbk')
            # data=self.getHtml(image_url,headers=header)
            # self.saveImage(name,data)
            urllib.urlretrieve(image_url,name+'.jpg')
spider = Spider()

