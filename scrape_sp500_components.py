# IMPORTS 
from bs4 import BeautifulSoup
import requests 

# CONSTANTS 
SP500_list = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks'

def scrape_sp500_wikipedia():
	sp500_page = requests.get(SP500_list).content
	soup = BeautifulSoup(sp500_page, 'html.parser')
	sp500_table = soup.find(id='constituents')
	
	raw_tickers = sp500_table.find('tbody').find_all('tr')[1:]
	sp500_tickers = []

	for raw_ticker in raw_tickers:
		ticker_md = raw_ticker.find_all('td')
		ticker_md = [md_elem.text for md_elem in ticker_md]
		
		sp500_ticker = {
		'symbol': ticker_md[0].split('\n')[0],
		'name': ticker_md[1],
		'sector': ticker_md[3],
		'subsector': ticker_md[4],
		'cik': ticker_md[7].split('\n')[0]
		}

		sp500_tickers.append(sp500_ticker)

	return sp500_tickers

def sort_tickers_by_industry(sp500_tickers):
	all_unique_sectors = set([(t['sector'], t['subsector']) in sp500_tickers])
	pass

if __name__ == '__main__':
	print(scrape_sp500_wikipedia())





