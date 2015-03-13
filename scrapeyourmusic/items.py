from scrapy.item import Item, Field


class Album(Item):

    url = Field()
    name = Field()
    artist = Field()
    type = Field()
    releaseDate = Field()
    releaseYear = Field()
    recordedDate = Field()
    rating = Field()
    totalRatings = Field()
    ranks = Field()
    rankDates = Field()
    primaryGenres = Field()
    secondaryGenres = Field()
    language = Field()

class Artist(Item):

    url = Field()
    name = Field()
    formed = Field()
    members = Field()
    genres = Field()
    studioAlbums = Field()
    liveAlbums = Field()
    EPs = Field()
    singles = Field()
