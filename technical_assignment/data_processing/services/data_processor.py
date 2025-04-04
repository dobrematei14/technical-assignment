import logging
import uuid


from data_processing.models import DataEntry as DataItem
from data_processing.services.data_validator import DataValidator

logger = logging.getLogger(__name__)


class DataProcessor:

    def __init__(self):
        self.validator = DataValidator()

    def process_item(self, data_item):
        item_id = data_item.get('id') or str(uuid.uuid4())

        data_string0 = data_item.get('dataString0', '')  # URL
        data_string1 = data_item.get('dataString1', '')  # DateTime
        data_string2 = data_item.get('dataString2', '')  # Category
        data_string3 = data_item.get('dataString3', '')  # Postal Code
        data_string4 = data_item.get('dataString4', '')  # String
        data_string5 = data_item.get('dataString5', '')  # Integer/Double

        grades = {
            'dataString0': self.validator.validate_url(data_string0),
            'dataString1': self.validator.validate_date(data_string1),
            'dataString2': self.validator.validate_category(data_string2),
            'dataString3': self.validator.validate_postcode(data_string3),
            'dataString4': self.validator.validate_string(data_string4),
            'dataString5': self.validator.validate_number(data_string5),
        }

        overall_grade = min(grades.values())
        logger.info(f"Overall grade for item {item_id}: {overall_grade}")

        try:
            # Try to parse the datetime string
            try:
                from datetime import datetime
                datetime_obj = datetime.strptime(data_string1, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    datetime_obj = datetime.strptime(data_string1, '%H:%M%p %Y-%m-%d')
                except ValueError:
                    datetime_obj = datetime.now()

            # Map to model fields
            data_item_instance = DataItem(
                external_id=item_id,
                url=data_string0,
                datetime=datetime_obj,
                category=data_string2,
                postal_code=data_string3,
                additional_info=data_string4,
                numeric_data=data_string5,
                grade=overall_grade
            )
            data_item_instance.save()
            logger.info(f"Data item {item_id} saved successfully with grade {overall_grade}")
            return overall_grade
        except Exception as e:
            logger.error(f"Error saving data item {item_id}: {e}")
            return 'D'