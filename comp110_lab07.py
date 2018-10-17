"""
Module: comp110_lab07

Modules with some functions for Lab 07 practice problems.
"""
import math
import urllib.request

api_key = "WKHOVZZEGLXAQLP0"

def read_stock_price(ticker_symbol, target_year):
    """
    Print the stock price for the stock whose sticker symbol is ticker_symbol,
    for all days in target_year and target_month (month is specified as an integer
    from 1 to 12.
    """
    url = urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=%s&apikey=%s&datatype=csv"
           % (ticker_symbol, api_key))
    data = url.readlines()
    lines = [line.decode('utf-8').split(',') for line in data]

    print(lines[0:5])

    price_dictionary = {}
    for line in lines[1:len(lines)]:
        date = line[0]
        date_list = date.split('-')
        year = int(date_list[0])
        month = int(date_list[1])
        price = float(line[2])
        if year == target_year:
            price_dictionary[month] = price

    return price_dictionary

def get_price_list(ticker_symbol):
    """
    Read the stock price for the stock whose sticker symbol is ticker_symbol,
    and return a list containing the prices for those months where the low price for the month
    was less than the open price for the month.  Each entry in the list should be a tuple where the
    first item in the tuple is the date, and the second entry is the low price for the day.
    """
    url = urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=%s&apikey=%s&datatype=csv"
           % (ticker_symbol, api_key))
    data = url.readlines()
    lines = [line.decode('utf-8').split(',') for line in data]

    # compute list using a loop
    price_list = []
    for line in lines[1:len(lines)]:
        date = line[0]
        open_price = float(line[1])
        low_price = float(line[3])
        if low_price < open_price:
            price_list.append((date, low_price))

    # Do the same thing using a list comprehension
    price_list_2 = [(line[0], float(line[3])) for line in lines[1:len(lines)] 
                                           if float(line[3]) < float(line[1])]

    return price_list
   

def get_earthquake_data():
    """
    Retrieves earthquake data from the USGS, and returns a list
    of tuples, one for each earthquake, that contain (date, magnitude, latitude, longitude)
    of the earthquake.
    """

    return 0  # placeholder.  You will replace the 0 here


def distance(loc1, loc2):
    """
    Returns the distance in kilometers between the locations represented by loc1 and loc2.
    Each of loc1 and loc2 is a tuple where the first element is the latitude, and the second
    element is the longitude.  Uses the Haversine formula for computing distance.
    """
    
    return 0 # placeholder.  You will replace the 0 here

def earthquake_list(max_dist, min_mag, max_mag):
    """
    Retrieves earthquake data from the USGS, and returns a list of earthquakes
    whose location is no more than max_dist km from San Diego, and whose magnitude
    is between min_mag and max_mag
    """

    return 0 # placeholder.  You will replace the 0 here