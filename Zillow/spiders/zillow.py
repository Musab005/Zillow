import scrapy
import json
from scrapy.loader import ItemLoader
from ..items import ZillowItem
from ..Util import URL, new_url


class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["www.zillow.com", 'photos.zillowstatic.com']

    current_page = 1

    query = {
        "searchQueryState": {
            "isMapVisible": False,
            "mapBounds": {
                "north": 40.93943050053751,
                "south": 40.62174864805049,
                "east": -73.70897081542967,
                "west": -74.24867418457029
            },
            "mapZoom": 11,
            "filterState": {
                "sortSelection": {
                    "value": "days"
                },
                "price": {
                    "min": 100000,
                    "max": 300000
                },
                "monthlyPayment": {
                    "min": 503,
                    "max": 1509
                },
                "isAllHomes": {
                    "value": True
                }
            },
            "isListVisible": True,
            "usersSearchTerm": "Manhattan New York NY",
            "regionSelection": [
                {
                    "regionId": 12530,
                    "regionType": 17
                }
            ],
            "pagination": {}
        },
        "wants": {
            "cat1": [
                "listResults"
            ],
            "cat2": [
                "total"
            ]
        },
        "requestId": 19,
        "isDebugRequest": False
    }

    def start_requests(self):
        # This method makes the API request to the
        yield scrapy.Request(
            url=URL,  # url to send the request to
            method='PUT',
            # body = payload. Need to send as string so convert the json object to string  using `dumps`
            body=json.dumps(self.query),
            headers={
                'Content-Type': 'application/json'
            },
            callback=self.parse  # go to this method after execution completes
        )

    # need to change both url and query state
    def parse(self, response):
        # with open('zillow.json', 'wb') as f:
        # 'wb' means write exactly as is without applying special formats like `\n`
        #     f.write(response.body)
        json_response = json.loads(response.body)
        listings = json_response.get('cat1').get('searchResults').get('listResults')
        total_pages = json_response.get('cat1').get('searchList').get('totalPages')
        for listing in listings:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', listing.get('id'))
            loader.add_value('status', listing.get('marketingStatusSimplifiedCd'))
            loader.add_value('image_urls', listing.get('imgSrc'))
            loader.add_value('url', listing.get('detailUrl'))
            loader.add_value('price', listing.get('price'))
            loader.add_value('address', listing.get('address'))
            home_info = listing.get('homeInfo')
            if home_info is not None:
                loader.add_value('unit_no', listing.get('unit'))
            loader.add_value('beds', listing.get('beds'))
            loader.add_value('baths', listing.get('baths'))
            loader.add_value('sqft', listing.get('area'))
            loader.add_value('isZillowOwned', listing.get('isZillowOwned'))
            loader.add_value('broker_name', listing.get('brokerName'))
            yield loader.load_item()

        # check if max no. of pages reached
        # cat1 -> searchList -> totalPages
        if self.current_page < total_pages:
            self.current_page += 1
            yield scrapy.Request(
                url=URL,
                method='PUT',
                # body = payload. Need to update the query to pagination number
                body=json.dumps(new_url(self.query, self.current_page)),
                headers={
                    'Content-Type': 'application/json'
                },
                callback=self.parse
            )
