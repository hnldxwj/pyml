# -*- coding: UTF-8 -*-
# __author__ = 'xiewenjing'

import urllib
import urllib2
from datetime import datetime
import requests


def spider_zimuku(param):
    # https://www.zimuku.cn/search?q=使女的故事
    url = "https://www.zimuku.cn/search?q={}".format(param)
    print url
    response = urllib.urlopen(url)
    content=response.read()
    return content

if __name__ == '__main__':
    print "Start!"
    start = datetime.now()
    print start

    movie_name = ['使女的故事']
    for x in range(len(movie_name)):
        print spider_zimuku(movie_name[x])

    print "The end"
    end = datetime.now()
    print str(end - start)
