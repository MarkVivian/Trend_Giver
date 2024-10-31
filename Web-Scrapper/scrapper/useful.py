import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# cannot be used with sites which are dynamically rendered by javascript.
# for that we use selenium.
def get_content_beautifulSoup(url):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.text
        content_soup = BeautifulSoup(html_content, 'html.parser')
        return content_soup
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# used mostly for dynamically loaded pages.
def get_content_selenium(url):
    # Setup the browser (Chrome in this case)
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get(url)

    # Optional: wait for JavaScript and page content to fully load
    time.sleep(10)  # Adjust the wait time based on how long the page takes to load

    # Return the driver so it can be used later
    return driver

def check_internet(url="https://www.google.com", timeout=5):
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=timeout)
        # Check if the response code is 200 (OK)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        return False