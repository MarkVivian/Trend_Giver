from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scrapper.useful import get_content_selenium, get_content_beautifulSoup
import os

class DataLogger:
    def __init__(self, url):
        # Initialize the URL for scraping
        self.url_all_images = url

    def site_navigation(self):
        # Get all the divs with the specified class attribute
        image_div = get_content_beautifulSoup(self.url_all_images).find_all('div', class_='col-sm-4 col-md-4')

        # Extract the href attribute from the first 'a' element within each div
        image_links = [div.find('a')['href'] for div in image_div]

        for link in image_links:
            # Initialize a Selenium webdriver for the current image page
            scrapper = get_content_selenium(link)

            try:
                # Wait for the dropdown button to be present and then click it
                dropdown_button = WebDriverWait(scrapper, 5).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'dropdown-toggle'))
                )
                dropdown_button.click()

                # Wait for the dropdown options to be visible and then click the first option
                dropdown_options = WebDriverWait(scrapper, 5).until(
                    ec.visibility_of_all_elements_located((By.CLASS_NAME, 'dropdown-item'))
                )
                dropdown_options[0].click()
                sleep(10)
                print("done with downloading.")

                try:
                    # Extract the nametag for the image downloaded
                    # create a checker which will check if name_tag has anything and if there is no value then it uses link.split('/')[-2]
                    name_tag = ((get_content_beautifulSoup(link).find_all('div', class_='box'))[1].find('h5')).text
                    name_tag = name_tag.replace(' ', '_')
                except Exception:
                    name_tag = link.split('/')[-2]
                    name_tag = name_tag.replace('-', '_')

                print(f"using name tag {name_tag}")

                # Replace spaces in the nametag with underscores
                print(f"Downloaded {name_tag}")

                # Extract the unique identifier for the image from the URL
                image_identifier = link.split('/')[-1]

                # Rename the downloaded image file using the nametag
                self.naming_handler(image_identifier, name_tag)

            except Exception as exception:
                print(f"Dropdown button not found or dropdown options not visible.")
            finally:
                # Quit the Selenium webdriver after processing the current image page
                scrapper.quit()

    @staticmethod
    def naming_handler(image_identifier, name_tag):
        # Check for .jpg images in the Downloads folder and rename them using the nametag
        # Get the home directory path
        home_directory = os.path.expanduser('~')

        # Construct the path to the Downloads folder
        download_path = os.path.join(home_directory, "Downloads")

        # Check if the Downloads folder exists
        if os.path.exists(download_path):
            # Get a list of all files in the Downloads folder
            files_in_downloads = os.listdir(download_path)

            # Filter the list to include only .jpg files
            images_in_downloads = [file for file in files_in_downloads if file.endswith('.jpg')]

            # Check if there are any .jpg files in the Downloads folder
            if images_in_downloads:
                # Filter the list to include only .jpg files that contain the image_identifier
                image = [image for image in images_in_downloads if image.__contains__(image_identifier)]

                # Check if an image with the image_identifier was found
                if image:
                    print(f"Image found: {image[0]}")

                    # Rename the image file using the nametag
                    os.rename(os.path.join(download_path, image[0]), os.path.join(download_path, name_tag + ".jpg"))
                    print(f"Renamed {image[0]} to {name_tag}.jpg")
        else:
            print(f"Downloads folder does not exist. Please download the images first.")
            exit(1)

    def runner(self):
        # Start the scraping process
        self.site_navigation()