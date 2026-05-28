# Intelligent E-Commerce Data Extraction System

An intelligent web scraping and data processing system built with Python, Playwright, BeautifulSoup, Pandas, and NLP-based sentiment analysis.

The system extracts structured e-commerce product data, cleans and deduplicates datasets, exports CSV/JSON files, and performs automated customer sentiment analysis.

---

# Features

* Dynamic web scraping with Playwright
* Multi-page asynchronous crawling
* Structured product data extraction
* Dataset cleaning and normalization
* Duplicate removal pipeline
* CSV and JSON export support
* Local NLP-based sentiment analysis
* Concurrent async scraping architecture

---

# Tech Stack

* Python
* Playwright
* BeautifulSoup4
* Pandas
* asyncio
* TextBlob
* lxml

---

# Project Structure

```bash
project/
│
├── scraper/
├── processing/
├── ai/
├── exports/
├── screenshots/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <your_repo_url>
cd intelligent-ecommerce-scraper
```

Create virtual environment:

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

# Usage

Run scraper:

```bash
python scraper/playwright_scraper.py
```

Run cleaning pipeline:

```bash
python processing/cleaner.py
```

Run sentiment analysis:

```bash
python ai/summarizer.py
```

---

# Example Outputs

## CSV Export

Structured product datasets exported to:

```bash
exports/all_books_async.csv
```

## JSON Export

```bash
exports/all_books_async.json
```

---

# Sentiment Analysis Example

```python
{
  "sentiment": "Positive",
  "score": 0.42,
  "summary": "Overall sentiment is Positive",
  "pros": [
      "Users generally like the product quality"
  ]
}
```

---

# Key Engineering Highlights

* Implemented asynchronous concurrent scraping using asyncio
* Built modular extraction and processing pipelines
* Developed automated data cleaning and deduplication systems
* Integrated NLP-based sentiment classification
* Structured exports for downstream analytics workflows

---

# Future Improvements

* Infinite scroll handling
* Proxy rotation
* CAPTCHA handling
* SQLite/PostgreSQL storage
* Dashboard analytics
* Real-time monitoring

---

# License

MIT License
