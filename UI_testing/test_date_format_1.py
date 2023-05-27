import pytest
from selenium.webdriver.common.by import By
import helper

"""In this test we would like to validate the date + hour format for the date column, last Modified and Date Created"""


class TestDateFormat:

    @pytest.mark.date_format
    def test_date_format(self, table_data):
        # Get all dates from the table
        dates = [column.text for row in table_data for column in row.find_elements(By.TAG_NAME, "td") if
                 helper.validate_date_format(column.text)]

        # Check if there are any dates
        if not dates:
            pytest.fail("No dates found in the table, there was an issue with collecting elements from the table")

        # Check for incorrect date formats
        incorrect_dates = [date for date in dates if not helper.validate_date_format(date)]

        assert not incorrect_dates, f"There are at least {len(incorrect_dates)} incorrect dates, and this is the list " \
                                    f"of the incorrect dates: {incorrect_dates}"
