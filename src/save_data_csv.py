import csv

def save_data_csv(records:list, search_term:str):

    file_name = f'output/{search_term.replace(" ", "_")}.csv'

    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Description', 'Price', 'Rating', 'Amount of reviews', 'Url'])
        writer.writerows(records)