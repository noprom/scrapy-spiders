# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
import codecs
import logging
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from hashlib import md5


class AppPipeline(object):
    def process_item(self, item, spider):
        return item


class GoogleplayPipeline(object):
    def __init__(self):
        self.file = ''

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        if spider.name == 'googleplay' or spider.name == 'gp':
            line = line.replace("\r", "").replace("\n", "").replace("\t", "").replace("'", "") + "\n"
        else:
            line = line.replace("\\n", "") + "\n"

        # save to file
        if not self.file:
            self.file = codecs.open(spider.name + '-apps.json', 'w', encoding='utf-8')

        self.file.write(line.decode('unicode_escape'))
        return item


class GooglePlayMysqlStoragePipeline(object):
    '''
    Save crawer apps to mysql
    '''

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        url_md5 = self._get_linkmd5id(item)
        print url_md5
        now = "%d" % (time.time() * 1000)
        conn.execute("""
                select 1 from apps where url_md5 = %s
        """, (url_md5,))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update apps set url = %s, pkg = %s, lang = %s, icon = %s, data = %s, update_time = %d where url_md5 = %s
            """, (item['url'], item['pkg'], item['lang'], item['icon'], item['data'], now, url_md5))
            print """
               update apps set url = %s, pkg = %s, lang = %s, icon = %s, data = %s, update_time = %d where url_md5 = %s
            """, (item['url'], item['pkg'], item['lang'], item['icon'], item['data'], now, url_md5)

        else:
            conn.execute("""
                insert into apps(url_md5, url, pkg, lang, icon, data, create_time, update_time)
                values(%s, %s, %s, %s, %s, %s, %d, %d)
            """, (url_md5, item['url'], item['pkg'], item['lang'], item['icon'], item['data'], now, now))
            print """
               insert into apps(url_md5, url, pkg, lang, icon, data, create_time, update_time)
                values(%s, %s, %s, %s, %s, %s, %d, %d)
            """, (url_md5, item['url'], item['pkg'], item['lang'], item['icon'], item['data'], now, now)

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['url']).hexdigest()

    # 异常处理
    def _handle_error(self, failue, item, spider):
        logging.error(failue)