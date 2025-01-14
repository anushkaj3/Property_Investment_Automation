
import os
import pandas as pd
from extract_data import Extract_Data
from property_visualiser import Property_Visualiser
from property_analysis import Property_Analysis

def main_menu():
	"""
	main menu prints the options for the user to select from

	"""
	print(" ")
	print("Menu")
	print("1) Property Summary")
	print("2) Average Land Size ")
	print("3) Property Value Distribution")
	print("4) Sales Trend")
	print("5) Property for a Target Price ")
	print("6) Exit")

def user():
    #display the menu
    main_menu()
    #Take the users option as input
    print(" ")
    user_option = input("Enter your option: ")
    flag = False
    #check if the option entered is valid
    while(not(user_option.isdigit()) or int(user_option) > 6):
        print(" ")
        print("Please enter a valid number between 1 and 6 from the Menu")
        print(" ")
        main_menu()
        print(" ")
        user_option = input("Enter your option: ")
    user_option = int(user_option)
    return user_option

def main():
	print("Welcome to Property Investment")
	print("We provide you with a range of options to generate quick answers to the most common queries a property investor would have")

	# check if their exists a file in the directory
	check = os.path.isfile('property_information.csv')

	print("In order to perform any operations,you will need to upload your data stored in a csv file.")
	print("Please name the file as property_information.csv")
	print("Please upload the file in the following path",os.getcwd())

	if not check:
		print("Once you have uploaded the file please enter Y")
		check_op = input("Have you uploaded the file?")
		check_op = check_op.upper()

	while True:
		if not check:
			print("Please upload your property data file in the right folder with the right name")
			print("Once you have uploaded the file please enter Y")
			check_op = input("Have you uploaded the file?")
			check_op = check_op.upper()
			check = os.path.isfile('property_information.csv')
		else:
			print("The file has been uploaded sucessfully !")
			break

	print("")
	filepath = 'property_information.csv'
	dataframe_initial = pd.read_csv(filepath)
	# create objects for the classes to be used
	ob = Extract_Data()
	dataframe = ob.extract_property_info(filepath)
	print(" ")
	print("Below you will find a menu with operations you can choose from.")
	print("Please enter the number for the option you would like to select")
	user_option = user()
	pa = Property_Analysis()
	pv = Property_Visualiser()

	while user_option != 6 :
		match user_option:
			case 1 :
				print("You have selected the Property Summary")
				print("To get a summary of all properties in a Suburb , please enter the Suburb name otherwise enter \"all\"")
				# display the available suburbs
				ava_suburb = dataframe['suburb'].unique()
				print("These are the available Suburbs")
				[print(each) for each in ava_suburb]
				suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
				suburb = suburb.lower()
				a_suburb = dataframe.suburb.apply(lambda x: x.lower()).unique()
				# check if suburb is valid
				while suburb not in a_suburb and suburb != "all":
					print("Kindly enter a valid suburb, make sure to check for spelling mistakes")
					suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
					suburb = suburb.lower()

				print("")
				print("The property summary provides a summary of:")
				print("1.Bedrooms")
				print("2.Bathrooms")
				print("3.Praking Spaces")
				print("The following property types are included in this summary")
				property_type = dataframe['property_type'].unique()
				[print(each) for each in property_type]
				print("")
				print("PROPERTY SUMMARY")
				# call the summary method
				pa.suburb_summary(dataframe, suburb)

				user_option = user()
			case 2:
				print("You have selected the Average Land Size")
				print("To get the Average Land Size of all properties in m² in a Suburb , please enter the Suburb name ")
				print("If you would like to get the Average Land size of all the properties in all the Suburbs enter \"all\"")
				ava_suburb = dataframe['suburb'].unique()
				print("These are the available Suburbs")
				[print(each) for each in ava_suburb]
				suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
				suburb = suburb.lower()
				a_suburb = dataframe.suburb.apply(lambda x: x.lower()).unique()
				# check if suburb is valid
				while suburb not in a_suburb and suburb != "all":
					print("Kindly enter a valid suburb, make sure to check for spelling mistakes")
					suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
					suburb = suburb.lower()

				print("")
				print("The Average Land size averages the land size of the following property types :")
				property_type = dataframe['property_type'].unique()
				[print(each) for each in property_type]
				print("")
				print("AVERAGE LAND SIZE in m²")
				# call the average land size method and display the average land size
				print(pa.avg_land_size(dataframe, suburb)," m²")

				user_option = user()

			case 3:
				print("You have selected Property Value Distribution")
				print("Property Value Distribution tells you the number of properties present for a property price in a currency of your choice ")
				print("To get the Property Value Distribution of all properties  in a Suburb , please enter the Suburb name ")
				print("If you would like to get the Avergae Land size of all the properties in all the Suburbs enter \"all\"")
				ava_suburb = dataframe['suburb'].unique()
				print("These are the available Suburbs")
				[print(each) for each in ava_suburb]
				suburb = input("Enter the name of a suburb or \"all\" to get the average land size of all suburbs ")
				suburb = suburb.lower()
				print("")
				print("Select the currency in which you would like to view the property prices")
				print("The following are the available currencies")
				print("AUD,USD,INR,CNY,JPY,HKD,KRW,GBP,EUR,SGD")
				target_currency = input("Enter the Currency of your choice in the format eg - AUD or INR : ")
				target_currency = target_currency.upper()
				print("")
				print(target_currency)
				# call the property value distribution for the target currency and the suburb
				pv.prop_val_distribution(dataframe,suburb,target_currency)

				user_option = user()

			case 4:
				print("You have selected Sale Trend")
				print("Sales Trend tells you the trend in the number of properties sold since the year 2010")
				print("")
				# call the sales trend method
				pv.sales_trend(dataframe)

				user_option = user()
			case 5:
				print("You have selected Property for a Target Price")
				print("Property for a Target Price tells you if a property exists for the target price of your choice")
				print("To check if a property of your Target price exists in a Suburb , please enter the Suburb name ")

				ava_suburb = dataframe['suburb'].unique()
				print("These are the available Suburbs")
				[print(each) for each in ava_suburb]
				suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
				suburb = suburb.lower()
				a_suburb = dataframe.suburb.apply(lambda x: x.lower()).unique()
				# check if suburb is valid
				while suburb not in a_suburb and suburb != "all":
					print("Kindly enter a valid suburb, make sure to check for spelling mistakes")
					suburb = input("Enter the name of a suburb or \"all\" to get a summary of all suburbs ")
					suburb = suburb.lower()
				print("")
				target_price= input("Enter the target Price")
				# check if target price is a number
				while not target_price.isdigit():
					print("Enter a valid numeric value for the target Price")
					target_price = input("Enter the target Price in AUD:")
				target_price = int(target_price)
				print("")
				output = pa.locate_price(target_price,dataframe,suburb)
				if output :
					print(f"Target price - {target_price}, is found in the Suburb {suburb}")
				else:
					print(f"Target price - {target_price}, is  not found in the Suburb {suburb}")

				user_option = user()


if __name__ == "__main__":
	main()



# dataframe=""
# ab = Extract_Data()
# file_path = "property_information.csv"
#dataframe = ab.extract_property_info(file_path)
# print(ab.extract_property_info(file_path))
#this should return the entire data frame
#                id badge   suburb  ... auction_date  available_date  sold_date
# 0       141922512  Sold  Clayton  ...          NaN             NaN   3/4/2023
# 1       141599568  Sold  Clayton  ...          NaN             NaN   3/4/2023
# 2       141574624  Sold  Clayton  ...          NaN             NaN   1/4/2023
# 3       141840188  Sold  Clayton  ...          NaN             NaN  29/3/2023
# 4       141462600  Sold  Clayton  ...          NaN             NaN  29/3/2023
# ...           ...   ...      ...  ...          ...             ...        ...
# 118766  104338089  Sold  Burwood  ...          NaN             NaN        NaN
# 118767    2595654  Sold  Burwood  ...          NaN             NaN        NaN
# 118768  117914751  Sold  Burwood  ...          NaN             NaN        NaN
# 118769  117081183  Sold  Burwood  ...          NaN             NaN        NaN
# 118770  119955165  Sold  Burwood  ...          NaN             NaN        NaN
#
# print(ab.currency_exchange((ab.extract_property_info(file_path)),56.50))
#this should return a numpy array- [54522500. 22882500. 49776500. ... 42827000. 37855000. 29425200.]

#
# ob = Property_Analysis()
# ob.suburb_summary(dataframe,'all')
# output
# Property Summary for all Suburbs
#                      bedrooms  bathrooms  parking_spaces
# Mean                 3.232831   1.769863        1.809263
# Standard Deviation   1.048621   0.793599        2.574261
# Minimum              0.000000   0.000000        0.000000
# Median               3.000000   2.000000        2.000000
# Maximum             30.000000  65.000000      819.000000
# print(ob.avg_land_size(dataframe,'all'))
#output
# 650.4213917367882
# print(ob.locate_price(965060,dataframe,'clayton'))
#output
# False

# ab = Property_Visualiser()
# ab.sales_trend(dataframe)
