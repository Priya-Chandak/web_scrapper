import scrapy
from amazon.items import AmazonItem


class AmazonproductspiderSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.in"]
  
    #Use working product URL below
    start_urls = [
        "https://www.amazon.in/s?k=145%2F80%2F12+tyre&ref=nb_sb_noss_1",
        "https://www.amazon.in/s?k=165%2F80%2F14+tyre&ref=nb_sb_noss",
        "https://www.amazon.in/s?k=155%2F70%2F13+tyre&ref=nb_sb_noss_1"
        ]
 
    def parse(self, response):
        items = AmazonItem()
        product_name = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        sale_price = response.xpath('//span[@class="a-price-whole"]/text()').extract()
        product_mrp = response.xpath('//span[@class="a-price a-text-price"]/span/text()').extract()
        product_rating = response.xpath('//span[@class="a-icon-alt"]/text()').extract()
        total_ratings = response.xpath('//span[@class="a-size-base"]/text()').extract()
        # tyre_size = response.xpath('//span[@class="a-color-state a-text-bold"]/span/text()').extract()
        
        print('---------------------------------------------')
        
        for (product_name,sale_price,product_rating,product_mrp,total_ratings) in zip(product_name,sale_price,product_rating,product_mrp,total_ratings):
            yield AmazonItem(product_name=product_name,sale_price=sale_price,product_rating=product_rating,product_mrp=product_mrp,total_ratings=total_ratings)

        next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
        print(next_page)
        next_page = response.urljoin(next_page)
        print(next_page)
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

