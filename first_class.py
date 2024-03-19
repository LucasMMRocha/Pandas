import pandas as pd

# Creating Data

# df = pd.DataFrame({'Yes': [50, 21], 'No': [13, 1]})

# df = pd.DataFrame({'Bob': ['I liked it', 'It was awful.'], 'Sue': ['Pretty good', 'Bland']})

# df = pd.Series([1, 2, 3, 4, 5])

# df = pd.Series([30, 45, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# print(df)


# Reading data files

# data_review = pd.read_csv("wine_review.csv")

# print(data_review.shape)  # The size of the file

# print(data_review.head())   # First 5 rows

# data_review = pd.read_csv("wine_review.csv", index_col=0)

# print(data_review.head())


# Native accessors

data_review = pd.read_csv("wine_review.csv")

# print(data_review.country)   Here we can specify the name of the column we
#                             want to display

# print(data_review['country'])     We can also do it like a dictionary
# print(data_review['country'][0])    To get a single specific file we just need index it


# Indexing in Pandas

# print(data_review.iloc[0])     Here we are selecting the first row of data in DT

# print(data_review.iloc[:, 0])   Here we are displaying the first column

# print(data_review.iloc[:3, 0])    Here we are going from 0 to 3, but only going until 2

# print(data_review.iloc[1:3, 0])     We can also do it like this

# print(data_review.iloc[[0, 1, 2], 0])     We can also pass as a list

# print(data_review.iloc[-5:])      Here we are getting the last 5


# Label-based selection

# print(data_review.loc[0, 'country'])

# print(data_review.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])


# Manipulating the Index

# print(data_review.set_index("title"))


# Conditional Selection

# print(data_review.country == 'Italy')

# print(data_review.loc[data_review.country == 'Italy'])

# print(data_review.loc[(data_review.country == 'Italy') & (data_review.points >= 90)])

# print(data_review.loc[data_review.country.isin(['Italy', 'France'])])   # This allows you select data that
#                                                                          is in a list of values

# print(data_review.loc[data_review.price.notnull()])     # This allows us to get rid of the values that are null


# Assigning data

# data_review['critic'] = 'everyone'      # Assign a constant value
# print(data_review['critic'])

# data_review['index_backwards'] = range(len(data_review), 0, -1)   # Or with an iterable of values
# print(data_review['index_backwards'])


# Summary Functions

# print(data_review.poits.describe())     # Here the output changes given the data type of the input
#                                       (the output here only makes sense for numerical data)

# print(data_review.taster_name.describe())

# print(data_review.points.mean())        #To see the mean of the points allotted

# print(data_review.taster_name.unique())     # To see a list of unique values

# print(data_review.taster_name.value_counts())  # To see a list of unique values and how
#                                                  often they occur in the dataset


# Maps

# Remeaning the scores the wines received to 0

# review_points_mean = data_review.points.mean()
# print(data_review.points.map(lambda p: p - review_points_mean))


# def remean_points(row):
#     row.points = row.points - review_points_mean
#     return row


# print(data_review.apply(remean_points, axis='columns'))

# print(data_review.head(1))    # Showing that the data in the file didn't change

# Here is a faster way for remeaning our points column
# review_points_mean = data_review.points.mean()
# print(data_review.points - review_points_mean)

# print(data_review.country + " - " + data_review.region_1)     # Combining coutry and region information in the DT
