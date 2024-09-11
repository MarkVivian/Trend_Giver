import scrapper.backiee as logger
from scrapper.useful import check_internet
from time import sleep

if __name__ == '__main__':
    retries = 0
    max_retries = 5
    i = 1
    while retries < max_retries:
        if check_internet():
            while i <= 10:
                # check if there is internet connection
                if check_internet():
                    logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
                    i += 1
                else:
                    while not check_internet():
                        sleep(input("type a time or leave it until internet access : "))
                        logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
                    i += 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
