import pytest
from selenium.webdriver.common.by import By


class TestTransactionOrder:
    @pytest.mark.test_transaction_order
    def test_transactions_ordered_by_last_modified(self, table_data):
        # Get the table headers
        header_row = table_data[0]
        header_columns = header_row.find_elements(By.TAG_NAME, "th")

        # Find the index of the "Last Modified" column
        last_modified_index = None
        for i in range(len(header_columns)):
            if header_columns[i].text == "Last Modified":
                last_modified_index = i
                break

        assert last_modified_index is not None, "Last Modified column not found"

        # Collect the values from the "Last Modified" column
        last_modified_values = []
        row_number = 1  # Start from row 1 (excluding the header row)
        failed_cells = {}  # Dictionary to store the failed cells
        for row in table_data[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            last_modified_values.append(columns[last_modified_index].text)

            # Verify that the values are sorted in descending order
            sorted_values = sorted(last_modified_values, reverse=True)
            if last_modified_values != sorted_values:
                failed_cells[(row_number, last_modified_index)] = columns[last_modified_index].text

            row_number += 1

        # Check if any cells failed the test
        assert len(failed_cells) == 0, f"Transactions are not ordered by Last Modified. Failed cells: {failed_cells}"
