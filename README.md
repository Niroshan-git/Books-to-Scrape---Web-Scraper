# Books to Scrape - Web Scraper

## Overview
A Python-based web scraper designed to extract book information from "Books to Scrape" (books.toscrape.com). The scraper handles pagination automatically and collects detailed information about each book, including ratings, pricing, and categories.

![image](https://github.com/user-attachments/assets/03697588-cb2d-475b-ad5b-b7fa971b1ff8)


## Features

### 1. Automated Pagination
- Automatically traverses through all available pages
- Smart page detection with 404 handling
- Progress tracking with current page display

### 2. Comprehensive Data Extraction
For each book, the scraper collects:
- Title
- Link to detailed page
- Price
- Stock availability
- Star rating (converted to numerical value)
- Category (extracted from detailed page)

### 3. Data Export
- Exports data in multiple formats:
  - JSON (books.json)
  - CSV (books.csv)
- Structured data ready for analysis

## Technical Implementation

### Dependencies
```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
```

### Core Features

#### 1. Pagination Handler
```python
while(proceed):
    url = "https://books.toscrape.com/catalogue/page-"+ str(current_page)+".html"
    page = requests.get(url)
    if soup.title.text == "404 Not Found":
        proceed = False
```

#### 2. Data Extraction
```python
item = {
    'Title': book.find("img").attrs["alt"],
    'Link': book.find("a").attrs["href"],
    'Price': book.find("p", class_="price_color").text[2:],
    'Stock': book.find("p", class_="instock availability").text.strip()
}
```

#### 3. Rating Conversion System
```python
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
```

## Getting Started

### Prerequisites
```bash
pip install beautifulsoup4 requests pandas
```

### Running the Scraper
```bash
python book_scraper.py
```

## Data Structure

### Collected Fields
| Field    | Description                    | Type   |
|----------|--------------------------------|--------|
| Title    | Book title                     | string |
| Link     | URL to detailed page           | string |
| Price    | Book price (in £)              | float  |
| Stock    | Availability status            | string |
| Rating   | Star rating (1-5)              | int    |
| Category | Book category                  | string |

## Key Features

### 1. Error Handling
- 404 detection for pagination
- Robust HTML parsing
- Network request management

### 2. Data Processing
- Clean price extraction
- Rating normalization
- Stock status formatting

### 3. Performance
- Efficient page traversal
- Minimal memory footprint
- Optimized requests

## Applications
1. Book Price Analysis
2. Category Distribution Studies
3. Rating Analysis
4. Stock Level Monitoring
5. Market Research

## Future Improvements
1. Add async support for faster scraping
2. Implement retry mechanism
3. Add more export formats
4. Include book description scraping
5. Add data validation
6. Implement proxy support

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/book-scraper

# Install required packages
pip install -r requirements.txt

# Run the scraper
python book_scraper.py
```

## Output Examples

### JSON Format
```json
{
  "Title": "Example Book",
  "Price": "29.99",
  "Rating": 4,
  "Category": "Fiction"
}
```

### CSV Format
```csv
Title,Price,Rating,Category
Example Book,29.99,4,Fiction
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments
- BeautifulSoup4 Documentation
- Books to Scrape website for providing the data source
- Pandas Documentation

---
*Note: Please ensure compliance with the website's terms of service and robots.txt when using this scraper.*
