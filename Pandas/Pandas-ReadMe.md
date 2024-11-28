# Pandas

Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, <br/>
built on top of the Python programming language.

## Pandas Syntax
````
import pandas as pd
pd.__version__
````

## Pandas Series with Python Lists
````
lst = [1, 2, 3, 4, 5]
series = pd.Series(lst)
````

### Pandas empty series
````
empty = pd.Series([])
````

### Definig own indexes and names to the series
````
# define own indexes in a list
a = pd.Series(['p', 'q', 'r', 's', 't'], index = [11, 12, 13, 14, 15], name='alphabets')
print(a)
````


### Creating Pandas series using scalar values
````
scalar_series1 = pd.Series(0.5, index=[1, 2, 3])
````


## Pandas Series with Python Dictionary
````
dict_series = pd.Series({'p':1, 'q':2, 'r':3, 't':4})
````

## Pandas as Dataframe
Dataframe - It is a collection of data that contains rows, and columns (i.e.  2 dimensional data structure).

### Examples-----
````
import pandas as pd
df = pd.DataFrame()
````

1. DataFrame as list
````
import pandas as pd
df = pd.DataFrame([1,2,3,4,5])
lst = [14,'a',5,'g']
df1 = pd.DataFrame(lst)
````

2. DataFrame as Dictionary
````
import pandas as pd
a = [{'a':5, 'b':7, 'c':9, 'd':2},
     {'a':4, 'b':8, 'c':19, 'd':12}]        # Dictionary Keys represents Column names
df = pd.DataFrame(a)
````

3. DataFrame as combination of Dictionary and Pandas Series
````
import pandas as pd
b = {'RollNo.': pd.Series([1,2,3,4,5]),
     'Maths': pd.Series([67,89,23,90,56]),
     'Physics': pd.Series([12,98,44,90,78])}

df = pd.DataFrame(b)
df
````

### Reading data from CSV File using Pandas DataFrame

Example:
````
df2 = pd.read_csv('<Dataset-location>')
df2
````

# Pandas DataFrame functions

1. Returning first 5 rows of the data
````
df2.head()
````

2. Returning last 5 rows of the data
````
df2.tail()
````

3. Returning first 7 rows of the data
````
df2.head(7)
````

4. Returning last 7 rows of the data
````
df2.tail(7)
````

5. Shape of DataFrame
````
df2.shape
````

6. Size of DataFrame
````
df2.size
````

7. Describe details of DataFrame Data
````
df2.describe
````

### Handling Missing values and Null values in a dataset

1. Dropping Rows with NaN values
````
df2.dropna()  # default axis = 0
df2.dropna(axis=1) 
df.dropna(how='all')    # if all row values is null then remove that row
df.dropna(inplace=True)         # droping NaN values in inplace dataframe
````


2. Calculating the sum of Null Values in each column
````
df2.isnull().sum()
````

3. Filling the Null Values
````
df2.fillna(0)                                       # fill NaN with 0
df2.fillna({'Physics': 'none', 'Chemistry':0, 'Maths':30})  # fill NaN column wise value

df2.fillna(method = 'ffill')      # fillling values from previous rows
df2.fillna(method = 'ffill', axis=1)      # fillling values from forward previous column
df2.fillna(method = 'bfill', inplace=True)      # inplace will update the original dataframe and method is backword fill

df_sample['Physics'].fillna(value=df_sample['Physics'].mean())   # filling NaN with mean value of column
````