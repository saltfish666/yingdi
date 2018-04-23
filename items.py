# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingdiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author=scrapy.Field()
    description=scrapy.Field()
    id=scrapy.Field()
    pageview=scrapy.Field()
    reply=scrapy.Field()
    seed=scrapy.Field()
    seedTime=scrapy.Field()
    sourceID=scrapy.Field()
    title=scrapy.Field()


