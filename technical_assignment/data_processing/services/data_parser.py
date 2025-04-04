import logging
import json
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


class XMLParser:
    def parse(self, file_path):
        """
        Parse XML data from the given file path.
        """
        logger.info(f"Parsing XML file: {file_path}")
        data_subitem_list = []
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            for item in root.findall('item'):
                data_item = {
                    'id': item.find('string6').text if item.find('string6') is not None else '',
                    'dataString0': item.find('string0').text if item.find('string0') is not None else '',
                    'dataString1': item.find('string1').text if item.find('string1') is not None else '',
                    'dataString2': item.find('string2').text if item.find('string2') is not None else '',
                    'dataString3': item.find('string3').text if item.find('string3') is not None else '',
                    'dataString4': item.find('string4').text if item.find('string4') is not None else '',
                    'dataString5': item.find('string5').text if item.find('string5') is not None else '',
                }

                data_subitem_list.append(data_item)

            logger.info(f"Parsed {len(data_subitem_list)} items from XML file")
        except ET.ParseError as e:
            logger.error(f"Error parsing XML file {file_path}: {e}")

        return data_subitem_list


class JSONParser:
    def parse(self, file_path):
        """
        Parse JSON data from the given file path.
        Handles both list and dictionary formats.
        """
        logger.info(f"Parsing JSON file: {file_path}")
        data_subitem_list = []
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Handle both list and dictionary formats
            items = data if isinstance(data, list) else data.get('syncItems', [])

            for item in items:
                current_data = item.get('currentData', item)
                data_item = {
                    'id': current_data.get('id', ''),
                    'dataString0': current_data.get('dataString0', ''),
                    'dataString1': current_data.get('dataString1', ''),
                    'dataString2': current_data.get('dataString2', ''),
                    'dataString3': current_data.get('dataString3', ''),
                    'dataString4': current_data.get('dataString4', ''),
                    'dataString5': current_data.get('dataString5', ''),
                }
                data_subitem_list.append(data_item)

            logger.info(f"Parsed {len(data_subitem_list)} items from JSON file")
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON file {file_path}: {e}")

        return data_subitem_list