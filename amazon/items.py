import scrapy
import datetime 

class AmazonItem(scrapy.Item):
  # define the fields for your item here like:
  product_name = scrapy.Field()
  sale_price = scrapy.Field()
  product_mrp = scrapy.Field()
  product_rating = scrapy.Field()
  total_ratings = scrapy.Field()
  tyre_size = scrapy.Field()
  
  