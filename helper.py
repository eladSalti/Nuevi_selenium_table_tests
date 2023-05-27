import re
from selenium.webdriver.support.color import Color
import webcolors


def validate_date_format(date_text):
    # Using regex pattern to check if the value is in the correct date format
    pattern = r"\d{2}-\d{2}-\d{4} \d{2}:\d{2}"
    return bool(re.match(pattern, date_text))


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
