"""
需求: 创建一个爬虫类，爬取直播网站中每个分类的主播信息并按照人气排序打印。
"""
from urllib.request import urlopen
import re

class Spider(object):
    cls_url = r'https://www.panda.tv/cate/lol'
    cls_root_pattern = r'<div class="video-info">(.*?)</div>'
    cls_info_pattern = r'</i>([\s\S]*?)</span>'

    def __init__(self, url=cls_url, root_pattern=cls_root_pattern, info_pattern=cls_info_pattern):
        self.url = url
        self.root_pattern = root_pattern
        self.info_pattern = info_pattern

    def fetch_content(self):
        resp = urlopen(self.url)
        htmls = resp.read().decode('utf-8')
        return htmls

    def analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls, flags=re.S)
        arthurs = []
        for html in root_html:
            # 提取主播名字
            info = re.findall(self.info_pattern, html)
            # name = re.sub('[\s]+', '', info[0])
            name = info[0].strip()
            score = info[1]
            infos = {'name':name, 'score': score}
            arthurs.append(infos)
        # print(root_html)
        return arthurs

    def score_sort(self, arthur):
        score = arthur['score']
        r = re.findall(r'\d*', score)
        number = float(r[0])
        if '\u4e07' in score:
            number *= 10000
        return number

    def show(self, arthurs):
        for arthur in arthurs:
            name = arthur['name']
            score = arthur['score']
            print('name: %s ---- hot: %s' % (name, score))


    def run(self):
        # 获取网页
        htmls = self.fetch_content()
        # print(htmls.decode('utf-8'))
        # 分析提取网站内容
        arthurs = self.analysis(htmls)
        arthurs = sorted(arthurs, key=self.score_sort, reverse=True)
        self.show(arthurs)


def main():
    spider = Spider()
    spider.run()

if __name__ == '__main__':
    main()
