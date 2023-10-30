# the URL of the home page of the target website
base_url = 'https://quotes.toscrape.com'

# retrieve the page and initializing soup...

# get the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # get the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parse the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    quotes = []
    quote_elements =soup.find_all('div', class_='quote')

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
    print(quotes)
    # look for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')