
# import requests
# from bs4 import BeautifulSoup
# url = "https://coinmarketcap.com/currencies/solana/"

# r = requests.get(url)
# htmlContent = r.content

# soup = BeautifulSoup(htmlContent, 'html.parser')

# print(soup.find('div', class_='sc-aef7b723-0 dDQUel priceTitle').get_text())


import websocket
import json

def on_message(ws, message):
    message = json.loads(message)
    print(message)

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Closed connection")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.coincap.io/prices?assets=solana",
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)
    ws.run_forever()

