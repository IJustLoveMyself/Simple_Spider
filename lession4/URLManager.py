#!/usr/bin/env python
# -*- coding:utf-8 -*-

class URLManager:
    def __init__(self):
        self.new_urls = set()  #为爬取URL集合
        self.old_urls = set()  #已爬取URL集合
    def has_new_url(self):
        return self.new_urls_size()!=0
    def add_new_url(self,url):
        if url is None:
            return 0
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0 :
            return 0
        for url in urls:
            self.add_new_url(url)
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def new_urls_size(self):
        return len(self.new_urls)
    def old_urls_size(self):
        return len(self.old_urls)