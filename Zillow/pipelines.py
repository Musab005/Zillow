# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.http.request import NO_CALLBACK
import hashlib
from scrapy.utils.python import to_bytes


class ZillowPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, callback=NO_CALLBACK, meta={'house_id': item.get('id')}) for u in urls]

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.meta['house_id']
        return f"images/{image_name}.jpg"
