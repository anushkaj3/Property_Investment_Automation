

import numpy as np
from extract_data import Extract_Data
import matplotlib.pyplot as plt
import os

class Property_Visualiser(Extract_Data):
    """
         Property_Visualiser class is used to generate visualization elements
           --Attributes--
           dataframe : the dataframe obtained from the csv file

           --Methods--
           prop_val_distribution():
              Generates a histogram based on the property price
           sales_trend():
              Generates a line graph of the number of sales per year


    """
    def __int__(self,dataframe=""):
        self.dataframe = dataframe

    def prop_val_distribution(self,dataframe,suburb,target_currency="AUD"):
        # create a dictionary with the currency and the exchange rate
        currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY":
            4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92, "GBP": 0.51,
                         "EUR": 0.60, "SGD": 0.88}
        target_currency = target_currency.upper()
        # check if target currency is in the dictionary
        if target_currency not in currency_dict:
            print("Target Currency is not valid. Generating histogram in AUD")
            target_currency = "AUD"
            # get exchange rate for the currency
            exchange_rate = currency_dict[target_currency]
        else:
            exchange_rate = currency_dict[target_currency]
        if suburb not in dataframe['suburb'].str.lower().unique() and suburb != 'all':
            # if the entered suburb is not valid generate a histogram for all suburbs
            print("The entered Suburb does not exist in the data , hence the histogram will be generated for all suburbs")
            suburb = "all"
        if suburb == "all":
            # call currency_exchange to get the arrapy of converted prices
            property_value = super().currency_exchange( dataframe, exchange_rate)
            property_value = property_value[~np.isnan(property_value)]
        else:
            dataframe_suburb = dataframe[dataframe['suburb'].str.lower() == suburb]
            property_value = super().currency_exchange(dataframe_suburb, exchange_rate)
            property_value = property_value[~np.isnan(property_value)]
        # divide values by 1000000 to represent the values on the scale in terms of 10 lakhs
        property_value = property_value/1000000
        plt.figure(figsize=(10,6))
        plt.hist(property_value,bins = 50 )
        plt.title(f'Property Value Distribution in {suburb} ({target_currency}) ')
        plt.xlabel(f'Property Price in ({target_currency}) (unit - 10,000 lakhs)')
        plt.ylabel ('No. of Properties')

        if suburb == "all":
            plt.savefig('property_value_distribution.png')
            print(f"The Property Value Distribution for all suburbs in the currency {target_currency} is saved as an image at the following path.")
            print(os.getcwd())
        else:
            plt.savefig('property_value_distribution.png')
            print(f"The Property Value Distribution for the suburb {suburb} in the currency {target_currency} is saved as an image at the following path.")
            print(os.getcwd())


    def sales_trend(self,dataframe):
        # get the sale_year
        sale_year = dataframe['sold_date'].str.split('/').str.get(2)
        # drop any emtpy values
        sale_year = sale_year.dropna()
        # get the no of properties sold in each year
        sale_year = sale_year.value_counts().rename_axis('Year').reset_index(name='Counts')
        # sort the list using insertion sort
        for i in range(1,len(sale_year)):
            cur_element = sale_year.loc[i].copy()
            pos = i-1
            while pos >= 0 and cur_element['Year'] < sale_year.loc[pos]['Year']:
                sale_year.loc[pos+1] = sale_year.loc[pos].copy()
                pos -= 1
            sale_year.loc[pos+1] = cur_element


        # plot the line graph
        plt.figure(figsize=(10, 6))
        plt.plot(sale_year['Year'],sale_year['Counts'],linestyle='-',color='b')
        plt.title('Property Sales Trend by Year')
        plt.xlabel('Year')
        plt.ylabel('No of Properties Sold')
        plt.grid(True,linestyle='--',alpha=0.6)

        plt.savefig('sales_trend.png')
        print("The Sales Trend for all suburb is saved as an image at the following path.")
        print(os.getcwd())





