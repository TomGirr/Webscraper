# Book Scraper Web App

This project is a Python-based web scraper that extracts book details (title, rating, price, and availability) from [Books to Scrape](http://books.toscrape.com/), and exports the data into a CSV file.

## Features

- Scrapes multiple pages of books (up to 50 pages).
- Extracts book title, rating (converted to numeric), price, and availability.
- Exports the data into a CSV file (`books.csv`).
- Handles pagination and basic error handling.

## Technologies Used

- **Python**: Backend logic.
- **BeautifulSoup**: HTML parsing.
- **Requests**: Web scraping.
- **CSV**: Data export.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TomGirr/Webscraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Webscraper
   ```
3. Install the required Python packages:
	```bash
	pip install
	```
### Running the Application
1. Run the script
	```bash
	python scrape.py
	```
2. Enter the number of pages you want to scrape (Max 50).
3. After scraping, the book details will be saved in a `books.csv` file in the project directory

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
