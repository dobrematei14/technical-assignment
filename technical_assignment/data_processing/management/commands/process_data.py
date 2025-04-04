import logging

from django.core.management.base import BaseCommand

from technical_assignment.data_processing.services.data_parser import XMLParser, JSONParser
from technical_assignment.data_processing.services.data_processor import DataProcessor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Process XML and JSON data files, validate and grade them, then store in database'

    def add_arguments(self, parser):
        parser.add_argument('--xml', type=str, help='Path to XML file')
        parser.add_argument('--json', type=str, help='Path to JSON file')

    def handle(self, *args, **options):
        data_processor = DataProcessor()

        if options['xml']:
            xml_parser = XMLParser()
            xml_data = xml_parser.parse(options['xml'])
            for data_item in xml_data:
                data_processor.process_item(data_item)

        if options['json']:
            json_parser = JSONParser()
            json_data = json_parser.parse(options['json'])
            for data_item in json_data:
                data_processor.process_item(data_item)

        self.stdout.write(self.style.SUCCESS('Data processing completed'))