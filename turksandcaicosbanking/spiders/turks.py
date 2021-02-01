import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from turksandcaicosbanking.items import Article


class TurksSpider(scrapy.Spider):
    name = 'turks'
    allowed_domains = ['turksandcaicos-banking.com']
    start_urls = ['https://www.turksandcaicos-banking.com/news/']

    def parse(self, response):
        links = response.xpath('//h2/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()
        title = response.xpath('//h1[@class="entry-title"]/text()').get()
        metadata = response.xpath('//p[@class="p-meta"]/span//text()').getall()
        date = response.xpath('//time/@datetime')
        date_time_obj = datetime.strptime(metadata[1], ' %B %d, %Y')
        article_date = date_time_obj.strftime("%Y/%m/%d")
        content = response.xpath('//div[@class="entry-content content"]//text()').getall()
        content = " ".join(content)

        item.add_value('title', title)
        item.add_value('date', article_date)
        item.add_value('author', metadata[0])
        item.add_value('category', metadata[2])
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
