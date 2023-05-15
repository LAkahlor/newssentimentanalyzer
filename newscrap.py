import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sqlite3
import csv

def get_database_name():
    # Check the existing database files in the 'outputdata' folder
    output_folder = 'outputdata'
    existing_databases = [file for file in os.listdir(output_folder) if file.endswith('.db')]

    # Generate a unique database name based on the number of existing databases
    database_name = f"test{len(existing_databases) + 1}.db"
    return os.path.join(output_folder, database_name)

def create_database():
    # Set up the database connection
    db_path = get_database_name()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table for storing article data
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                    (source TEXT, article TEXT)''')

    return conn, cursor

def parse_url(url, cursor):
    # Check if the URL includes a protocol
    if not urlparse(url).scheme:
        url = "https://" + url
    
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the article or content text
        article_text = extract_article_text(soup)

        # Insert the source and article text into the database
        cursor.execute("INSERT INTO articles (source, article) VALUES (?, ?)", (url, article_text))
        
        print("Data saved for", url)
    except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as err:
        print("Error occurred while accessing the website:", str(err))
        print("Skipping this URL.")
        return  # Skip this URL and proceed to the next one

def extract_article_text(soup):
    # Placeholder implementation: Extract all text from the web page
    article_text = soup.get_text(separator=' ')

    return article_text

def scrape_articles_from_csv(csv_file):
    conn, cursor = create_database()

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            url = row[0]
            parse_url(url, cursor)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Get a list of all .csv files in the current directory
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Display the .csv files to the user and prompt them to select one
print("Select a CSV file:")
for i, file in enumerate(csv_files, start=1):
    print(f"{i}. {file}")

selection = int(input("Enter the number of your selection: ")) - 1
csv_file = csv_files[selection]

scrape_articles_from_csv(csv_file)
