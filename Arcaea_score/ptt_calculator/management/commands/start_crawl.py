
from django.core.management.base import BaseCommand
import logging

from ptt_calculator.tasks import crawl_website

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = '啟動爬蟲任務'

    def handle(self, *args, **kwargs):
        # 排定爬蟲任務
        crawl_website()
        logger.info('done')