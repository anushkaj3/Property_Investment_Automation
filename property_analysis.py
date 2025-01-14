

class Property_Analysis:
    """
       Property_Analysis class is used to perform analysis on the data
       --Attributes--
       dataframe : the dataframe obtained from the csv file

       --Methods--
       suburb_summary():
          Provides a summary of the suburb based on the bedrooms , bathrooms and parking
          spaces for the given suburb or all suburbs.
       avg_land_size():
           Calculates the average land size of the properties and returns the average land size in m²
       convert_unit():
        This method is used to convert the land units in ha to m²
       locate_price():
       This method locates the target price in the prices of properties in a given suburb

"""
    def __int__(self,dataframe):
        # storing the dataframe
        self.dataframe = dataframe

    def suburb_summary(self,dataframe,suburb):
        # if suburb is all
        if suburb == 'all':
            # use describe to get the summary of the property
            property_summary = dataframe[['bedrooms','bathrooms','parking_spaces']].describe()
            # selecting the rows of the describe output to print
            row_index = [1,2,3,5,7]
            # setting row labels for better understanding
            row_index_label = {
                                'mean' : 'Mean',
                                'std'  :  'Standard Deviation',
                                'min'  : 'Minimum',
                                '50%'  : 'Median',
                                'max'  : 'Maximum'
            }
            property_summary = property_summary .rename(index=row_index_label)
            print("Property Summary for all Suburbs")
            print(property_summary.iloc[row_index])
        else:
            # if the user has selected a paticular suburb
            if suburb in dataframe['suburb'].str.lower().unique():
                # if suburb is in the dataframe
                suburb_summary = dataframe[dataframe['suburb'].str.lower() == suburb]
                property_summary =  suburb_summary[['bedrooms','bathrooms','parking_spaces']].dropna().describe()
                # selecting the rows from the describe output
                row_index = [1,2,3,5,7]
                # Setting the rwo labels for better understanding
                row_index_label = {
                                'mean' : 'Mean',
                                'std'  :  'Standard Deviation',
                                'min'  : 'Minimum',
                                '50%'  : 'Median',
                                'max'  : 'Maximum'}
                property_summary = property_summary.rename(index=row_index_label)
                print("Suburb:",suburb)
                print(property_summary.iloc[row_index])
            else:
                # give an error is the suburb is not in the lisr
                print("Suburb not in the list")


    def  avg_land_size(self,dataframe, suburb):
        # if the user selects all suburbs
        if suburb == 'all':
            # obtain the land size unit and convert it to  m²
            land_size_unit = dataframe['land_size_unit'].apply(self.convert_unit)
            # drop any emtpy or null values
            valid_unit = land_size_unit.dropna()
            land_size = dataframe['land_size']
            # drop any null values
            land_size = land_size.dropna()
            # drp land size values with land_size as -1
            land_size = land_size[~(land_size == -1)]
            total_land_size = land_size * valid_unit
            #return the average
            return total_land_size.mean()
        else :
            if suburb in dataframe['suburb'].str.lower().unique():
                # if the suburb entered by user is in the suburb list from the csv
                suburb_s= dataframe[dataframe['suburb'].str.lower() == suburb]
                # convert those in ha to the right unit
                land_size_unit = suburb_s['land_size_unit'].apply(self.convert_unit)
                # drop any emtpy land_size unit values
                valid_unit = land_size_unit.dropna()
                land_size = suburb_s['land_size']
                land_size = land_size.dropna()
                land_size = land_size[~(land_size == -1)]
                # calculate the land size unit after conversion
                total_land_size = land_size * valid_unit

                return total_land_size.mean()
            else:
                return None


    def convert_unit(self,land_unit):
        # create a dictionary with all the land size units
        land_unit_conv={
            'm²' : 1,
            'ha' : 10000
        }
        # check if the units from the csv is in the dictionary
        if land_unit in land_unit_conv:
            return land_unit_conv[land_unit]
        return None

    def locate_price(self,target_price, data,target_suburb):
        # if the target suburb is in the suburb list from the csv file
        if target_suburb in data['suburb'].str.lower().unique():
            t_suburb = data[data['suburb'].str.lower() == target_suburb]

            # covert the suburb price to a list
            suburb_price = t_suburb['price'].dropna().tolist()

        # sort the list using insertion sort
            for i in range(1,len(suburb_price)):
                # get the current item to be positioned
                item = suburb_price[i]
                pos = i-1
                # find the correct position
                while pos >= 0 and suburb_price[pos] < item:
                    # shift items that are smaller to the right
                    suburb_price[pos+1] = suburb_price[pos]
                    pos -= 1
                suburb_price[pos+1] = item

        # perform binary search on the sorted list to search for the target price
            return self.binary_search(suburb_price,target_price,0,len(suburb_price)-1)

    def binary_search(self,suburb_price,target_price,low,high):

        if low <= high:
            mid = (low+high)//2
            # the base condition when the target price is found
            if suburb_price[mid] == target_price:
                return True
            # if target price is not found repeatedly divide the list
            elif suburb_price[mid] < target_price:
                return self.binary_search(suburb_price,target_price,low,mid-1)
            else:
                return self.binary_search(suburb_price,target_price,mid+1,high)
        return False




