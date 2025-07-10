from pathlib import Path

from datetime import datetime as dt

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = 'results'
TIMESTAMP = dt.now().strftime('%Y-%m-%d_%H-%M-%S')

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
