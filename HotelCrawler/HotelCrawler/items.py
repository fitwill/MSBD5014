# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Store the hotel id and hotel name for further crawler work

class HotelItem(scrapy.Item):
    # define the fields for your item here like:
    hotelId = scrapy.Field()
    hotelName = scrapy.Field()  
