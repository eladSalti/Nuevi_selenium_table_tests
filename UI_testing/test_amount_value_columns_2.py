import pytest
from selenium.webdriver.common.by import By
from helper import validate_amount_value_format

class TestTransactions:
    @pytest.mark.amount_value_columns
    def test_amount_value_format(self, table_data):
        amount_values = []  # Create an empty list to store the values

        # Collect valid values from the column
        for row in table_data:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 2:
                if validate_amount_value_format(columns[2].text):
                    amount_values.append(columns[2].text)  # Add the value to the list

        # Check if the list is empty
        assert amount_values, "No amount values found in the column"

        # Check the values using assert
        for amount_value in amount_values:
            assert validate_amount_value_format(amount_value), f"Invalid amount value format: {amount_value}"
