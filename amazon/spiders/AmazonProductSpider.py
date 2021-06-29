import scrapy
from amazon.items import AmazonItem
import datetime

class AmazonproductspiderSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.in"]
  
    #Use working product URL below
    start_urls = [
        "https://www.amazon.in/s?k=145%2F80%2F12+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=165%2F80%2F14+tyre&ref=nb_sb_noss"
        # "https://www.amazon.in/s?k=155%2F70%2F13+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=175%2F65%2F14+tyre&i=automotive&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=155%2F80%2F13+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=185%2F65%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=215%2F75%2F15+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=155%2F65%2F13+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=205%2F65%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=185%2F70%2F14+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=145%2F80%2F13+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=145%2F70%2F12+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=145%2F70%2F13+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=165%2F70%2F14+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=165%2F65%2F14+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=165%2F65%2F13+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=185%2F65%2F14+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=185%2F60%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=195%2F55%2F16+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=175%2F70%2F13+tyre&ref=nb_sb_noss_2"
        # "https://www.amazon.in/s?k=155%2F65%2F14+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=175%2F70%2F14+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=235%2F70%2F16+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=205%2F65%2F16+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=175%2F65%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=205%2F60%2F16+tyre&ref=nb_sb_noss"
        # "https://www.amazon.in/s?k=235%2F65%2F17+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=215%2F60%2F16+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=195%2F65%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=195%2F60%2F15+tyre&ref=nb_sb_noss_1"
        # "https://www.amazon.in/s?k=215%2F65%2F16+tyre&ref=nb_sb_noss_1"
        ]
 
    def parse(self, response):
        items = AmazonItem()
        sections =response.xpath('//div[@class="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16"]')
        #sg-col-inner s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16
        
        tyre_size = response.xpath('//span[@class="a-color-state a-text-bold"]/text()').get()
        for section in sections:
            # print('---------------------------------------------')
            # print(section)
            product_name = section.xpath('.//div[@class="a-section a-spacing-none"]/h2/a/span/text()').get()
            sale_price = section.xpath('.//span[@class="a-price-whole"]/text()').get()
            product_mrp = section.xpath('.//span[@data-a-color="secondary"]/span/text()').get()
            product_rating = section.xpath('.//span[@class="a-icon-alt"]/text()').get()
            total_ratings = section.xpath('.//span[@class="a-size-base"]/text()').get()
            
            # product_name = section.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').get()
            print('---------------PN------------------------------')
            print(product_name)
            yield AmazonItem(product_name=product_name,sale_price=sale_price,product_mrp = product_mrp.strip("₹"),product_rating=product_rating,total_ratings=total_ratings,tyre_size=tyre_size.strip('"'))#,product_rating=product_rating,product_mrp=product_mrp,total_ratings=total_ratings
        
        next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
        print(next_page)
        next_page = response.urljoin(next_page)
        print(next_page)
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
        