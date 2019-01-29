"""
多线程豆瓣爬虫
"""
from threading import Thread, local
import time
from lxml import etree
import requests

movie_local = local()
movie_list = []
# 多线程爬虫
class DoubanSpider(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    # 当前进程的任务
    def run(self):
        self.parse_html()
    
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
            movie_local.movie_info = '%s %s' % (score, title)
            movie_list.append(movie_local.movie_info)



def main():
    base_url = r'https://movie.douban.com/top250?start=%s&filter=' 
    # url 列表 0->25->50...->225
    url_list = [base_url % i for i in range(0, 225+1, 25)]
    # 进行循环爬取
    thread_list = []
    for url in url_list:
        # 创建一个爬虫进程
        t_doubanSpider = DoubanSpider(url)
        t_doubanSpider.start()
        thread_list.append(t_doubanSpider)
    
    for t in thread_list:
        t.join()  # 执行同步
    
    print('\n'.join(movie_list))


if __name__ == '__main__':
    start = time.time()
    main()
    print('run time: %s' % (time.time()-start))
