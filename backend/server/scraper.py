import requests
from bs4 import BeautifulSoup

def scrape_toi_headlines(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the div elements with the class "col_l_6"
            divs = soup.find_all('div', class_='col_l_6')

            headlines = []

            # Loop through the div elements and extract the data you need
            for div in divs:
                try:
                    # Extract the headline text from the figcaption
                    headline_text = div.find('figcaption').text.strip()

                    # Extract the link to the news article from the anchor inside the div
                    headline_link = div.find('a')['href']

                    headlines.append({
                        'headline': headline_text,
                        'link': headline_link
                    })
                except:
                    pass

            return headlines
        else:
            return None
    except Exception as e:
        print('Error:', str(e))
        return None

if __name__ == '__main__':
    url = 'https://timesofindia.indiatimes.com/'
    headlines = scrape_toi_headlines(url)
    if headlines:
        for headline in headlines:
            print(f"Headline: {headline['headline']}")
            print(f"Link: {headline['link']}")
            print()
    else:
        print('Failed to retrieve the web page.')

