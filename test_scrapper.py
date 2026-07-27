# Rule of thumb is test every function and class/object that you have written inside your python module
from scrapper import scrape_quotes, quotes_to_df

def test_scrape_quotes():
    quotes = scrape_quotes(limit=3)
    assert len(quotes) == 3 # getting back 3 entries in my list or not

def test_quotes_to_df():
    df = quotes_to_df([{"ThinkPython":"Tushar"},{"AI":"Vihan"}]) # Treat this as quotes and we are passing only 2 elements
    assert df.shape[0] == 2
    assert "Quote" in df.columns
    assert "Author" in df.columns

