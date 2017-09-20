#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from HtmlDownload import HtmlDownload

class HtmlParser:
    def url_Get(self,html):
        urls = []
        soup = BeautifulSoup(html,'lxml')
        get_info = soup.find_all('div',class_ = "grid-list grid-list-spot")
        if len (get_info) != 0:
            get_url = get_info[0].find_all('div',class_ = 'photo')
            for info in get_url:
                url = 'http://baike.baidu.com'+ info.a['href']
                urls.append(url)
            return urls
        return None
    def data_Get(self,url,html):
        data = [url]
        print "data=",url
        soup = BeautifulSoup(html, 'lxml')
        #判断页面是否正确，也有可能页面找不到，响应的是错误的请求页面
        if soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title") != None:
            title = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find('h1').get_text().encode('utf-8')
            data.append(title)
            #判断是否有简介
            if soup.find('div',class_ ="lemma-summary") != None:
                text = soup.find('div',class_ ="lemma-summary").get_text().encode('utf-8')
                data.append(text)
            else:
                data.append("空缺")
            return data
        return None
