# newssentimentanalyzer
Using An Sentiment Analyzer to collect data on large numbers of world news sources. 
News Article Scraper

This script scrapes the text of news articles from a CSV file. The script first gets the CSV file from the user, then parses the CSV file to get the URLs of the news articles. The URLs are then used to make GET requests to the websites of the news articles. The HTML content of the websites is then parsed using BeautifulSoup to extract the text of the news articles. The text of the news articles is then saved to a SQLite database.

Usage

To use the script, you will need to have the following installed:

Python 3
The requests library
The BeautifulSoup library
The sqlite3 library
Once you have installed the necessary dependencies, you can run the script by following these steps:

Save the script in a directory.
Run the script by typing the following command in the terminal:
Code snippet
python news_article_scraper.py
Use code with caution. Learn more
The script will prompt you to enter the name of a CSV file that contains the URLs of the news articles. Enter the name of the CSV file and press Enter. The script will then scrape the text of the news articles and save them to a SQLite database called articles.db.


