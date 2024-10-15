from src.scrape import scrape
from src.save_data_csv import save_data_csv

if __name__ == '__main__':
    #save in csv file
    scrape('https://www.amazon.com/', "coffe maker", save_data_csv)
