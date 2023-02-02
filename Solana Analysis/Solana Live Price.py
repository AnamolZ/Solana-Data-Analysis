import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {'Accepts': 'application/json', 'X-CMC_Pro_API_Key': 'e3763607-e592-4ba9-b6d5-3769d4a54290'}
params = {'symbol': 'BTC', 'convert': 'USD'}

data = requests.get(url, headers=headers, params=params).json()
d = data['data'][list(data['data'].keys())[0]]
quote = d['quote']['USD']

symbol = d['symbol']
price = "${:.2f}".format(quote['price'])
volume = "${:,.2f}".format(quote['volume_24h'])
change = "{:.2f}%".format(quote['volume_change_24h'])
percent1h = "{:.2f}%".format(quote['percent_change_1h'])
percent24h = "{:.2f}%".format(quote['percent_change_24h'])

print(f"\nSymbol: {symbol}\nPrice: {price}\n\n24_Hour\nTraded: {volume}\nChange: {change}\n\nPercent\n1 Hour: {percent1h}\n24 Hour: {percent24h}")