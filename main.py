import requests
from bs4 import BeautifulSoup
from datetime import datetime


# supplies user with a list of common ticker symbols
# useful if the user is unfamiliar with the stock market
def ticker_symbol_menu():
    menu = '\nAAPL: Apple\n' \
           'MSFT: Microsoft\n' \
           'AMZN: Amazon\n' \
           'TSLA: Tesla\n' \
           'SBUX: Starbucks\n' \
           'NVDA: Nvidia\n' \
           'GME:  GameStop\n' \
           'VZ:   Verizon\n' \
           'BBY:  Best Buy\n' \
           'DIS:  Disney\n' \
           'NFLX: Netflix'
    print(menu + '\n\n')
    # time.sleep(2)


# removes parentheses and ticker symbol from text that includes the company's name
def clean_name(n):
    for i in range(len(n)):  # go up to parentheses, and omit the ticker symbol
        if n[i] == '(':
            return n[:i-1]
    return n


def stock_scraper():
    # make sure that the user inputs a valid ticker
    # if invalid, error AttributeError when soup.find() because soup can't find data id = 50
    name = None  # name of the company
    price = None # price of the stock
    while True:
        try:
            ticker = input('Enter a ticker symbol:\n'
                           '  If you need a list of ticker symbols, type "menu"\n'
                           '  If you wish to exit the program, type "exit"\n'
                           'Ticker Symbol:  ')
            if ticker.lower() == 'menu':
                ticker_symbol_menu()
                continue
            elif ticker.lower() == 'exit':
                print('Goodbye human...')
                # time.sleep(1)
                break

            url = 'https://finance.yahoo.com/quote/' + ticker
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            # print(soup.prettify())
            price = soup.find('span', {'data-reactid': '50'}).text
            name = clean_name(soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text)

        except AttributeError:
            print('Invalid ticker symbol. Please try again...\n\n')
            # time.sleep(1)
        else:
            break

    if price and name:
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'\nAt {current_time}, the current price of a share of {name} is ${price}.')


def ui_stock_scraper(ticker):
    try:
        url = 'https://finance.yahoo.com/quote/' + ticker
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify())
        price = soup.find('span', {'data-reactid': '50'}).text
        name = clean_name(soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text)

    except AttributeError:
        return f'{ticker} is not a valid ticker symbol.\n'
    else:
        if price and name:
            current_time = datetime.now().strftime('%H:%M:%S')
            return f'At {current_time}, the current price of a share of {name} is ${price}.\n'


def trending_scraper():
    r = requests.get('https://finance.yahoo.com/trending-tickers/')
    soup = BeautifulSoup(r.text, 'html.parser')
    trs = soup.find('tbody', {'data-reactid': '54'}).findAll('tr')
    trending_array = []
    for tr in trs:
        ticker_symbol = tr.find('td').find('a').text
        name = tr.findAll('td')[1].text
        positive = True if tr.findAll('td')[4].text[0] == '+' else False
        array_element = [name, ticker_symbol, positive]
        trending_array.append(array_element)
    return trending_array


if __name__ == '__main__':
    print('Welcome user')
    trending_scraper()