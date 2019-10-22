# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    rating_score = scrapy.Field()
    rating_badge = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
