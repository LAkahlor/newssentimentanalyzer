import os
import csv
import sqlite3
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def get_article_data(database_path):
    """Fetch articles data from a SQLite database."""
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles")
    articles = cursor.fetchall()
    conn.close()
    return articles

def perform_sentiment_analysis(article):
    """Perform sentiment analysis on a single article and return scores."""
    source = article[0]
    sentiment_text = article[1]
    sentiments = sia.polarity_scores(sentiment_text)
    return source, sentiments['pos'], sentiments['neg'], sentiments['neu']

def get_database_files(output_folder):
    """Fetch all .db files from a directory."""
    return [f for f in os.listdir(output_folder) if f.endswith('.db')]

def user_select_file(database_files):
    """Prompt user to select a database file."""
    print("Select a database file:")
    for i, file in enumerate(database_files, start=1):
        print(f"{i}. {file}")
    selection = int(input("Enter the number of your selection: ")) - 1
    return database_files[selection]

def calculate_average_scores(scores):
    """Calculate average of sentiment scores."""
    num_articles = len(scores)
    return sum(scores) / num_articles

def determine_overall_sentiment(average_positive_score, average_negative_score):
    """Determine the overall sentiment based on average scores."""
    average_compound_score = average_positive_score - average_negative_score
    if average_compound_score >= 0.05:
        return 'Positive'
    elif average_compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def write_to_csv(output_csv_file, data, average_scores, overall_sentiment):
    """Write sentiment analysis results to a CSV file."""
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Article/Source', 'Positive Score', 'Negative Score', 'Neutral Score'])
        writer.writerows(data)
        writer.writerow(['Average Scores', *average_scores])
        writer.writerow(['Overall Sentiment', overall_sentiment])

def main():
    output_folder = 'outputdata'
    database_files = get_database_files(output_folder)
    database_file = user_select_file(database_files)

    articles = get_article_data(os.path.join(output_folder, database_file))

    data = [perform_sentiment_analysis(article) for article in articles]
    sources, positive_scores, negative_scores, neutral_scores = zip(*data)

    average_positive_score = calculate_average_scores(positive_scores)
    average_negative_score = calculate_average_scores(negative_scores)
    average_neutral_score = calculate_average_scores(neutral_scores)

    overall_sentiment = determine_overall_sentiment(average_positive_score, average_negative_score)

    output_csv_file = os.path.join(output_folder, 'sentiment_analysis.csv')

    write_to_csv(output_csv_file, data, (average_positive_score, average_negative_score, average_neutral_score), overall_sentiment)

    print('Sentiment analysis completed. Results saved to', output_csv_file)

if __name__ == "__main__":
    main()
