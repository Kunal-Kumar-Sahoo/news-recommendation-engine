import schedule
import time
import datetime

from dataset_curator import scrape_and_save_headlines_to_csv

def job():
    url = 'https://timesofindia.indiatimes.com/'
    csv_filename = 'toi_headlines.csv'
    scrape_and_save_headlines_to_csv(url, csv_filename)

schedule.every().day.at('00:00').do(job)

if __name__ == '__main__':
    print("Dataset curation job scheduled to run daily at 12 AM.")
    while True:
        schedule.run_pending()
        time.sleep(60) 