import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_content_beautifulSoup(url):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.text
        content_soup = BeautifulSoup(html_content, 'html.parser')
        return content_soup
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def get_content_selenium(url):
    # Setup the browser (here using Chrome)
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get(url)
    return driver

def check_internet(url="https://www.google.com", timeout=5):
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=timeout)
        # Check if the response code is 200 (OK)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        return False