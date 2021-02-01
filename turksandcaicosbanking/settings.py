BOT_NAME = 'turksandcaicosbanking'
SPIDER_MODULES = ['turksandcaicosbanking.spiders']
NEWSPIDER_MODULE = 'turksandcaicosbanking.spiders'
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'turksandcaicosbanking.pipelines.DatabasePipeline': 300,
}
