# This module is used for scraping - core-logic

# function to screpe quotes and build Pandas DF

import requests
import pandas as pd
import logging
from bs4 import BeautifulSoup
logging.basicConfig(level=logging.DEBUG)

def scrape_quotes(limit=5):
    url="https://quotes.toscrape.com/"
    response = requests.get(url) # Fetches the webpage
    if response.status_code!=200:
        print("Page not loading!!!!")
        logging.error(f"Page not loading!!!! and it return code as {response.status_code}")
        return [] # Retrun empty list
    else:
        soup = BeautifulSoup(response.text,"html.parser")
        # <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
        # quotes = [q.text for q in soup.find_all("span",class_="text")]
        # print(quotes)
        quotes = []
        for q in soup.find_all("div",class_="quote"):
            quote = q.find("span", class_="text")
            author = q.find("small",class_="author")
            print(quote)

            quotes.append({
                "Quote" : quote,
                "Author" : author
            })

        # print(quotes)
        
        return quotes[:limit] # List of quotes

# Pandas Dataframe - very handy for tabular form of representation
def quotes_to_df(quotes):
    df = pd.DataFrame(quotes, columns=["Quote","Author"])
    # print(df)
    return df
            
quote = scrape_quotes()

quotes_to_df(quote)