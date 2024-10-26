import sys

sentiment_count = {}

for line in sys.stdin:
    line = line.strip()
    sentiment, count = line.split("\t")
    count = int(count)
    
    if sentiment in sentiment_count:
        sentiment_count[sentiment] += count
    else:
        sentiment_count[sentiment] = count

for sentiment, count in sentiment_count.items():
    print(f"{sentiment}\t{count}")