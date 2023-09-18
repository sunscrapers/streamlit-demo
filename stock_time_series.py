# Import required libraries
import streamlit as st
import pandas as pd
import requests

st.write('# Alpha Vantage stock price data')

API_KEY = 'demo' # Replace it with real value

# Ask user for stock symbol
symbol = st.text_input('Enter stock symbol:', 'IBM').upper()

# API Endpoint to retrieve Daily Time Series
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

# Request the data, parse JSON response and store it in Python variable
r = requests.get(url, timeout=5)
data = r.json()

# Extract basic information from collected data
information = data['Meta Data']['1. Information']
symbol = data['Meta Data']['2. Symbol']
last_refreshed = data['Meta Data']['3. Last Refreshed']

# Display the collected data to user using Streamline functions
st.write('## ' + information)
st.write('### ' + symbol)
st.write('### Last update: ' + last_refreshed)

st.write('## Time Series (Daily)')

# Use Pandas' Data Frame to prepare data to be displayed in charts
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')

df = df.reset_index()
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

df['open'] = df['open'].astype(float)
df['high'] = df['high'].astype(float)
df['low'] = df['low'].astype(float)
df['close'] = df['close'].astype(float)
df['volume'] = df['volume'].astype(int)

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Display Streamline charts
st.line_chart(df.set_index('date')[['open', 'high', 'low', 'close']])
st.bar_chart(df.set_index('date')['volume'])
