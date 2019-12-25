## README.md



This code is the solution of MSBD5014 Independent Project.  

In this project, I implemented two network crawlers which could obtain the whole hotel list and corresponding comments from customers. 

The first crawler is named as "Hotel", you can run it by executing the following command in terminal.

```bash
/(YourPath)/HotelCrawler: scrapy crawl Hotel -o hotel_list.json   
```

The second crawler is named as "hotel_comments", you can run it by excuting the following command in terminal.

```bash
/(YourPath)/SingleHotel: scrapy crawl hotel_comments -o comments_result.json
```



**Environment**: 

- Python 3.7.4
- Scrapy 1.7.3
- Pandas 0.25.2

**Repository Structure:**

- *HotelCrawler*:  Get the list of the hotels;
  - *HotelCrawler/HotelCrawler/spiders/hotel.py*: Code of Hotel crawler;
  - *HotelCrawler/HotelCrawler/hotel_list.json*: The result of the crawler;
- *SingleHotel*: Get the reviews of each hotel;
  - *SingleHotel/SingleHotel/spiders/hotel_spider.py*: Code of hotel_comments crawler;
  - *SingleHotel/comments_result.json*: The result of the crawler;









<img src="/Users/will/Library/Application Support/typora-user-images/image-20191225153058471.png" alt="image-20191225153058471" style="zoom:60%;" />