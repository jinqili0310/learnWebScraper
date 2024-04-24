# import requests
# from bs4 import BeautifulSoup
# import time
#
# URL = "https://www.chewy.com/brands/shop-by-cat-11283"
#
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
# headers = {'User-Agent': user_agent}
#
# def fetch_url(url):
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response
#     elif response.status_code == 429:
#         try:
#             retry_after = int(response.headers.get('Retry-After', 60))  # Default to 60 seconds if no header
#             print(f"Rate limit hit. Retrying after {retry_after} seconds.")
#             time.sleep(retry_after)
#             return fetch_url(url)  # Recursive retry
#         except ValueError:
#             print("Failed to parse Retry-After header. Retrying with a default delay.")
#             time.sleep(60)
#             return fetch_url(url)
#     else:
#         print(f"Failed to retrieve content, status code: {response.status_code}")
#         return None
#
# response = fetch_url(URL)
# if response:
#     soup = BeautifulSoup(response.text, "html.parser")
#     results = soup.select(".kib-product-title__text")
#     if results:
#         for result in results:
#             print(result.text.strip())
#     else:
#         print("No results found")

# .kib-product-price

# https://github.com/skickham/Chewy_Pets

import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        price_tag = soup.find('div', class_='kib-product-price')
        price = price_tag.text.strip() if price_tag else 'Price not found'
        print("Price:", price)
        return price
    else:
        print("Failed to retrieve the page")
        return None


# Example URL
url = 'https://www.chewy.com/vital-essentials-freeze-dried-raw/dp/152726'
price = get_price(url)
if price:
    print(f"The current price is: {price}")
else:
    print("Could not fetch the price")