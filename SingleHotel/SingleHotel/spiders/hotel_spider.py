import scrapy
from SingleHotel.items import ReviewItem
import json
import os
import pandas as pd

class hotel_spider(scrapy.Spider):
    
    with open(os.getcwd() + "/SingleHotel/spiders/hotel_list.json", 'r') as f:
        hotelList = json.loads(f.read())
    currentIndex = 0
    # flag = True
    hotel_df = pd.DataFrame(hotelList, columns=['hotelId'])
    hotel_df = hotel_df.drop_duplicates()
    # print(hotel_df)

    name = "hotel_comments"
    allowed_domains = ["www.hotels.com"]
    start_urls = [
        "http://www.hotels.com/ho940393024-tr/",
    ]

    def parse(self, response):
        # if 'currentIndex' not in response.meta :
        #     currentIndex = 0
        # else:
        #     currentIndex = response.meta['currentIndex']
        

        # row = self.hotel_df.iloc[self.currentIndex, :]
        reviews = response.css(".review-card")
        # name = row['hotelName']

        for review in reviews:
            reviewItem = ReviewItem()
            reviewItem["hotel_name"] = response.css(".vcard a::text").extract_first()
            reviewItem["rating_score"] = review.css(".rating-score::text").extract_first()
            reviewItem["rating_badge"] = review.css(".rating-badge::text").extract_first()
            reviewItem['description'] = review.css(".description::text").extract_first()
            reviewItem["date"] = review.css(".date::text").extract_first()
            yield reviewItem

        if response.css("a.cta-next") != []:
            next = response.css("a.cta-next").attrib['href']
            nextURL = "https://www.hotels.com" + next
            # print("next url alert!!!!!" + nextURL)
            # , meta={"currentIndex": currentIndex + 1}
            yield scrapy.Request(url = nextURL, callback = self.parse)
        else:
            # print("nextindex is !!!!!")
            # print(self.hotel_df.iloc[self.currentIndex, :]['hotelId'])
            self.currentIndex += 1
            if self.currentIndex <= self.hotel_df.shape[0]:
                #print("here is hotel iterator" )
                #print(self.hotel_df.iloc[currentIndex, :]['hotelId'])
                nextHotel = "https://www.hotels.com/ho" + str(self.hotel_df.iloc[self.currentIndex, :]['hotelId']) + "-tr/"
                # , meta={"currentIndex": currentIndex + 1}
                yield scrapy.Request(url=nextHotel, callback=self.parse)
            else:
                return