# 📈 TIOBE Index Language Ranker

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2.31-orange.svg)](https://requests.readthedocs.io/)

This project is a high-performance web scraper designed to extract the top 20 programming languages from the **TIOBE Index**. It demonstrates professional data extraction using **Static Web Scraping** techniques and **Object-Oriented Programming (OOP)**.

## 🛠️ Tech Stack

* **Python**: Core programming language.
* **Requests**: Used for sending HTTP requests and retrieving website source code.
* **BeautifulSoup4**: Used for parsing HTML and navigating the DOM tree to find specific table elements.
* **OOP Architecture**: Code organized into classes for better maintainability and error tracking.

## 🏗️ Project Structure

The project follows a modular class-based structure (`TiobeScraper` class):
1. **get_site()**: Handles the connection and HTML retrieval.
2. **find_object()**: Specifically targets the TIOBE ranking table using unique IDs.
3. **div_columns()**: Iterates through rows, cleaning and formatting the data for the user.
4. **active()**: The orchestration method that manages the execution flow and error logging.

## 🛡️ Advanced Error Handling

This script implements a **custom debug-friendly error tracking system**. Each major function is wrapped in a `try/except` block that identifies exactly which part of the scraping process failed (Connection, Parsing, or Data Processing), making it easier to maintain if the website structure changes.

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ViniciusSantos-Tech/tiobe-scraper-oop.git](https://github.com/ViniciusSantos-Tech/tiobe-scraper-oop.git)
   ```
2. **Install requirements:**
  ```
  pip install -r requirements.txt
```
3. **Run the scraper:**
```
python tiobe_scraper.py
