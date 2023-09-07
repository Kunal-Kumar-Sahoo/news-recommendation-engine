from flask import Flask, jsonify
import csv

from scheduler import job
from dataset_curator import scrape_and_save_headlines_to_csv

app = Flask(__name__)

csv_filename = './backend/dataset/toi_headlines.csv'

# Function to retrieve news headlines from the CSV file
def read_headlines_from_csv():
    headlines = []
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            headlines.append(row)
    return headlines

# API endpoint to get all news headlines
@app.route('/api/news', methods=['GET'])
def get_all_news():
    headlines = read_headlines_from_csv()
    return jsonify({'headlines': headlines})

# API endpoint to get a specific news headline by index
@app.route('/api/news/<int:index>', methods=['GET'])
def get_news_by_index(index):
    headlines = read_headlines_from_csv()
    if 0 <= index < len(headlines):
        return jsonify(headlines[index])
    else:
        return jsonify({'message': 'News not found'}), 404

if __name__ == '__main__':
    # Start the scraping and writing task immediately
    scheduled_scrape_and_write()

    # Start the Flask application
    app.run(debug=True)