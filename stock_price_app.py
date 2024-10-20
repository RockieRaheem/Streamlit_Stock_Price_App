import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# KAMWANGA RAHIIM
""")

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Apple!        

""")
#define the ticker symbol
tickerSymbol = 'AAPL'   # Google  GOOGL

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
 
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# open high Low Close Volume Dividends Stock Splits

st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)