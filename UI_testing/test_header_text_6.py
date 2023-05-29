import pytest
from selenium.webdriver.common.by import By

"""In this test we would like to validate the text in the table's header"""


class TestTableHeader:
    @pytest.mark.test_table_header
    def test_table_header_text(self, table_data):
        # Get the first row in the table (header row)
        header_row = table_data[0]

        # Get all columns in the header row
        header_columns = header_row.find_elements(By.TAG_NAME, "th")

        # Get the text from each header column
        header_texts = [column.text for column in header_columns]

        # Define the expected header text
        expected_header_text = ["Date", "ClientID", "Amount", "Currency Code", "Bank", "Status", "Last Modified", "Date Created"]

        # Compare the header text with the expected header text
        assert header_texts == expected_header_text, f"The header text does not match the expected text. " \
                                                     f"Expected: {expected_header_text}, Actual: {header_texts}"
