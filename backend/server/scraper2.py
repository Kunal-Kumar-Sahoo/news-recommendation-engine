import requests
import json
def scrapeIt(category='technology'):
    response = requests.get(f"https://newsapi.org/v2/everything?q={category}&sortBy=publishedAt&apiKey=72d6bc18cca647e69eabca0077710673")

    res= response.json()['articles']
    headlines = []
    for i in res:
        headlines.append({
            'headline': i['title'],
            'link': i['url'],
            'image': i['urlToImage'],
            'category':category
        })
    return headlines


print(scrapeIt())