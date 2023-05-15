import requests
import csv
from datetime import datetime

api_key = 'fbac63a8b3c7421099fc35f6f5e9c72b'

# Get the search query from user input
search_query = input("Enter the search query: ")

# Make a GET request to the NewsAPI
response = requests.get(
    f'https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}'
)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the URLs from the response
    articles = data['articles']
    article_urls = [article['url'] for article in articles]

    # Generate a unique filename based on date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"news_urls_{current_time}.csv"

    # Save the URLs in a CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])
        writer.writerows(zip(article_urls))

    print(f"URLs saved in {filename} successfully.")
else:
    print('Error occurred while making the API request.')
