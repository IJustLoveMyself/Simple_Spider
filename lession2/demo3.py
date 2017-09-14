#!/usr/bin/env python
# -*- coding:utf-8 -*-


import urllib
import urllib2
from lxml import etree

class Spider:
    def __init__(self):
        url = "https://www.qiushibaike.com/imgrank/"
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
        self.downLoad(url,header)


    def getHtml(self,url,header):
        request = urllib2.Request(url,headers = header)
        res = urllib2.urlopen(request)
        html = res.read()
        return html

    def downLoad(self,url,header):
        html_qiubai = self.getHtml(url,header)
        html = etree.HTML(html_qiubai)
        print etree.tostring(html)
        result = html.xpath('//img')
        # html = etree.parse(html)
        # result = etree.tostring(html)
        for img in result:
            if len(img.xpath('./@class'))!= 0:
                title = img.xpath('./@alt')[0]+'.jpg'
                url = 'https:'+img.xpath('./@src')[0]
                urllib.urlretrieve(url,title)
app = Spider()