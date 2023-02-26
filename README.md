<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <h1>Crypto Trading Bot</h1>
    <p>This repository contains a Python script for a simple crypto trading bot. The bot fetches market data from the Binance API, calculates technical indicators, and uses them to make buy and sell decisions for a given cryptocurrency.</p>
    <h2>Dependencies</h2>
    <ul>
      <li>requests</li>
      <li>pandas</li>
      <li>selenium</li>
      <li>numpy</li>
    </ul>
	   <h2>Functions</h2>
    <ul>
      <li>fetch_coins_from_scalpstation()</li>
      <p>This function fetches all the relevant coin symbols from ScalpStation.</p>
      <li>get_market_data(symbol, interval, start_time, end_time)</li>
      <p>This function retrieves market data from the Binance API for a given currency and time interval.</p>
      <ul>
        <li>symbol: The currency symbol to retrieve market data for.</li>
        <li>interval: The time interval of the market data, e.g. "1h" for hourly data.</li>
        <li>start_time: The start time of the market data in milliseconds.</li>
        <li>end_time: The end time of the market data in milliseconds.</li>
      </ul>
      <li>calculate_bollinger_bands(symbol, market_data, window_size=21, num_std=2)</li>
      <p>This function calculates the Bollinger Bands for a given currency.</p>
      <ul>
        <li>symbol: The currency symbol to calculate Bollinger Bands for.</li>
        <li>market_data: The market data for the currency.</li>
        <li>window_size: The window size for the moving average.</li>
        <li>num_std: The number of standard deviations for the Bollinger Bands.</li>
      </ul>
      <li>calculate_rsi(market_data, window_size=14)</li>
      <p>This function calculates the Relative Strength Index (RSI) for a given currency.</p>
      <ul>
        <li>market_data: The market data for the currency.</li>
        <li>window_size: The window size for the RSI calculation.</li>
      </ul>
      <li>calculate_market_profile(market_data, interval_size=10)</li>
      <p>This function calculates the Market Profile for a given currency.</p>
      <ul>
        <li>market_data: The market data for the currency.</li>
        <li>interval_size: The size of the intervals to split the market data into.</li>
      </ul>
      <li>calculate_volume_profile(market_data, interval_size=10)</li>
      <p>This function calculates the Volume Profile for a given currency.</p>
      <ul>
        <li>market_data: The market data for the currency.</li>
        <li>interval_size: The size of the intervals to split the market data into.</li>
      </ul>
    </ul>
    <h2>Usage</h2>
    <p>To use the bot, run the `crypto_bot.py` script in a Python environment with the above dependencies installed. The bot will prompt you to enter the symbol for the cryptocurrency you want to trade, the time interval for the market data (e.g. 1m, 1h, 1d), and the start and end times for the market data (in UNIX timestamp format).</p>
    <p>By default, the bot uses a simple Bollinger Bands trading strategy, but you can modify the script to use other indicators or strategies.</p>
    <h2>Contributing</h2>
    <p>If you have any suggestions for improving this code, feel free to submit a pull request or open an issue.</p>
   
