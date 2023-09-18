# Import required libraries
import streamlit as st
import pandas as pd
import requests

st.write('# Alpha Vantage Crypto Exchange Rates')

API_KEY = 'demo' # Replace it with real value

from_currency = st.text_input('Enter from currency:', 'BTC').upper()
to_currency = st.text_input('Enter to currency:', 'CNY').upper()
amount = round(st.number_input('Enter amount:', 1.0, step=0.01), 2)

# API Endpoint to retrieve Current Exchange Rates
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&' \
      f'from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}'

print(url)

# Request the data, parse JSON response and store it in Python variable
r = requests.get(url, timeout=5)
data = r.json()

st.write(
    f'### {data["Realtime Currency Exchange Rate"]["2. From_Currency Name"]} to '
    f'{data["Realtime Currency Exchange Rate"]["4. To_Currency Name"]}'
)
st.write(f'### Last update: {data["Realtime Currency Exchange Rate"]["6. Last Refreshed"]}')
st.write(f'{amount} {data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]} gives {round(amount * float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]), 2)} {data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]}')
