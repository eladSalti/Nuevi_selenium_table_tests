import pytest
from selenium.webdriver.common.by import By
import helper

"""In this test we would like to verify the color background of the status column (approved – green || pending – 
Yellow || rejected - Red)"""


class TestStatusColor:
    @pytest.mark.test_status_color
    def test_jpy_amount_validation(self, table_data):
        # Create dictionaries to store cells with incorrect colors for each status
        not_green_cells = {}
        not_yellow_cells = {}
        not_red_cells = {}

        for row_number, row in enumerate(table_data, start=1):
            columns = row.find_elements(By.TAG_NAME, "td")
            for column, col_element in enumerate(columns):
                text = col_element.text
                background_color = col_element.value_of_css_property("background-color")
                color_name = helper.convert_color(background_color)

                # Add the cell to the not_green_cells dictionary with row and column information
                if "approved" in text and color_name != "green":
                    not_green_cells['approved'] = {
                        "row": "the row is: " + str(row_number),
                        "column": "the column is: " + str(column) + ' This is not a green color'
                    }
                # Add the cell to the not_yellow_cells dictionary with row and column information
                elif "pending" in text and color_name != "yellow":
                    not_yellow_cells['pending'] = {
                        "row": "the row is: " + str(row_number),
                        "column": "the column is: " + str(column) + ' This is not a yellow color'
                    }
                # Add the cell to the not_red_cells dictionary with row and column information
                elif "rejected" in text and color_name != "red":
                    not_red_cells['rejected'] = {
                        "row": "the row is: " + str(row_number),
                        "column": "the column is: " + str(column) + ' This is not a red color',
                    }
        # Create a result dictionary to collect all the invalid cells for each status
        result = {
            'not_green': not_green_cells,
            'not_yellow': not_yellow_cells,
            'not_red': not_red_cells
        }
        # Check if all the dictionaries for each status are empty, indicating no cells with incorrect colors
        assert not_green_cells == {} and not_yellow_cells == {} and not_red_cells == {}, f"There are some cells that " \
                                                                                         f"have wrong color {result}"
