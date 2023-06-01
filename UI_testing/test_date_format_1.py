import pytest
from selenium.webdriver.common.by import By
import helper

class TestValidateDates:
    @pytest.mark.test_validate_dates
    def test_validate_dates(self, table_data):
        # Get the table headers
        header_row = table_data[0]
        header_columns = header_row.find_elements(By.TAG_NAME, "th")

        # Find the indexes of the relevant columns
        date_index = None
        last_modified_index = None
        date_created_index = None

        for i, column in enumerate(header_columns):
            if column.text == "Date":
                date_index = i
            elif column.text == "Last Modified":
                last_modified_index = i
            elif column.text == "Date Created":
                date_created_index = i

        assert date_index is not None, "Date column was not found"
        assert last_modified_index is not None, "Last Modified column was not found"
        assert date_created_index is not None, "Date Created column was not found"

        # Collect the date values from the table
        date_values = []
        last_modified_values = []
        date_created_values = []

        invalid_dates = []

        for row_number, row in enumerate(table_data[1:], start=2):  # Start from row 2 (excluding the header row)
            columns = row.find_elements(By.TAG_NAME, "td")

            date_values.append(columns[date_index].text)
            last_modified_values.append(columns[last_modified_index].text)
            date_created_values.append(columns[date_created_index].text)

            # Validate the date format
            if not helper.validate_date_format(columns[date_index].text):
                invalid_dates.append((row_number, date_index, "Date"))
            if not helper.validate_date_format(columns[last_modified_index].text):
                invalid_dates.append((row_number, last_modified_index, "Last Modified"))
            if not helper.validate_date_format(columns[date_created_index].text):
                invalid_dates.append((row_number, date_created_index, "Date Created"))

        # Assert that there are no invalid dates and print the invalid dates with row and column numbers
        assert not invalid_dates, f"There are {len(invalid_dates)} invalid dates found. " \
                                   f"Please check the following rows and columns:\n" \
                                   f"{', '.join(f'Row {row}, Column {col} in {column}' for row, col, column in invalid_dates)}"
