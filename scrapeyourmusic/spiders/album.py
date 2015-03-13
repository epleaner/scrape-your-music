from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapeyourmusic.items import Album


class AlbumSpider(Spider):
    name = "album_scraper"
    allowed_domains = ["rateyourmusic.com"]
    start_urls = [
        "http://rateyourmusic.com/release/album/radiohead/in_rainbows/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://rateyourmusic.com/release/album/radiohead/in_rainbows/
        @scrapes name
        """

        # The most equivalent thing in xpath to css selector to class. Found here:
        # http://stackoverflow.com/questions/8808921/selecting-a-css-class-with-xpath
        sel = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " section_main_info ")]')

        album_info = sel.xpath('.//table[@class="album_info"]')

        item = Album()

        item['url'] = response.url
        item['name'] = sel.xpath('.//div[@class="album_title"]/text()').extract()
        item['artist'] = album_info.xpath('.//a[@class="artist"]/text()').extract()
        item['type'] = album_info.xpath('.//tr')[1].xpath('.//td/text()').extract()
        item['releaseDate'] = album_info.xpath('.//tr')[2].xpath('.//td/text()').extract()
        item['releaseYear'] = album_info.xpath('.//tr')[2].xpath('.//td/a/b/text()').extract()
        item['recordedDate'] = album_info.xpath('.//tr')[3].xpath('.//td/text()').extract()
        item['rating'] = album_info.xpath('.//tr')[4].xpath('.//td/span/span[@class="avg_rating"]/text()').extract()
        item['totalRatings'] = album_info.xpath('.//tr')[4].xpath('.//td/span/span[@class="num_ratings"]/b/span/text()').extract()

        rankings = album_info.xpath('.//tr')[5].xpath('.//td')
        item['ranks'] =  rankings.xpath('.//b/text()').extract()
        item['rankDates'] = rankings.xpath('.//a/text()').extract()

        item['primaryGenres'] = album_info.xpath('.//tr[@class="release_genres"]/td/div/span[@class="release_pri_genres"]/a/text()').extract()
        item['secondaryGenres'] = album_info.xpath('.//tr[@class="release_genres"]/td/div/span[@class="release_sec_genres"]/a/text()').extract()
        item['language'] = album_info.xpath('.//tr')[7].xpath('.//td/text()').extract()

        return item