import requests
import json

def get_sol_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data['price'])

previous_price = None

while True:
    sol_price = get_sol_price()
    if sol_price != previous_price:
        print("Latest SOL Price:", sol_price)
        previous_price = sol_price