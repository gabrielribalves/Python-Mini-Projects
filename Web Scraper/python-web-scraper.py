import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

base_url = 'https://quotes.toscrape.com'
page = requests.get(base_url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
next_li_element = soup.find('li', class_='next')

# h1_elements = soup.find_all('h1')
# main_title_element = soup.find(id='main-title')
# footer_element = soup.find(text={'Powered by WordPress'})
# email_element = soup.find(attrs={'name': 'email'})
# centered_element = soup.find_all(class_='text-center')
# soup.find(class_='navbar').find_all('li')
# soup.select('.navbar > li')

quotes = []
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']
    page = requests.get(base_url + next_page_relative_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    quote_elements =soup.find_all('div', class_='quote')

    # print(quote_elements)
    for quote_element in quote_elements:
        text = quote_element.find('span', class_='text').text
        author = quote_element.find('small', class_='author').text
        tag_elements = quote_element.find_all('a', class_='tag')
        tagsList =[]
        for tag_element in tag_elements:
            tagsList.append(tag_element.text)
        quotes.append(
            {
                'text': text,
                'author': author,
                'tags': ', '.join(tagsList)
            }
        )

    next_li_element = soup.find('li', class_='next')


csv_file = open('quotes.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(csv_file)

writer.writerow(['Text', 'Author', 'Tags'])

for quote in quotes:
    writer.writerow(quote.values())

csv_file.close()