FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean;

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m nltk.downloader vader_lexicon

COPY . /app

WORKDIR /app

CMD ["python", "main.py"]
