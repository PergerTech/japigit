"""
Jared Waltisperger
IFT 458 Spring 2020
03/09/2020
Module 5 Lab
"""

import urllib.request
import json
import os


# alphavantage.co api key = 5MQNW62V7ZVYPPTE

def getStockData(stock_symbol):
    # Alphavantage API url access & set stock symbol
    target_url = \
        "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&interval=5min&apikey=5MQNW62V7ZVYPPTE".format(
            stock_symbol)

    # Creating url connection
    connection = urllib.request.urlopen(target_url)

    # Get data from connection
    response_data = connection.read().decode()
    return response_data


def main():
    input_symbol = ''
    while input_symbol != 'QUIT':
        try:
            input_symbol = input("Please enter a stock symbol for retrieval or enter \"quit\" to end: ").upper()
        except:
            print("Not a valid symbol!")

        # exit loop if user input quit
        if input_symbol == "QUIT":
            print("Thanks, Program ending!")
            break

        # Get stock data
        try:
            stock_data = getStockData(input_symbol)

            # Print data to user
            print(stock_data)

            # Convert Json string data to dictionary object
            stock_dict = json.loads(getStockData(input_symbol))

            stock_price = round(float(stock_dict["Global Quote"]['05. price']), 2)

            price_message = "The current price of stock {} is: ${}".format(input_symbol, stock_price)
            print(price_message)
            print("="*60)
            print("Stock Quoutes retreived successfully!")

            with open("japi.out", "a+") as f:
                f.write("{}\n{}\n\n".format(stock_data, price_message))
        except:
            print("Stock {} not found!".format(input_symbol))


if __name__ == '__main__':
    main()
