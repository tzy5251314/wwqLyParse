#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>


import urllib.request,io,os,sys,json,re

from pyquery.pyquery import PyQuery

try:
    from .. import common
except Exception as e:
    import common


class BaiduLinkUrlHandle(common.UrlHandle):

    filters = ['^(http|https)://v.baidu.com/link']

    def urlHandle(self,input_text):
        html = PyQuery(common.getUrl(input_text))
        a = html.children('a')
        a = PyQuery(a)
        url = a.attr("href")
        print('urlHandle:"'+input_text+'"-->"'+url+'"')
        return url
    
class MgtvUrlHandle(common.UrlHandle):
    #http://www.hunantv.com/v/3/45732/f/1872791.html
    filters = ['^(http|https)://www.hunantv.com']

    def urlHandle(self,input_text):
        url = input_text.replace("hunantv.com","mgtv.com")
        print('urlHandle:"'+input_text+'"-->"'+url+'"')
        return url
    
class LetvUrlHandle(common.UrlHandle):
    #http://www.hunantv.com/v/3/45732/f/1872791.html
    filters = ['^(http|https)://www.letv.com']

    def urlHandle(self,input_text):
        url = input_text.replace("letv.com","le.com")
        print('urlHandle:"'+input_text+'"-->"'+url+'"')
        return url