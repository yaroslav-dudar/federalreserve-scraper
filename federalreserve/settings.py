# -*- coding: utf-8 -*-

BOT_NAME = 'federalreserve'

SPIDER_MODULES = ['federalreserve.spiders']
NEWSPIDER_MODULE = 'federalreserve.spiders'

DOWNLOAD_DELAY = 1.5
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5

ITEM_PIPELINES = {
    'federalreserve.pipelines.FederalreservePipeline': 300,
}
