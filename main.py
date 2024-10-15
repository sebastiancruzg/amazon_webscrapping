from src.scrape import scrape
from src.models.csv.store_record_csv import store_records
from src.models.sqlite.insert_record_sqlite import insert_records

if __name__ == '__main__':
    while True:
        choice = input("Enter 1 for CSV or 2 for SQLite: ")

        if choice == '1':
            # Save in CSV file
            scrape('https://www.amazon.com/', "coffee maker", store_records)
            break
        elif choice == '2':
            # Save in SQLite
            scrape('https://www.amazon.com/', "coffee maker", insert_records)
            break
        else:
            print("Invalid input. Please enter 1 or 2.")