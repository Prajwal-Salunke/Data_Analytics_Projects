          # Data Analysis of Diwali-Sales with Visualisation

''' > Libraries Required < '''
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns

''' *Note :- '\n' is deliberately used to precisely read the output results on new lines for convinient view, can delete if using other IDEs '''

# import csv file to read the data
df = pd.read_csv('DiwaliSalesDataset.csv', encoding='unicode_escape')
print('\n(Rows, Columns) \n', df.shape)
print(df.head())
print(df.info()) # Overview of dataset

nullCount = df.isnull().sum()
print('\n> Count of Null Values :-\n', nullCount)

''' -- Data Cleaning -- '''

delClm = df.drop(['Status', 'unnamed1'], axis=1, inplace=True) # Deleting 2 columns as NO data is available for any instance

# NOTE:- Instead of removing complete row, we assumed '0' in empty cells of Amount Column to accurately calculate the attributes(Mean,Varience) of other features
df['Amount'] = df['Amount'].fillna(0) # replacing with '0' to blank cells ; otherwise can delete the same rows
print('\n> Validating Null Values :-\n', df.isnull().sum())

# Change the DataTypes
amntDtype = df.Amount.dtypes
print('\n> Current Data-type of Amount Column:- ', amntDtype)

df.Amount = df.Amount.astype('int') # type Conversion
print('> NEW Data-type of Amount :- ', df.Amount.dtypes)

# Rename Columns
df.rename(columns={'Age Group': 'Age_Group'}, inplace=True) # df['Age_Group'] = df['Age Group']
print('\n>Columns after Re-naming :- ', df.columns)

# Summary of features
summary = df[['Age', 'Marital_Status', 'Orders', 'Amount']].describe()
print('\n> Summarised Data:- \n', summary)

''' -- EDA -- '''

# Gender & Marriage-wise
genderPlt = sns.countplot(data=df, x='Gender')
labels = [genderPlt.bar_label(bars) for bars in genderPlt.containers] # labeling counts on bars
plt.xticks(['F', 'M'], ['Female', 'Male']) # Edit X-axis ticks
plt.ylabel('Total Count of Orders') # Edit Y-axis label
plt.show()

genderSales = df.groupby(['Gender', 'Marital_Status'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print('\n> Total spending w.r.t. gender :-\n', genderSales)
sns.barplot(x='Gender', y='Amount', data=genderSales, hue='Marital_Status')
plt.yscale('log')
plt.ylabel('Total Spending Amount')
plt.xticks(['F', 'M'], ['Female', 'Male'])
plt.show()

print('\n> From the charts, Married-Women are more likely to purchase products with High amount of spending w.r.t Male')

# Age-wise
agePlt = sns.countplot(data=df, x='Age_Group', hue='Gender')
ageLabels = [agePlt.bar_label(bars) for bars in agePlt.containers]
plt.ylabel('Total Count of Orders')
plt.show()

ageSales = df.groupby(['Age_Group'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=ageSales, x='Age_Group', y='Amount')
plt.ylabel('Total Amount of Orders')
plt.yscale('log')
plt.show()
print('\n> From the charts, Ages from 26 to 35 years Females purchase more products with High spending.')

# State-wise
statePlt = sns.countplot(data=df, x='State', order=df['State'].value_counts().iloc[:10].index) #.iloc[:10]--> to view first 10bars only on chart 
plt.xticks(rotation=90) # Rotating ticks foe better visualisation
# stateLabels = [statePlt.bar_label(bars) for bars in statePlt.containers]
plt.ylabel('Total Count of Orders')
plt.show()

stateSales = df.groupby(['State'], as_index=False)['Amount'].sum()
sns.barplot(data=stateSales, x='State', y='Amount',order=df['State'].value_counts().iloc[:10].index)
plt.xticks(rotation=90)
plt.ylabel('Total Amount of Orders')
plt.show()
print(f'\n> The states "Uttar Pradesh, Maharashtra, Karnataka" have more number of Orders with high spending respectively.')

# Occupation-wise
occuPlt = sns.countplot(data=df, x='Occupation', order=df['Occupation'].value_counts().iloc[:10].index) 
plt.xticks(rotation=90)
occuLabels = [occuPlt.bar_label(bars) for bars in occuPlt.containers]
plt.ylabel('Total Count of Orders')
plt.show()

occuSales = df.groupby(['Occupation'], as_index=False)['Amount'].sum()
sns.barplot(data=occuSales, x='Occupation', y='Amount',order=df['Occupation'].value_counts().iloc[:10].index)
plt.xticks(rotation=90)
plt.ylabel('Total Amount of Orders')
plt.show()
print("\n> Highest number of Orders received with maximum amount of purchase can be figured out through charts are "
 "from IT Sector, Healthcare, Aviation & Banking field working professionals.")

# Most Selling Product Category
prodPlt = sns.countplot(data=df, x='Product_Category', order=df['Product_Category'].value_counts().iloc[:10].index)
plt.xticks(rotation=90)
prodLabels = [prodPlt.bar_label(bars) for bars in prodPlt.containers]
plt.ylabel('Total Count of Orders')
plt.show()
print(f'\n> TOP 3 most Selling items are from "Clothing & Apparel", "Food" and "Electronics & Gadgets".')

print("\n> Overall Conclusion from all the charts and analysed data is Married Women of age group of 26-35 years from "
 "Uttar Pradesh, Maharashtra and Karnataka working in IT Sector, Healthcare, Aviation & Banking sectors are most "
 "likely to buy products from Clothing & Apparel, Food and Electronics catagory")
