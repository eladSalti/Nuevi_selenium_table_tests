import pytest
from selenium.webdriver.common.by import By
from datetime import datetime

"""In this test we would like to check if the dates in Date Created column are equal or early than the dates in Last 
Modified column"""


class TestValidateDates:
    @pytest.mark.test_validate_dates
    def test_validate_dates(self, table_data):
        pass
        # Get the table headers
        header_row = table_data[0]
        header_columns = header_row.find_elements(By.TAG_NAME, "th")

        # Find the index of the "Last Modified" column
        last_modified_index = None
        for i in range(len(header_columns)):
            if header_columns[i].text == "Last Modified":
                last_modified_index = i
                break
        # Check if the Last Modified column is exists
        assert last_modified_index is not None, "Last Modified column was not found"

        # Collect the values from the "Last Modified" column
        last_modified_values = []
        row_number = 1  # Start from row 1 (excluding the header row)
        for row in table_data[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            last_modified_values.append(columns[last_modified_index].text)

        # Find the index of the "Last Modified" column
        date_created_index = None
        for i in range(len(header_columns)):
            if header_columns[i].text == "Date Created":
                date_created_index = i
                break
        # Check if the Date Created column is exists
        assert date_created_index is not None, "Date created column was not found"

        # Collect the values from the "Date Created" column
        date_created_values = []
        row_number = 1  # Start from row 1 (excluding the header row)
        for row in table_data[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            date_created_values.append(columns[date_created_index].text)

        # Check if the columns are equal in order to do the date and time compare
        assert len(date_created_values) == len(last_modified_values)

        # Validate the dates
        # We would like to pass the cells with the Invalid date value
        for i in range(len(last_modified_values)):
            if date_created_values[i] != "Invalid date" or last_modified_values[i] != "Invalid date":
                try:
                    last_modified = datetime.strptime(last_modified_values[i], "%d-%m-%Y %H:%M")
                    date_created = datetime.strptime(date_created_values[i], "%d-%m-%Y %H:%M")
                    assert last_modified >= date_created, f"Last Modified value '{last_modified}' is earlier " \
                                                          f"than Date Created value '{date_created}' (Row: {i}, " \
                                                          f"Last Modified Column: {last_modified_index + 1}," \
                                                          f" Date Created Column: {date_created_index + 1})"
                except ValueError:
                    pass
