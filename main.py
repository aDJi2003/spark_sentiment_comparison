import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace
from pyspark.sql.types import StringType
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pyspark.sql.functions import pandas_udf
import matplotlib.pyplot as plt
import seaborn as sns

spark = SparkSession.builder.appName("SentimentAnalysisTrumpKamala").getOrCreate()

@pandas_udf(StringType())
def analyze_sentiment(text_series):
    sid = SentimentIntensityAnalyzer()
    return text_series.apply(lambda x: "positive" if sid.polarity_scores(x)["compound"] >= 0 else "negative")

def process_file(file_path, topic):
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    df = df.select("created_at", "favorite_count", "full_text", "reply_count", "retweet_count", "quote_count", "username", "location")
    df = df.withColumn("cleaned_text", regexp_replace(lower(col("full_text")), r"http\S+|@\w+|[^a-zA-Z\s]", ""))
    df = df.withColumn("sentiment", analyze_sentiment(col("cleaned_text")))
    sentiment_summary = df.groupBy("sentiment").count()
    print(f"Sentiment Analysis for {topic}:")
    sentiment_summary.show()
    return sentiment_summary

def plot_sentiment_distribution(trump_summary, kamala_summary):
    trump_df = trump_summary.toPandas()
    kamala_df = kamala_summary.toPandas()
    trump_df['candidate'] = 'Trump'
    kamala_df['candidate'] = 'Kamala'
    combined_df = pd.concat([trump_df, kamala_df])
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=combined_df, x='sentiment', y='count', hue='candidate', marker='o')
    plt.title("Sentiment Distribution: Trump vs Kamala")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.legend(title='Candidate')
    plt.grid()
    plt.show()

def determine_winner(trump_summary, kamala_summary):
    trump_df = trump_summary.toPandas()
    kamala_df = kamala_summary.toPandas()
    trump_positive = trump_df[trump_df["sentiment"] == "positive"]["count"].values[0]
    kamala_positive = kamala_df[kamala_df["sentiment"] == "positive"]["count"].values[0]
    print(f"Trump positive sentiment count: {trump_positive}")
    print(f"Kamala positive sentiment count: {kamala_positive}")
    if trump_positive > kamala_positive:
        winner = "Trump memiliki lebih banyak sentimen positif dan kemungkinan menjadi pemenang."
    elif kamala_positive > trump_positive:
        winner = "Kamala memiliki lebih banyak sentimen positif dan kemungkinan menjadi pemenang."
    else:
        winner = "Sentimen positif antara Trump dan Kamala seimbang."
    return winner

def show_popup(winner):
    print(winner)

if __name__ == "__main__":
    trump_summary = process_file("sentiment_analysis/kamala_tweets.csv", "Trump")
    kamala_summary = process_file("sentiment_analysis/trump_tweets.csv", "Kamala")
    plot_sentiment_distribution(trump_summary, kamala_summary) 
    winner = determine_winner(trump_summary, kamala_summary)
    show_popup(winner)
