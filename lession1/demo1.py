#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

novel={}
usr_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
header={'User-Agent':usr_agent}
first_url="http://www.quanshuwang.com/book/9/9055/"
repom=urllib2.urlopen(first_url)
html=repom.read().decode('gbk')

novel_info=re.findall(r'<div class="chapName"><span class="r">.*?</span><strong>(.*?)</strong><span class="l">',html)
novel['title']=novel_info[0]
novel_info=re.findall(r'<div class="chapName"><span class="r">(.*?)</span><strong>',html)
novel['autor']=novel_info[0]

novel_info=re.findall(r'<DIV class="clearfix dirconone">(.*?)</div>',html,re.S)
novel_info=re.findall(r'<a (.*?)</a>',novel_info[0])

fd=open((novel['title']+".txt"),'a')
for info in novel_info:
    chapter_url = first_url + re.findall(r'href="(.*?)"',info)[0]
    chapter_title = re.findall(r'title="(.*?)"',info)[0]+'\r\n'
    fd.write(chapter_title)
    request = urllib2.Request(chapter_url, headers=header)
    repom=urllib2.urlopen(request)
    html2=repom.read().decode('gbk')
    html_data=re.findall(r'<div class="mainContenr"   id="content"><script type="text/javascript">.*?</script>'
                     r'(.*?)<script type="text/javascript">',html2,re.S)
    html_data = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />', html_data[0])
    for data in html_data:
        w_data='  '+data+'\n'
        fd.write(w_data)
        w_data=''
    print chapter_title
fd.close()

print 'ok'