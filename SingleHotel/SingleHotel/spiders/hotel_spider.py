import scrapy
from SingleHotel.items import ReviewItem
import time

class hotel_spider(scrapy.Spider):
    name = "hotel_comments"
    start_urls = [
        "https://www.hotels.com/ho105344-tr/",
        
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
            
        next = response.css("a.cta-next").attrib['href']
        nextURL = "https://www.hotels.com" + next
        yield scrapy.Request(url = nextURL, callback = self.parse)