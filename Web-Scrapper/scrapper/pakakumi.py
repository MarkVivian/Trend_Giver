import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapper.useful import get_content_selenium

class DataLogger:
    def __init__(self, url):
        # Initialize the URL for scraping
        self.site_url = url

    # Function to monitor the page and capture data when a change occurs
    def monitor_page(self, driver):
        old_odds = self.capture_odd(driver)
        old_odds_value = [odd.text for odd in self.capture_odd(driver)]

        for odd in old_odds:
            self.clicker(odd, driver)

        while True:
            new_odds = self.capture_odd(driver)
            new_odds_value = [odd.text for odd in self.capture_odd(driver)]

            if old_odds_value != new_odds_value:
                # New element detected, capture the data
                print(f"New odd captured {self.capture_odd(driver)[0]}")
                old_odds = self.capture_odd(driver)

                self.clicker(self.capture_odd(driver)[0], driver)

            # Add a small delay before checking again (if needed)
            time.sleep(2)

    def clicker(self, odd_element, driver):
        try:
            # Wait for any overlay to disappear before clicking
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "react-joyride__overlay"))
            )

            # Click the <a> element (the odd)
            odd_element.click()
            print(f"Clicked on odd: {odd_element.text}")

            # Wait for 3 seconds
            time.sleep(5)

            # You can perform more actions here after clicking the link
            self.extracting_table_elements(driver)

            # After the actions, you might want to go back to the previous page
            driver.back()  # Go back to the previous page

        except Exception as e:
            print(f"An error occurred while clicking on the odd: {e}")

    def site_navigation(self):
        driver = get_content_selenium(self.site_url)
        self.monitor_page(driver)


    def extracting_table_elements(self, driver):
        try:
            data_storage = []

            # Find element by their tags, class_name (e.g., 'css-an5cfz')
            # Attempt to find the div with the betters' info.
            div = driver.find_element(By.CLASS_NAME, 'css-v5ykae')

            # Attempt to find the table inside the div
            table_betters = div.find_element(By.TAG_NAME, 'table')

            # Find the tbody inside the table
            tbody_betters = table_betters.find_element(By.TAG_NAME, 'tbody')

            # Extract the rows (betters) from the tbody.
            rows_betters = tbody_betters.find_elements(By.TAG_NAME, 'tr')

            # Loop through each row (better)
            for row in rows_betters[1:]:
                # Extract the columns (name, odds, winning amount, etc.)
                cols_better = row.find_elements(By.TAG_NAME, 'td')

                # Extract the better's name, odds, and winning amount
                better_name = cols_better[0].text
                odds = cols_better[1].text
                amount_bet = cols_better[2].text
                profit = cols_better[3].text

                # put it in a object format.
                better_info = {
                    'name': better_name,
                    'odds': odds,
                    'amount_bet': amount_bet,
                    'profit': profit
                }

                data_storage.append(better_info)
            # return the better's information
            return data_storage
        except StaleElementReferenceException as ste:
            print("StaleElementReferenceException: The element reference is no longer valid. Retrying...")
            # Re-capture data or call capture_table_data again
            self.extracting_table_elements(driver)  # Retry capturing the table data
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def capture_odd(driver):
        # Find the div containing the odds
        stopping_odd = driver.find_element(By.CLASS_NAME, 'css-xy3rl8')

        # Capture the <a> elements within the specified class
        odd_elements = stopping_odd.find_elements(By.CLASS_NAME, 'css-19toqs6')

        return odd_elements  # Return the list of <a> elements


    def runner(self):
        # Start the scraping process
        self.site_navigation()