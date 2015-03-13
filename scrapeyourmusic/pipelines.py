from scrapy.exceptions import DropItem
from scrapeyourmusic.utility import ListToString


class FormatDataPipeline(object):
    # """A pipeline for filtering out items which contain certain words in their
    # description"""
    #
    # # put all words in lowercase
    # words_to_filter = ['politics', 'religion']
    #
    # def process_item(self, item, spider):
    #     for word in self.words_to_filter:
    #         if word in unicode(item['description']).lower():
    #             raise DropItem("Contains forbidden word: %s" % word)
    #     else:
    #         return item
    def process_item(self, item, spider):

        item['name'] = ListToString(item['name'])
        item['artist'] = ListToString(item['artist'])
        item['type'] = ListToString(item['type'])
        item['releaseDate'] = ListToString(item['releaseDate']).replace(',', '')
        item['releaseYear'] = ListToString(item['releaseYear'])
        item['recordedDate'] = ListToString(item['recordedDate'])
        item['rating'] = ListToString(item['rating'])
        item['totalRatings'] = ListToString(item['totalRatings'])
        item['primaryGenres'] = ListToString(item['primaryGenres'], ', ')
        item['secondaryGenres'] = ListToString(item['secondaryGenres'], ', ')
        item['language'] = ListToString(item['language'])
        return item