import shutil

import scrapper.backiee as logger
from scrapper.useful import check_internet
from time import sleep
import os

def move_to_folder():
    # Check for .jpg images in the Downloads folder and move to the cars folder.
    # Get the home directory path
    home_directory = os.path.expanduser('~')

    # Construct the path to the Downloads folder
    downloads_directory = os.path.join(home_directory, 'Downloads')
    cars_folder = os.path.join(downloads_directory, "cars")

    # check for all the jpg files in the downloads_directory and move them to the cars_folder
    if os.path.exists(downloads_directory) :
        files_in_downloads = os.listdir(downloads_directory)
        images_in_downloads = [file for file in files_in_downloads if file.endswith('.jpg')]

        if images_in_downloads:
            if not os.path.exists(cars_folder):
                os.makedirs(cars_folder)

            for image in images_in_downloads:
                image_path = os.path.join(downloads_directory, image)
                # if the file exists in the destination then it skips the file
                if os.path.isfile(os.path.join(cars_folder, image)):
                    print(f"{image} already exists in cars folder.")
                    os.remove(image_path)  # Delete the image in the original location
                else:
                    # Move the image to the cars folder
                    shutil.move(image_path, cars_folder)
                    print(f"Moved {image} to cars folder.")

    else:
        print("No Downloads folder found.")


if __name__ == '__main__':
    # Initialize retry counters
    retries = 0
    max_retries = 5
    i = 5

    # Loop until we reach the desired number of pages (10 in this case)
    while i <= 50:
        # Inner loop for retries
        while retries < max_retries:
            # Check if there is an internet connection
            if check_internet():
                try:
                    # Scrape the data from the website
                    logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
                    i += 1
                    print(f"done with page {i} \n\n\n")

                    # move all the jpg files in the downloads directory
                    move_to_folder()
                    break  # Break out of the inner loop after successful scraping

                except Exception as e:
                    retries += 1
                    print(f"An error occurred while trying to navigate the website: {e}")
            else:
                try:
                    # Wait for 60 seconds before retrying if there is no internet connection
                    sleep(60)
                    logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
                    retries += 1
                except Exception as e:
                    retries += 1
                    print(f"No internet connection available: {e}")