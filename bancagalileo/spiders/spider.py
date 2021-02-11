import scrapy

from scrapy.loader import ItemLoader
from ..items import BancagalileoItem
from itemloaders.processors import TakeFirst


class BancagalileoSpider(scrapy.Spider):
	name = 'bancagalileo'
	start_urls = ['https://www.bancagalileo.it/it-it/news-1.aspx']

	def parse(self, response):
		post_links = response.xpath('//div[@class="media"]')
		for post in post_links:
			yield self.parse_post(response, post)

		next_page = response.xpath('//a[text()="»"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response, post):
		title = post.xpath('.//h4/text()').get()
		description = post.xpath('.//text()[normalize-space() and not(ancestor::h4 | ancestor::b[@class="media-body-date"] | ancestor::script)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = post.xpath('.//b[@class="media-body-date"]/text()').get()

		item = ItemLoader(item=BancagalileoItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
