import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Test case to validate search functionality on Selenium Playground
def test_search_functionality():
    # Setup Chrome WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Navigate to the Selenium Playground table search demo page
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

        # Locate the search box
        search_box = driver.find_element(By.CSS_SELECTOR, "#example_filter input")

        # Enter "New York" in the search box
        search_box.send_keys("New York")
        time.sleep(2)  # Allow time for the results to update

        # Validate the search results
        rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
        visible_rows = [row for row in rows if row.is_displayed()]

        # Assert that there are 5 visible rows in the search results
        assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}"

        # Validate total entries text
        info_text = driver.find_element(By.CSS_SELECTOR, "#example_info").text
        assert "24 entries" in info_text, "Total entries text does not match"

        print("Test Passed: Search functionality works as expected.")

    finally:
        # Clean up and close the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--capture=no", "--disable-warnings", __file__])
