from scraper import scrape_toi_headlines
import csv

def scrape_and_save_headlines_to_csv(url, csv_filename):
    try:
        headlines = scrape_toi_headlines(url)

        if headlines:
            with open(csv_filename, 'w', newline='') as csvfile:
                fieldnames = ['headline', 'link']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for headline in headlines:
                    writer.writerow(headline)
            print(f'Headlines saved to {csv_filename}')
        else:
            print('Failed to retrieve headlines from the web page.')

    except Exception as e:
        print('Error:', str(e))

if __name__ == '__main__':
    url = 'https://timesofindia.indiatimes.com/'
    csv_filename = 'toi_headlines.csv'
    scrape_and_save_headlines_to_csv(url, csv_filename)
