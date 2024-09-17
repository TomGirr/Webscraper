import requests
from bs4 import BeautifulSoup
import csv
import time

numPages = int(input('How many pages would you like to scrape? (Max 50)'))
# Step 2: Make a request to the website
base_url = 'http://books.toscrape.com/catalogue/page-'
pageNum = 1
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all the books on the page
books = soup.find_all('article', class_='product_pod')

# Step 4: Prepare the CSV file outside the loop to prevent overwriting
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Rating', 'Price', 'Availability'])  # Write headers

    while pageNum <= numPages:
        # Construct the URL for each page
        page_url = f'{base_url}{pageNum}.html'

        # Request the page content
        response = requests.get(page_url)
        print(f"Scraping page {pageNum}: Status code {response.status_code}")

        if response.status_code != 200:
            print(f"Error: Could not retrieve page {pageNum}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all books
        books = soup.find_all('article', class_='product_pod')
        print(f"Found {len(books)} books on page {pageNum}")

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()

            rating_class = book.p['class']
            rating = rating_class[-1]  # Last class is the rating (e.g., "Three", "Five")

            writer.writerow([title, rating, price, availability])
            print(f"Scraped: {title}, {rating}, {price}, {availability}")

        time.sleep(2)
        pageNum += 1

print("Data successfully written to books.csv!")