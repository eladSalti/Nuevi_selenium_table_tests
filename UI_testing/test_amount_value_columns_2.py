import pytest
from selenium.webdriver.common.by import By
from helper import validate_amount_value_format

"""In this test we would like to check if the amount value columns support a decimal point separated number with 
up to 3 digits after the decimal point."""


class TestTransactions:
    @pytest.mark.amount_value_columns
    def test_amount_value_format(self, table_data):
        # Check the format of the amount value for each cell in the amount value column
        for row in table_data:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 2:
                amount_value = columns[1].text  # Assuming the amount value column is the second column (index 1)
                assert validate_amount_value_format(amount_value), f"Invalid amount value format: {amount_value}"
                # Validate the amount value format using the helper function validate_amount_value_format If the
                # format is invalid, the assert statement will raise an AssertionError with an appropriate error
                # message. The test will fail and the error message will indicate the specific amount value that
                # failed the validation.
