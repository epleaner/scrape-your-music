# scrapeyourmusic
A python-based web scraper for www.rateyourmusic.com, powered by scrapy.

### How to use
Navigate to the outer scrapeyourmusic directory, and
`scrapy crawl album_scraper`
Scraped data will appear in out/ by default, in json format
To override output file or export format,
`scrapy crawl album_scraper -o myOutput myFormat`,
where availble feed formats can be found here:
http://doc.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-format