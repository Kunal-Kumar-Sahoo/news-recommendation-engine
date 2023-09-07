from scraper import scrape_toi_headlines
import csv

def scrape_and_save_headlines_to_csv(url, csv_filename):
    try:
        headlines = scrape_toi_headlines(url)

        if headlines:
            with open(csv_filename, 'a', newline='') as csvfile:  # Use 'a' for append mode
                fieldnames = ['headline', 'link']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Check if the file is empty, and if so, write the header row
                if csvfile.tell() == 0:
                    writer.writeheader()
                
                for headline in headlines:
                    writer.writerow(headline)
            print(f'New headlines appended to {csv_filename}')
        else:
            print('Failed to retrieve headlines from the web page.')

    except Exception as e:
        print('Error:', str(e))

if __name__ == '__main__':
    url = 'https://timesofindia.indiatimes.com/'
    csv_filename = './backend/dataset/toi_headlines.csv'
    scrape_and_save_headlines_to_csv(url, csv_filename)
