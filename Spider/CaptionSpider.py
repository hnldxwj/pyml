# -*- coding: UTF-8 -*-
# __author__ = 'xiewenjing'

import urllib
import urllib2
from datetime import datetime
import requests
import re


def spider_assrt(param):
    # http://assrt.net/sub/?searchword=使女的故事+s02e11
    url = "http://assrt.net/sub/?searchword={}&sort=rank".format(param)
    print url
    response = urllib.urlopen(url)
    content = response.read()
    print content
    href = re.findall(r"/xml/sub/\d+/\d+\.xml", content)
    return href


def spider_zimuku(param):
    # https://www.zimuku.cn/search?q=使女的故事
    url = "https://www.zimuku.cn/search?q={}".format(param)
    print url
    response = urllib.urlopen(url)
    content = response.read()
    return content


if __name__ == '__main__':
    print "Start!"
    start = datetime.now()
    print start

    movie_name = ['使女的故事']
    for x in range(len(movie_name)):
        print spider_assrt(movie_name[x])

    print "The end"
    end = datetime.now()
    print end
    print str(end - start)
