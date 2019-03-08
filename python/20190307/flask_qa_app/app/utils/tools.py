#!/usr/bin/env python
# encoding: utf-8
from random import choice

import requests
from lxml import etree

headers = {}
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
headers['Connection'] = 'keep-alive'
headers['Upgrade-Insecure-Requests'] = '1'
headers['User-Agent'] = \
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'


def fetch_question(url):
    """
    从知否(segmentfault.com)爬取热门问题
    :param url:
    :return:
    """
    r = requests.get(url, headers=headers, timeout=5)
    html = etree.HTML(r.text)
    link_list = ['https://segmentfault.com'+i for i in html.xpath("//div[@class='summary']/h2/a/@href")]
    info_list = html.xpath("//div[@class='summary']/h2/a/text()")
    return choice(list(zip(link_list, info_list)))


if __name__ == '__main__':
    print(fetch_question('https://segmentfault.com/questions/hottest'))
