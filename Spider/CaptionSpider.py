# -*- coding: UTF-8 -*-
# __author__ = 'xiewenjing'

import urllib
import urllib2
from datetime import datetime
import requests


def spider_zimuku(data):
    # https://www.zimuku.cn/search?q=使女的故事
    url = "https://www.zimuku.cn/search"
    content = urllib.urlopen(url, data)
    return content


if __name__ == '__main__':
    print "Start!"
    start = datetime.now()
    print start

    movie_name = [{'q': '使女的故事'}]
    for x in range(len(movie_name)):
        data = bytes(urllib.urlencode(movie_name[x]))
        print spider_zimuku(data)

    print "The end"
    end = datetime.now()
    print str(end - start)
