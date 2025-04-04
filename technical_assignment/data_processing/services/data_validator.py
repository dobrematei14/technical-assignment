import logging
from datetime import datetime
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class DataValidator:

    def validate_url(self, url):
        """
        Validate if the given URL is valid and accessible.
        """
        if not url:
            return 'F'
        try:
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                return 'A'
            else:
                return 'D'
        except Exception as e:
            logger.error(f"Error validating URL {url}: {e}")
            return 'D'

    def validate_date(self, date_str):
        """
        Validate if the given date string is in valid format.
        """
        if not date_str:
            return 'F'
        try:
            # multiple formats can be used here
            formats = [
                '%Y-%m-%dT%H:%M:%S%z',
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%dT%H:%M:%S',
                '%d-%m-%Y %H:%M:%S',
                '%Y-%m-%d %H:%M:%S',
                '%H:%M%p %Y-%m-%d',
                '%d-%m-%Y %H:%M',
            ]

            for fmt in formats:
                try:
                    datetime.strptime(date_str, fmt)
                    return 'A'
                except ValueError:
                    continue

            if 'AM' in date_str or 'PM' in date_str:
                parts = date_str.split()
                if len(parts) == 2:
                    return 'A'

                return 'C'

        except ValueError as e:
            logger.error(f"Error validating date {date_str}: {e}")
            return 'C'

    def validate_category(self, category):
        """
        Validate if category is in the correct format.
        """
        if not category:
            return 'B'

        if all(c.isprintable() for c in category):
            return 'A'
        else:
            return 'B'

    def validate_postcode(self, postcode):
        """
        Validate if the given postcode is in the correct format.
        """
        if not postcode:
            return 'F'

        postcode = postcode.replace(" ", "")
        if len(postcode) != 6:
            return 'C'
        else:
            digits = postcode[:3]
            letters = postcode[3:]
            if digits.isdigit() and letters.isalpha():
                return 'A'
            else:
                return 'C'

    def validate_string(self, string):
        """
        Validate if the given string is not empty and contains only printable characters.
        """
        if not string:
            return 'B'

        if all(c.isprintable() for c in string) and 5 <= len(string) <= 40:
            return 'A'
        else:
            return 'B'

    def validate_number(self, integer):
        """
        """
        if not integer:
            return 'B'

        try:
            float_integer = float(integer)
            if float_integer == int(float_integer) or integer.endwith('.00'):
                return 'A'
            else:
                return 'B'
        except ValueError as e:
            logger.error(f"Error validating number {integer}: {e}")
            return 'B'
