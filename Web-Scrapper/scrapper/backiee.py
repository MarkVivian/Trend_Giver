from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scrapper.useful import get_content_selenium, get_content_beautifulSoup
import os

class DataLogger:
    def __init__(self, url):
        self.url_all_images = url

    def site_navigation(self):
        # TODO : make this configurable
        # Get all the divs with the class attribute described.
        image_div = get_content_beautifulSoup(self.url_all_images).find_all('div', class_='col-sm-4 col-md-4')

        # find the first a in the div and get the href element.
        image_links = [div.find('a')['href'] for div in image_div]

        for link in image_links:
            # Locate the dropdown button using its class or other selectors
            scrapper = get_content_selenium(link)

            try:
                # Attempt to locate the dropdown button
                dropdown_button = WebDriverWait(scrapper, 5).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'dropdown-toggle'))
                )

                # Click the button to make the dropdown menu visible
                dropdown_button.click()

                # Wait for the dropdown options to become visible and then click the first option
                dropdown_options = WebDriverWait(scrapper, 5).until(
                    ec.visibility_of_all_elements_located((By.CLASS_NAME, 'dropdown-item'))
                )
                dropdown_options[0].click()
                sleep(5)
                print("done with downloading.")

                # also get the nametag for the image downloaded.
                name_tag = ((get_content_beautifulSoup(link).find_all('div', class_='box'))[1].find('h5')).text
                print(name_tag)

                # replace the spaces in name_tag with _
                name_tag = name_tag.replace(' ', '_')
                print(f"Downloaded {name_tag}")

                # the element after /
                image_identifier = link.split('/')[-1]

                self.naming_handler(image_identifier, name_tag)

            except Exception as exception:
                print(f"Dropdown button not found or dropdown options not visible.")
            finally:
                scrapper.quit()

    @staticmethod
    def naming_handler(image_identifier, name_tag):
        # check for .jpg images in downloads folder and check if any of their names contain image_identifier
        # get the home directory
        home_directory = os.path.expanduser('~')

        # the downloads folder path
        download_path = os.path.join(home_directory, "Downloads")

        # check if the download_path exists
        if os.path.exists(download_path):
            # get all files in downloads folder
            files_in_downloads = os.listdir(download_path)

            # check if there are any images (.jpg) files here.
            images_in_downloads = [file for file in files_in_downloads if file.endswith('.jpg')]

            # check if images_in_downloads is not empty
            if images_in_downloads:
                # check if image_identifier is in the images_in_downloads
                image = [image for image in images_in_downloads if image.__contains__(image_identifier)]
                print(f"image found {image[0]}")

                # rename the image to name_tag
                os.rename(os.path.join(download_path, image[0]), os.path.join(download_path, name_tag + ".jpg"))
                print(f"Renamed {image[0]} to {name_tag}.jpg")
        else:
            print(f"Downloads folder does not exist. Please download the images first.")
            exit(1)

    def runner(self):
        self.site_navigation()