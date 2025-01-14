
import pandas as pd
import numpy as np

class Extract_Data:
    """
    Extract_Data class is used to Extract data from the csv file
    and any other operations that involve getting data from the data frame.

    --Attributes--
    dataframe : the dataframe obtained from the csv file

    --Methods--
    extract_property_info():
        Extracts the data from the csv using the file path as an input parameter
        and saves it as a dataframe
    currency_exchange():
        Converts the price values in the dataframe to based on the exchange rate

    """
    def __int__(self,dataframe=""):
        # storing a copy of the dataframe for an instance
        self.dataframe = dataframe

    def extract_property_info(self, file_path):
        # creating a dataframe
        dataframe = pd.read_csv(file_path)
        return(dataframe)
    def currency_exchange(self,dataframe,exchange_rate):
        # storing the price from the dataframe
        pricein_aud = dataframe["price"]
        # dropping empty or null values - cleaning the data
        pricein_aud = pricein_aud.dropna()
        # converting to the required currency based on exchange rate
        pricein_currency = pricein_aud * exchange_rate
        # generating a numpy array
        property_price = np.array(pricein_currency)
        return property_price






