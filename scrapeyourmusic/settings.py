# Scrapy settings for scrapeyourmusic project

SPIDER_MODULES = ['scrapeyourmusic.spiders']
NEWSPIDER_MODULE = 'scrapeyourmusic.spiders'
DEFAULT_ITEM_CLASS = 'scrapeyourmusic.items.Album'

ITEM_PIPELINES = {'scrapeyourmusic.pipelines.FormatDataPipeline': 1}

FEED_URI = 'out/out.json'
FEED_FORMAT = 'json'