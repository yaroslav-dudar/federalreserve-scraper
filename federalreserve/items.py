# -*- coding: utf-8 -*-
import scrapy

from .serializers import base_serialzier


class ExchangeRateItem(scrapy.Item):
    country_name = scrapy.Field()
    monetary_unit = scrapy.Field()
    rate = scrapy.Field(serializer=base_serialzier)
    date = scrapy.Field(serializer=base_serialzier)
