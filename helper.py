from selenium.webdriver.support.color import Color
import webcolors
from datetime import datetime

def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y %H:%M")
        return True
    except ValueError:
        return False


def validate_amount_value_format(amount_value):
    try:
        # Convert the value to a floating-point number and check the number of digits after the decimal point
        amount = float(amount_value)
        decimal_digits = len(str(amount).split(".")[-1])
        return decimal_digits <= 3
    except ValueError:
        return False


def validate_jpy_currency(amount_text):
    # Check if the amount has non-zero digits after the decimal point
    if "." in amount_text:
        decimal_digits = amount_text.split(".")[1]
        if decimal_digits != "0":
            return False
    return True


def convert_color(background_color):
    # Converts the background color from CSS format to a color name.
    color_background_object = Color.from_string(background_color)
    color_name_hex = color_background_object.hex
    color_name = webcolors.rgb_to_name(webcolors.hex_to_rgb(color_name_hex))
    return color_name
