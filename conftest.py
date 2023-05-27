from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="session")
def setup():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
    except Exception as e:
        # Handle the exception or raise a custom exception
        print(f"Error occurred in setup fixture: {e}")
        raise
    finally:
        if driver:
            driver.quit()


@pytest.fixture
def table_data(setup):
    driver = setup
    try:
        driver.get('http://localhost:3000')
        driver.implicitly_wait(5)
        # Get the table
        table = driver.find_element(By.ID, "root")
        # Get the table rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        return rows
    except Exception as e:
        # Handle the exception or raise a custom exception
        print(f"Error occurred in table_data fixture: {e}")
        raise
