# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request

from ..items import ExchangeRateItem


class ExchageRatesSpider(CrawlSpider):
    name = 'exchange_rates'
    site_url = 'https://www.federalreserve.gov/releases/h10/hist/'
    start_urls = [site_url]

    def parse(self, response):
        countries = response.xpath('//table[@class="statistics"]/tr')
        for country in countries:
            country_name = country.css('th a[href]::text').extract()[0]
            monetary_unit = country.css('td::text').extract()[0]

            exchange_rates_link = country.\
                css('th a::attr(href)').extract()[0]

            yield Request(
                '%s%s' % (self.site_url, exchange_rates_link),
                dont_filter=True,
                meta={
                    'country_name': country_name,
                    'monetary_unit': monetary_unit
                },
                callback=self.parse_rates
            )

    def parse_rates(self, response):
        country_name = response.meta.get('country_name')
        monetary_unit = response.meta.get('monetary_unit')

        exchange_rates = response.xpath('//table[@class="statistics"]/tr')
        for rate in exchange_rates:
            item = ExchangeRateItem()
            item['country_name'] = country_name
            item['monetary_unit'] = monetary_unit

            item['date'] = rate.css('th#r1::text').extract()
            item['rate'] = rate.css('td[headers="a2 a1 r1"]::text').extract()

            yield item
