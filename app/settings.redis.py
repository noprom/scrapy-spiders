# -*- coding: utf-8 -*-

# Scrapy settings for app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'app'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'

# REDIS_HOST = '127.0.0.1'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 保存到文件配置
ITEM_PIPELINES = {
    'app.pipelines.GoogleplayPipeline': 100
}

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'q=0.8,en-US;q=0.6,en;q=0.4',
    'Cookie': 'SID=owMEkLViDONu0-ys6Nxuzt02N2M_SSu6EpVFUbxq5YWa_UJ4jpD08AH8I4S7uCl4uGZlFQ.; HSID=ADnoGFoSjynt_ZLtx; SSID=AdukEDUibdiOcbkpe; APISID=0tWOu1GdUYh2C6rN/A802W_b2M2sBRVijv; SAPISID=wTMGWJV24QGknrtF/AeY8qRyIqFTwPUN1j; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=tyeenoprom@gmail.com; NID=89=O2irfVss_7juI-pr3ilpZLDLTompI2UwdtaAq86x5RZ27WawlsmrCjjtK7nnuNzPECBhHcGK2ra2EbetR8pIHEn5WrVMjQtxR-PT9RLQMHib44Binz7b5OU9C78SVfDjgEJGAneCFEk97XSKgozfL8cjLXq1JBute7k2Ed_Uyt81H7xruCTMjoMcG2KfJKNfVQQp-UzX8oNxWxIGMk9F9_1U2PJZmwf5e3weCq9Afr5bNhZVjoYJjnGUo2-m; PLAY_PREFS=CroGCISgtsbsCBKwBgoCU0cQuNXyz_8qGvEFERITFBUWGNQB1QGrAsQE4wXlBegF1wbYBt4G3waQlYEGkZWBBpKVgQaVlYEGl5WBBqSVgQa3lYEGuJWBBryVgQa9lYEGwJWBBsGVgQbElYEGxZWBBsiVgQbOlYEGz5WBBtCVgQbUlYEG2ZWBBt2VgQbylYEG-JWBBvmVgQaGloEGiZaBBoyWgQaPloEGkpaBBpuWgQaeloEGn5aBBqCWgQahloEGqJaBBqqWgQarloEGypeBBu6XgQbvl4EGhZiBBr6YgQatm4EGy5uBBsCcgQa8nYEG3Z2BBt6dgQbnnYEGkJ6BBpaegQakoIEG4qKBBvOigQb8ooEGi6OBBpqkgQaepIEGsqSBBq-lgQbqpYEGxqaBBtSmgQbVpoEG1qaBBv6mgQaAp4EGgqeBBoSngQaGp4EGiKeBBoqngQajqIEGxKiBBvKogQb0qIEGo6mBBrysgQbLrYEG2q6BBtuugQbcroEG1q-BBsGwgQaksYEGpbGBBoeygQaJsoEGq7KBBtaygQaxtIEGv7mBBta5gQbruoEGjsCBBqLAgQbAwIEG7cCBBvLAgQaEwYEGwcGBBrPCgQbWwoEGjMWBBo_FgQbKxoEGy8aBBrHHgQb4x4EGrcmBBrDJgQaeyoEGqsqBBuHKgQbryoEG3MyBBuTMgQbdzYEGhs6BBqHPgQbFz4EGxNKBBqrXgQai2IEGk9mBBsvZgQbM2YEG1NuBBufegQbZ4IEGguSBBtvkgQaL5YEGjOWBBpflgQaw7IEG8-2BBv3tgQbv7oEGyO-BBuvvgQbA8IEGivGBBtn1gQby9oEGuvuBBr__gQbE_4EGyf-BBrCEggbIhIIGyYSCBvuEgga1hoIGpoeCBqeHgga3h4IGuIeCBtuHggbsh4IG7YeCBr6NggbrjYIGlJGCBsuRggbOkYIG1pGCBsyXggbvl4IGw5iCBs-ZggbvmYIG_JmCBpmaggbLmoIGmZuCBtSdggaUnoIGxJ6CBuSeggaa8OI7KMXpls7_KjokNWU5ZDUxOTUtNjRjYy00NzUxLTg0MjktMGY0MGRjZTRmZmE2QAFIAA:S:ANO1ljK_gVx6vQzbYA; _gat=1; S=billing-ui-v3=NQ4YOLxTtetyuJokdxreRZ8MzGTEURcN:billing-ui-v3-efe=NQ4YOLxTtetyuJokdxreRZ8MzGTEURcN; _ga=GA1.3.1789025720.1473084929'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'app.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'app.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'app.pipelines.SomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
