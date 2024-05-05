              # Big-Data Analysis for Weather Dataset

''' > Libraries Required < '''
import pandas as pd

''' *Note :- '\n' is deliberately used to precisely read the output results on new lines for convinient view, can delete if using other IDEs '''

# Read the data from Dataset file
dataset = pd.read_csv(r"C:\Users\2230304\PycharmProjects\Data Analytics Proj\WeatherDataSet.csv")
 # use of 'r' in above line is to remove the unicode(unicodespace) error or else
 # we can use "\\" everywhere in path location
pd.set_option('display.max_columns', None) # to view all the columns on terminal of pyCharm IDE , default--> few initial and last columns appear on o/p terminal
print('> Complete Dataset :- \n' ,dataset)


''' > Walkthrough to basic functions used in pandas frameworks < ''' 

# to view first 5 (default) rows of dataset or else mention no.of rows in ()
print('\n> Data with first 10 Rows :-\n', dataset.head(10))

# shape --> (rows,column) as o/p
print('\n(Rows, Columns) \n', dataset.shape)

# index--> label--> marking on each row ex:- 1.Name, 2.Sname --> 1&2 are index
print('\n',dataset.index)

# show column names present in dataset
print('\n> Available Columns in the dataset:- ',dataset.columns)

# get datatypes of each column and can be analysed to change dtype if neccessory
print('\n> The data-type of each column :- \n', dataset.dtypes)

# get only unique values of 'a particular' column(avoid duplicates)
print('\n> Weather conditions in the dataset:- ', dataset['Weather'].unique())

# get number of unique values in a column
print('\n> Total unique values :-\n', dataset.nunique())

# Non-Null values
print('\n> Count of Non-Null values::-\n', dataset.count()) # gives total count nos. of NON-NULL values , both for each column / whole dataset

# Unique values for Weather column
print('\n> Total unique values in Weather Column:-\n', dataset['Weather'].value_counts()) # shows all unique values with count nos., one column of dataset ONLY ; o\p--> snow - 53 , rain - 33(appears 33times in the column)


# Rename 'Weather' column to "Weather Condition"
renameClm = dataset.rename(columns={"Weather" : "Weather Condition"}) #use " ,inplace=Ture" for permanent changes
print('\n> Dataset after Renamed Weather Column:\n', renameClm)

# Overview the Data
print('\n> Overview of data:-\n', dataset.info) # shows overview of dataset --> rows*col , contained datatypes, memory usage, all columns name


''' > Analysis of Data < '''

 # Validate the NULL values
countNull = dataset.isnull().sum()
print('\n> Validating Null Values :-\n', countNull)

 # Extract all unique values for Wind Speed
uniqueSpeeds = dataset["Wind Speed_km/h"].unique()
print(f'\n> Available speeds:- {uniqueSpeeds}, Total ={uniqueSpeeds.size}')

 # A Clear Weather
clearWeather =dataset[dataset.Weather == "Clear"]
print('\n> Features when Weather is Clear:- \n', clearWeather)
#Way-2 (grouping)-->dataset.Weather.groupby('Weather').get_group("Clear")

 # Wind Speed with exactly 4km/Hr
_4kmph = dataset[dataset["Wind Speed_km/h"] == 4] #using filter method
print('\n> Data with a constant wind speed of 4km/hr :- \n', _4kmph)

 # Mean for Visibility
meanVis = dataset.Visibility_km.mean()
print(f'\n> Mean value for \'Visibility\' :- {meanVis} km')

 # Pressure with Standard Deviation
stdDevPress = dataset.Press_kPa.std()
print(f'\n> Pressure with Standard Deviation of {stdDevPress}')

 # Varience of Humidity
humidVar = dataset["Rel Hum_%"].var()
print(f"\n> Variance of Relative Humidity found to be {humidVar}")

 # Details When snow was occured
snowed = dataset[dataset.Weather.str.contains('Snow')] # this covers all the data when snow occurred in combine climate conditions as well --> Snow Shower, Snow Fog,etc.
print(f'\n> In all Snowy conditions, the instances are as follows :- \n {snowed}')

 # When wind speed > 24 km/h and Visibility=25
finalRslt = dataset[(dataset['Wind Speed_km/h'] > 24) & (dataset['Visibility_km'] == 25)]
print("\n> Filtered instances when wind speed > 24 km/h and Visibility is 25km \n", finalRslt)

 # Clear Weather or Visibility above 40
visWeather = dataset[(dataset.Weather == 'Clear') | (dataset.Visibility_km >= 40)]
pd.set_option('display.max_columns', None)
print("\n> With Clear Weather or above 40km visibility the results are :- \n", visWeather)

 # Clear Weather with Rel.Humidity above 50deg OR Visibility above 40
clrHumidVis = dataset[((dataset.Weather == 'Clear') & (dataset['Rel Hum_%'] > 50) )| (dataset.Visibility_km > 40)]
pd.set_option('display.max_columns', None)
print("\n> Result below shows the data where either Weather condition is Clear with Relative Humidity more than 50 Degrees OR Visibility is above 40Km\n", clrHumidVis)
