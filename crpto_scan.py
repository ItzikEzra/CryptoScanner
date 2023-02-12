import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import numpy as np


# get all the relevant list from  scalpstation
def fetch_coins_from_scalpstation():
    # Open the browser
    service_obj = Service("C:\webdriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    url_site = 'https://scalpstation.com/'
    driver.get(url_site)

    # fetch all the relevant elements
    list_of_coins = driver.find_elements(By.CLASS_NAME, 'symbol-name')  # BTC
    list_of_coins_usdt_suffix = []

    # adding usdt suffix for binance api
    for e in list_of_coins:
        list_of_coins_usdt_suffix.append(e.text + 'usdt')  # BTC -> BTCUSDT
    return list_of_coins_usdt_suffix


# get the market data from binance api

def get_market_data(symbol, interval, start_time, end_time):
    # Define the API endpoint for retrieving the market data
    endpoint = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}"

    # Make the API request
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception("Failed to retrieve market data")

    # Convert the response to a pandas DataFrame
    market_data = pd.DataFrame(response.json(),
                               columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
                                        "Quote asset volume", "Number of trades", "Taker buy base asset volume",
                                        "Taker buy quote asset volume", "Ignore"])

    # Convert the timestamps to datetime objects
    market_data["Open time"] = pd.to_datetime(market_data["Open time"], unit='ms')
    market_data["Close time"] = pd.to_datetime(market_data["Close time"], unit='ms')

    # Set the index to the close time
    market_data.set_index("Close time", inplace=True)

    # Keep only the close price
    market_data = market_data[["Close"]]

    return market_data


# according to the desire strategy, this will return bollinger info
def calculate_bollinger_bands(symbol, market_data, window_size=21, num_std=2):
    # Calculate the moving average
    middle_band = market_data["Close"].rolling(window=window_size).mean()

    # Calculate the standard deviation
    std = market_data["Close"].rolling(window=window_size).std()

    # Calculate the upper and lower bands
    upper_band = middle_band + std * num_std
    lower_band = middle_band - std * num_std

    # Create a new DataFrame to store the Bollinger Bands
    bollinger_bands = pd.DataFrame({
        "symbol": symbol,
        "Middle": middle_band,
        "Upper": upper_band,
        "Lower": lower_band,
        "distance between u/l": (abs(upper_band - lower_band) / ((upper_band + lower_band) / 2)) * 100
    })

    return bollinger_bands


def calculate_rsi(market_data, window_size=14):
    # Calculate the change in close price
    delta = market_data["Close"].diff()

    # Calculate the gain and loss
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate the average gain and loss over the specified window size
    avg_gain = gain.rolling(window=window_size).mean()
    avg_loss = loss.rolling(window=window_size).mean()

    # Calculate the relative strength
    relative_strength = avg_gain / avg_loss

    # Calculate the RSI
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi


def calculate_market_profile(market_data, interval_size=10):
    # Create a list to store the market profile values
    market_profile = []

    # Split the data into intervals of the specified size
    intervals = np.array_split(market_data, interval_size)

    # Calculate the market profile for each interval
    for interval in intervals:
        high = interval["High"].max()
        low = interval["Low"].min()
        interval_range = high - low
        interval_midpoint = (high + low) / 2
        market_profile.append((interval_midpoint, interval_range))

    return market_profile


def calculate_volume_profile(market_data, interval_size=10):
    # Create a list to store the volume profile values
    volume_profile = []

    # Split the data into intervals of the specified size
    intervals = np.array_split(market_data, interval_size)

    # Calculate the volume profile for each interval
    for interval in intervals:
        volume = interval["Volume"].sum()
        volume_profile.append((interval["Close"].iloc[0], volume))

    return volume_profile
