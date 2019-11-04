import scrapy
from SingleHotel.items import ReviewItem
import json
import os
import pandas as pd

class hotel_spider(scrapy.Spider):
    
    with open(os.getcwd() + "/SingleHotel/spiders/hotel_list.json", 'r') as f:
        hotelList = json.loads(f.read())
    currentIndex = 0
    flag = True
    hotel_df = pd.DataFrame(hotelList, columns=['hotelId', 'hotelName'])
    hotel_df.drop_duplicates()
    print(hotel_df)

    name = "hotel_comments"
    allowed_domains = ["www.hotels.com"]
    start_urls = [
        "http://www.hotels.com/ho940393024-tr/",
    ]

    def parse(self, response):

        while self.flag:
            row = self.hotel_df.iloc[self.currentIndex, :]
            reviews = response.css(".review-card")
            name = row['hotelName']
            print("index_ _ _ _ _ " + str(self.currentIndex) + "_ _ _ _ _ _ _ _alert")

            for review in reviews:
                reviewItem = ReviewItem()
                reviewItem["hotel_name"] = name
                reviewItem["rating_score"] = review.css(".rating-score::text").extract_first()
                reviewItem["rating_badge"] = review.css(".rating-badge::text").extract_first()
                reviewItem['description'] = review.css(".description::text").extract_first()
                reviewItem["date"] = review.css(".date::text").extract_first()
                yield reviewItem

            if response.css("a.cta-next") != []:
                next = response.css("a.cta-next").attrib['href']
                nextURL = "https://www.hotels.com" + next
                print("next url alert!!!!!" + nextURL)
                yield scrapy.Request(url = nextURL, callback = self.parse)
            else:
                self.currentIndex += 1
                print("nextindex is !!!!!")
                print(self.hotel_df.iloc[self.currentIndex, :]['hotelId'])
                if self.currentIndex <= self.hotel_df.head(3).shape[0]:
                    print("here is hotel iterator" )
                    print(self.hotel_df.iloc[self.currentIndex, :]['hotelId'])
                    nextHotel = "https://www.hotels.com/ho" + str(self.hotel_df.iloc[self.currentIndex, :]['hotelId']) + "-tr/"
                    yield scrapy.Request(url = nextHotel, callback = self.parse)
                else:
                    self.flag = False