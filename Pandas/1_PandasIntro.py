import pandas as pd

print(pd.__version__)

# Pandas Series with Python List

lst = [1, 2, 3, 4, 5]
series = pd.Series(lst)

print(series)
print(type(series))

# empty Series
empty = pd.Series([])
print(empty)

# define own indexes in a list
a = pd.Series(['p', 'q', 'r', 's', 't'], index = [11, 12, 13, 14, 15])
print(a)

# Giving name to the series
b = pd.Series(['p', 'q', 'r', 's', 't'], index = [11, 12, 13, 14, 15], name='alphabets')
print(b)

# creating series using a scalar value
scalar_series = pd.Series(0.5)
print(scalar_series)

# increase the quantity of scalar values
scalar_series1 = pd.Series(0.5, index=[1, 2, 3])
print(scalar_series1)


# Pandas Series with Python Dictionary

dict_series = pd.Series({'p':1, 'q':2, 'r':3, 't':4})
print(dict_series)

# printing dict_series at 0th index
print(dict_series[0])

# printing dict_series from 0th to 3rd index
print(dict_series[0:3])

# maxm of dict series
print(max(dict_series))


# Combining dictionary and list into a series
dict_list_series = pd.Series({'p':[1,5,6], 'q':[2,6,7], 'r':[3,4,5]})
print(dict_list_series)
