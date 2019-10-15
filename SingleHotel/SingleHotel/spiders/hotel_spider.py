import scrapy
from SingleHotel.items import ReviewItem
import time

class hotel_spider(scrapy.Spider):
    name = "hotel_comments"
    start_urls = [
        "https://zh.hotels.com/ho105344-tr-p2/?q-check-in=2019-10-18&q-check-out=2019-10-19&q-rooms=1&q-room-0-adults=2&SYE=3&ZSX=0&MGT=1&YGF=3&WOD=5&WOE=6&applyEmbargo=false&reviewTab=brand-reviews",
    ]

    def parse(self, response):
        reviews = response.css(".review-card")
        # reviews[0].css(".review-score::text").extract_first()
        for review in reviews:
            reviewItem = ReviewItem()
            reviewItem["rating_score"] = review.css(".rating-score::text").extract_first()
            reviewItem["rating_badge"] = review.css(".rating-badge::text").extract_first()
            reviewItem['description'] = review.css(".description::text").extract_first()
            reviewItem["date"] = review.css(".date::text").extract_first()
            yield reviewItem
            
        next = response.css(".pagination-controls a::attr(href)").extract_first()
        nextURL = "https://zh.hotels.com" + next
        yield scrapy.Request(url = nextURL, callback = self.parse)