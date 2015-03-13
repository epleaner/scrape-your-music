from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import Request

from scrapeyourmusic.items import Artist, Album
from scrapeyourmusic.utility import ListToString

class ArtistSpider(Spider):
    name = "artist_scraper"
    allowed_domains = ["rateyourmusic.com"]
    start_urls = [
        "http://rateyourmusic.com/artist/radiohead"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://rateyourmusic.com/artist/radiohead
        @scrapes name
        """

        item = Artist()

        studios = response.xpath('//div[@id="disco_type_s"]/div[@class="disco_release"]')

        for studio in studios:
            url = 'www.rateyourmusic.com' + ListToString(studio.xpath('.//div[@class="disco_info"]/a/@href').extract())
            yield Request(url, callback=self.parse_album)

    def parse_album(self, response):
        item = Album()

        return item
