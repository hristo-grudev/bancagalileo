BOT_NAME = 'bancagalileo'

SPIDER_MODULES = ['bancagalileo.spiders']
NEWSPIDER_MODULE = 'bancagalileo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancagalileo.pipelines.BancagalileoPipeline': 100,

}