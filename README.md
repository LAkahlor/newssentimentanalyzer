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

Output

The SQLite database will contain the following tables:

articles: This table contains the following columns:
source: The URL of the news article
article: The text of the news article
Example

The following is an example of the output of the script:

Code snippet
>>> python news_article_scraper.py
Select a CSV file:
1. news_articles.csv

Enter the number of your selection: 1

Data saved for https://www.nytimes.com/2023/05/15/business/dealbook/elon-musk-twitter-deal.html
Data saved for https://www.washingtonpost.com/technology/2023/05/15/elon-musk-twitter-deal-final/
Data saved for https://www.cnn.com/2023/05/15/tech/elon-musk-twitter-deal-trnd/index.html
Use code with caution. Learn more
In this example, the script has scraped the text of three news articles from the CSV file news_articles.csv and saved them to the SQLite database articles.db.
