import requests
from bs4 import BeautifulSoup
import csv
import time

# Define user-agent for requests
headers = {'User-Agent': 'Mozilla/5.0'}

# Map ratings to numbers
rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Ask for the number of pages
numPages = int(input('How many pages would you like to scrape? (Max 50): '))

# Ensure pages do not exceed the maximum
if numPages > 50:
    numPages = 50

base_url = 'http://books.toscrape.com/catalogue/page-'
pageNum = 1

# Open the CSV file before the loop to avoid overwriting
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Rating', 'Price', 'Availability'])  # Write headers

    # Loop through each page
    while pageNum <= numPages:
        # Construct the URL for each page
        page_url = f'{base_url}{pageNum}.html'

        try:
            response = requests.get(page_url, headers=headers)
            print(f"Scraping page {pageNum}: Status code {response.status_code}")

            # Stop if the page doesn't exist
            if response.status_code != 200:
                print(f"Error: Could not retrieve page {pageNum}")
                break

            soup = BeautifulSoup(response.content, 'html.parser')
            books = soup.find_all('article', class_='product_pod')
            print(f"Found {len(books)} books on page {pageNum}")

            # Scrape details from each book
            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()

                # Get numeric rating
                rating_class = book.p['class']
                rating = rating_dict.get(rating_class[-1], 'Unknown')

                # Write book details to the CSV file
                writer.writerow([title, rating, price, availability])
                print(f"Scraped: {title}, Rating: {rating}, Price: {price}, Availability: {availability}")

        except requests.RequestException as e:
            print(f"Request failed for page {pageNum}: {e}")
            break

        # Add a delay to avoid overwhelming the server
        time.sleep(2)
        pageNum += 1

print("Data successfully written to books.csv!")
