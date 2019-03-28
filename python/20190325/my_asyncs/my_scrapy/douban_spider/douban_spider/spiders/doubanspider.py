# -*- coding: utf-8 -*-
import scrapy
import re
from douban_spider.items import DoubanSpiderItem
from scrapy import Request


class DoubanspiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        print('====scrapy fetch start====')
        """通过xpath解析所需字段"""
        movies = response.xpath('//div[@class="article"]//li')
        for movie in movies:
            item = DoubanSpiderItem()
            item['movie_name'] = ''.join([y.replace(' ', '') for y in [
                x.replace('\xa0', '') for x in movie.xpath('.//div[@class="item"]//a//span//text()').extract()]])
            item['movie_desc'] = ''.join(
                movie.xpath('.//div[@class="item"]//div[@class="bd"]//p[1]//text()').extract_first().split())
            item['movie_grade'] = movie.xpath(
                './/div[@class="item"]//div[@class="star"]//span[@class="rating_num"]//text()').extract_first()

            item['comment_num'] = re.findall(
                r'\d+', movie.xpath('.//div[@class="item"]//div[@class="star"]//span[4]//text()').extract_first())[0]

            item['movie_tip'] = ''.join(
                movie.xpath('.//div[@class="item"]//div[@class="bd"]//p[2]//text()').extract()).strip()
            yield item

        # 爬取下一页
        next_page = response.xpath('//span[@class="next"]//link/@href').extract_first()
        if next_page:
            next_url = DoubanspiderSpider.start_urls[0] + next_page
            print('====scrapy fetch next page: %s====' % next_url)
            yield Request(next_url, callback=self.parse)
