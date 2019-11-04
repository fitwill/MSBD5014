# -*- coding: utf-8 -*-
import scrapy
from HotelCrawler.items import HotelItem
import json

class HotelSpider(scrapy.Spider):
    name = 'Hotel'
    url = 'https://hotels.com/search/listings.json?destination-id=606379&q-destination=%E9%A6%99%E6%B8%AF,%20%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%A5%E8%A1%8C%E6%94%BF%E5%8D%80&pn='
    start_urls = [url + str(1)]

    def parse(self, response):
        data = json.loads(response.body).get('data', {})
        for item in data.get('body', {}).get('searchResults', {}).get('results', {}):
            yield {
                'hotelId': item.get('id'),
                'hotelName': item.get('name')
            }
        # if data.get('body', {}).get('searchResults', {}).get('pagination', {}).get('nextPageUrl'):
        currentPage = data.get('body', {}).get('searchResults', {}).get('pagination', {}).get('currentPage')
        nextPageNum = currentPage + 1
        nextUrl = self.url + str(nextPageNum)
        print(nextUrl)
        yield scrapy.Request(url = nextUrl, callback = self.parse)


# import scrapy
# from SingleHotel.items import ReviewItem
# import time

# class hotel_spider(scrapy.Spider):
#     name = "hotel_comments"
#     start_urls = [
#         "https://zh.hotels.com/ho105344-tr/?q-check-in=2019-10-18&q-check-out=2019-10-19&q-rooms=1&q-room-0-adults=2&SYE=3&ZSX=0&MGT=1&YGF=3&WOD=5&WOE=6&applyEmbargo=false&reviewTab=brand-reviews",
#     ]

#     def parse(self, response):
#         reviews = response.css(".review-card")
#         # reviews[0].css(".review-score::text").extract_first()
#         for review in reviews:
#             reviewItem = ReviewItem()
#             reviewItem["rating_score"] = review.css(".rating-score::text").extract_first()
#             reviewItem["rating_badge"] = review.css(".rating-badge::text").extract_first()
#             reviewItem['description'] = review.css(".description::text").extract_first()
#             reviewItem["date"] = review.css(".date::text").extract_first()
#             yield reviewItem

#         next = response.css("a.cta-next").extract()
#         nextURL = "https://zh.hotels.com" + next
#         yield scrapy.Request(url = nextURL, callback = self.parse)
