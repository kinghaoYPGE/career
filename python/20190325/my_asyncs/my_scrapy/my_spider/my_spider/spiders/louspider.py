import scrapy
from my_spider.items import CourseItem
from scrapy.selector import Selector
from scrapy import Request


class LouSpider(scrapy.Spider):
    name = 'louspider'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        """
        解析html并提取到Item
        :param response:
        :return:
        """
        tree = Selector(response)
        courses = tree.xpath('//a[@class="course-box"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract()[0].strip()
            item['image'] = course.xpath('./div[@class="course-img"]/img/@src').extract()[0].strip()
            item['learned'] = (''.join(course.xpath('.//span[@class="course-per-num pull-left"]/text()').extract())).strip()
            yield item

        # 爬取下一页
        next_page = tree.xpath('//ul[@class="pagination"]//a[@aria-label="Next"]/@href').extract_first()
        if next_page:
            next_url = 'https://www.shiyanlou.com/'+next_page
            # print('fetch {0}:'.format(next_url))
            yield Request(next_url, callback=self.parse)
