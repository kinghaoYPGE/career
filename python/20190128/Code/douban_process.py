"""
多进程豆瓣爬虫实现
"""
from multiprocessing import Process, Queue
import time
from lxml import etree
import requests

# 多进程爬虫
class DoubanSpider(Process):
    def __init__(self, url, q):
        super().__init__()
        self.url = url
        self.q = q

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
            self.q.put('%s %s' % (score, title))



def main():
    # 创建一个队列用于存储子进程获取到的数据
    q = Queue()
    base_url = r'https://movie.douban.com/top250?start=%s&filter=' 
    # url 列表 0->25->50...->225
    url_list = [base_url % i for i in range(0, 225+1, 25)]
    # 进行循环爬取
    process_list = []
    for url in url_list:
        # 创建一个爬虫进程
        p_doubanSpider = DoubanSpider(url, q)
        p_doubanSpider.start()
        process_list.append(p_doubanSpider)
    
    for p in process_list:
        p.join()  # 执行同步
    
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    start = time.time()
    main()
    print('run time: %s' % (time.time()-start))
