import scrapper.backiee as logger
from scrapper.useful import check_internet
from time import sleep

if __name__ == '__main__':
    i = 4
    while i <= 10:
        # check if there is internet connection
        if check_internet():
            logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
            i += 1
        else:
            sleep(input("type a time or leave it until internet access : "))
            logger.DataLogger(f"https://backiee.com/search/sports+car?category=car&page={i}").runner()
            i += 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
