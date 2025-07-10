import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    """Паук для сбора информации о PEP."""
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        """Обработка главной страницы со списком PEP."""
        pep_links = [url for url in response.xpath(
            '//table[contains(@class, "pep-zero-table")]//tr/td[2]/a/@href'
        ).getall()]
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Обработка страницы отдельного PEP."""
        pep_number = response.css(
            'h1.page-title::text'
        ).re_first(r'PEP\s+(\d{1,4})')
        pep_name = response.css(
            'h1.page-title::text'
        ).re_first(r'PEP \d+ – (.+)')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': pep_number,
            'name': pep_name,
            'status': status,
        }
        yield PepParseItem(data)
