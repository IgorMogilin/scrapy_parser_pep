import scrapy


class PepParseItem(scrapy.Item):
    """Класс для хранения информации о PEP."""
    name = scrapy.Field()
    number = scrapy.Field()
    status = scrapy.Field()
