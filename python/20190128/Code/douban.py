"""
单任务爬虫：爬取豆瓣电影top250, 打印电影名和评分
"""
import requests
from lxml import etree
import time

class DoubanSpider(object):
    def __init__(self, url):
        self.url = url
    # 发送请求
    def send_request(self):
        i = 0
        # 如果请求有问题, 重复请求3次
        while i <= 3:
            try:
                print(5*'=','url: %s' % self.url, 5*'=') 
                return requests.get(self.url).content.decode()
                
            except Exception as e:
                print(e)
                print('exception url is %s' % self.url)
                i += 1
    def run(self):
        self.parse_html()

    def parse_html(self):
        response = self.send_request()
        # xpath解析网页数据
        html = etree.HTML(response)
        node_list = html.xpath(r"//div[@class='info']")
        for movie in node_list:
            # 电影名称
            title = movie.xpath(r'.//a/span/text()')[0]
            # 电影评分
            score = movie.xpath(r".//div[@class='star']//span[@class='rating_num']/text()")[0]
            print('%s %s' %(score, title))


def main():
    base_url = r'https://movie.douban.com/top250?start=%s&filter=' 
    # url 列表 0->25->50...->225
    url_list = [base_url % i for i in range(0, 225+1, 25)]
    # 进行循环爬取
    for url in url_list:
        doubanSpider = DoubanSpider(url)
        doubanSpider.run()
        

if __name__ == '__main__':
    start = time.time()
    main()
    print('run time: %s' % (time.time()-start))