# coding=utf-8
'''
@Title: Crawl for google apps

@Author: tyee.noprom@qq.com
@Time: 25/10/2016 2:24 PM
'''

import scrapy
from app.items import GoogleItem


class GPSpider(scrapy.Spider):
    '''
    Google app
    '''
    name = 'gp'
    datapath = '/Users/noprom/Documents/Dev/Python/Pro/scrapy-spiders/data/'

    def start_requests(self):
        '''
        爬虫入口
        :return:
        '''
        file = open(self.datapath + 'pkgname.txt')
        langs = ['en', 'af', 'ms', 'ca', 'cs', 'da', 'de', 'et', 'en_GB', 'en', 'es', 'es_419', 'fil', 'fr_CA',
                 'fr', 'hr', 'in', 'zu', 'it', 'sw', 'lv', 'lt', 'hu', 'nl', 'no', 'pl', 'pt_BR', 'pt_PT', 'ro',
                 'sk', 'sl', 'fi', 'sv', 'vi', 'tr', 'el', 'be', 'bg', 'ru', 'sr', 'uk', 'ar', 'am', 'hi', 'th', 'ko',
                 'zh_HK', 'ja', 'zh_CN', 'zh_TW']
        for lang in langs:
            detail_url = 'https://play.google.com/store/apps/details?hl=%s&id=' % lang
            while True:
                lines = file.readlines(100000)
                if not lines:
                    break
                for pkg in lines:
                    pkg = pkg.replace("\r", "").replace("\n", "").replace("\t", "").replace("'", "")
                    print 'pkg: %s' % pkg
                    url = detail_url + pkg
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        提取字段
        :param response:
        :return:
        '''
        item = GoogleItem()
        lang_start = response.url.index('hl=') + 3
        lang_end = response.url.index('&id=')
        item['lang'] = response.url[lang_start: lang_end]
        item['url'] = response.url
        item['title'] = response.xpath("//div[@class='id-app-title']").xpath("text()").extract()
        item['title'] = ''.join(item['title']).replace('\n', '').replace('\r', '').replace('\t', '')
        item['producer'] = response.xpath("//a[@class='document-subtitle primary']/span/text()").extract()
        item['producer'] = ''.join(item['producer']).replace('\n', '').replace('\r', '').replace('\t', '')
        item['price'] = response.xpath("//meta[@itemprop='price']/@content").extract()[0]
        item['rating'] = response.xpath("//span[@class='rating-count']/text()").extract()
        item['num'] = response.xpath("//div[@itemprop='numDownloads']").xpath("text()").extract()[0]
        item['cate'] = response.xpath("//span[@itemprop='genre']").xpath("text()").extract()
        item['cate'] = ''.join(item['cate']).replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
        item['rate'] = response.xpath("//div[@itemprop='contentRating']").xpath("text()").extract()
        item['rate'] = ''.join(item['rate']).replace('\n', '').replace('\r', '').replace('\t', '')
        item['desc'] = response.xpath("//div[@class='description']").xpath("text()").extract()
        item['desc'] = ''.join(item['desc']).replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
        item['desc'] = ''
        item['score'] = response.xpath("//div[@class='score']").xpath("text()").extract()[0]
        item['meta'] = response.xpath("//meta[@name='description']").xpath("@content").extract()
        item['meta'] = ''
        item['meta'] = ''.join(item['meta']).replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
        item['pkg'] = response.xpath("/html").re(u'data-docid="(.*?)"')[0]
        item['icon'] = response.xpath("//div[@class='cover-container']/img/@src").extract()[0].replace("//", "")

        item['info'] = dict()
        title = response.css('.details-section.metadata').css(".title::text").extract()
        content = response.css('.details-section.metadata').css(".content::text").extract()

        for i, t in enumerate(title):
            key = ''.join(t.strip()).replace('\t', '').replace('\r', '').replace('\n', '').replace(' ', '')
            value = ''.join(content[i].strip()).replace('\t', '').replace('\r', '').replace('\n', '')
            item['info'][key] = value

        yield item