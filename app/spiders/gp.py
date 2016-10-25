# coding=utf-8
'''
@Title: Crawl for gp apps

@Author: tyee.noprom@qq.com
@Time: 25/10/2016 2:24 PM
'''

import scrapy


class GPSpider(scrapy.Spider):
    name = "gp"

    def start_requests(self):
        urls = [
            'http://app.mi.com/category/5',
            'http://app.mi.com/category/15',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print '----------> %s' % page
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
