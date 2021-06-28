import scrapy
from amazon.items import AmazonItem

class AmazonproductspiderSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.in"]
  
    #Use working product URL below
    start_urls = [
        "https://www.amazon.in/s?k=145%2F80%2Fr12+tyre&ref=nb_sb_noss_1"
        ]
 
    def parse(self, response):
        items = AmazonItem()
        title = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        sale_price = response.xpath('//span[@class="a-price-whole"]/text()').extract()
        # category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        # availability = response.xpath('//div[@id="availability"]//text()').extract()
        # product_mrp = response.xpath('//span[@class="priceBlockStrikePriceString a-text-strike"]/text()').extract()
        print('priya-------------------------------------------------------------')
        print(title)
        print(sale_price)
        items['product_name'] = ','.join(title).strip()
        items['product_sale_price'] = ','.join(sale_price).strip()
        # items['product_mrp'] = ''.join(product_mrp).strip()
        # items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
        # items['product_availability'] = ''.join(availability).strip()
        yield items
