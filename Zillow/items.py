# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class ZillowItem(scrapy.Item):
    id = scrapy.Field(
        output_processor=TakeFirst()
    )
    status = scrapy.Field(
        output_processor=TakeFirst()
    )
    image_urls = scrapy.Field()
    images = scrapy.Field()
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    address = scrapy.Field(
        output_processor=TakeFirst()
    )
    unit_no = scrapy.Field(
        output_processor=TakeFirst()
    )
    beds = scrapy.Field(
        output_processor=TakeFirst()
    )
    baths = scrapy.Field(
        output_processor=TakeFirst()
    )
    sqft = scrapy.Field(
        output_processor=TakeFirst()
    )
    isZillowOwned = scrapy.Field(
        output_processor=TakeFirst()
    )
    broker_name = scrapy.Field(
        output_processor=TakeFirst()
    )
