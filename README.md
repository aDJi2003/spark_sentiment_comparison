<h1>Spark Sentiment Comparasion</h1>
A sentiment analysis project comparing tweets about two political figures—Trump and Kamala—using PySpark and NLTK. This project fetches tweets, cleans the text, analyzes the sentiment, and visualizes sentiment distribution, helping to determine which figure has a higher positive sentiment score.

<h2>Key Objectives</h2>
<ul>
  <li>Clean and preprocess tweet data</li>
  <li>Perform sentiment analysis on tweet content</li>
  <li>Visualize sentiment distribution for comparison</li>
  <li>Determine which candidate has more positive sentiment</li>
</ul>

<h2>Features</h2>
<ul>
  <li><b>Data Preprocessing</b>: Cleans tweet text by removing URLs, mentions, and special characters.</li>
  <li><b>Sentiment Analysis</b>: Uses NLTK’s Vader to determine sentiment (positive/negative).</li>
  <li><b>Data Visualization</b>: Generates a line plot showing sentiment distribution between the two candidates.</li>
  <li><b>Result Summary</b>: Prints a message indicating the candidate with the higher positive sentiment.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li><b>PySpark</b>: For data processing and transformation</li>
  <li><b>NLTK</b>: Sentiment analysis with Vader</li>
  <li><b>Pandas</b>: Data manipulation and analysis</li>
  <li><b>Matplotlib and Seaborn</b>: Data visualization</li>
  <li><b>Docker</b>: Containerization for easy setup</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li><b>Python 3.8+</b>: Make sure you have Python installed.</li>
  <li><b>Docker</b>: Required to run the project in a container.</li>
  <li><b>Twitter API</b>: If you wish to fetch live tweets, you'll need Twitter API credentials.</li>
  <li><b>Dependecies</b>: See `requirements.txt` for the list of required Python packages.</li>
</ul>

<h2>Installation</h2>
<b>Clone the Repository</b>
```
git clone https://github.com/aDJi2003/spark_sentiment_comparasion.git
cd SentimentComparison
```
<b>Build Docker Image</b>
```
docker build -t sentiment_analysis_image .
```
<b>Run the Docker Container</b>
```
docker run -it -v your_local_path sentiment_analysis_image
```