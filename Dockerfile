# Gunakan image base Python
FROM python:3.8-slim

# Instal Java untuk Spark
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean;

# Set variabel lingkungan untuk Java
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

# Instal dependensi Python
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m nltk.downloader vader_lexicon

# Salin seluruh kode ke dalam Docker container
COPY . /app

# Set working directory
WORKDIR /app

# Jalankan kode Python utama
CMD ["python", "main.py"]
