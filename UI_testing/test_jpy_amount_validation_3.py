from selenium.webdriver.common.by import By
from helper import validate_jpy_currency
import pytest

"""In this test we need to make sure there are no non-zero digits after the decimal point in JPY amounts"""


class TestJPYCurrency:
    @pytest.mark.jpy_currency_format
    def test_jpy_amount_validation(self, table_data):
        # List to store invalid JPY amounts
        invalid_amounts = []

        for row in table_data:
            columns = row.find_elements(By.TAG_NAME, "td")

            for i in range(len(columns)):
                # Check if the cell contains the string "JPY"
                if "JPY" in columns[i].text:
                    # Find the JPY amount in the previous cell
                    amount_text = columns[i - 1].text

                    # Validate JPY amount format using helper function
                    if not validate_jpy_currency(amount_text):
                        # Add the invalid amount to the list
                        invalid_amounts.append(amount_text)

        # Check if there are any invalid amounts
        assert len(invalid_amounts) == 0, f"Invalid JPY amounts found: {invalid_amounts}"
