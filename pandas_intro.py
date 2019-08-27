import pandas as pd

df = pd.read_csv("weather_data_nyc_2016.csv")
# print(df)

"""
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

df = pd.DataFrame(weather_data)
"""

# Dimension of the dataframe. returns a tuple of rows and columns
rows, columns = df.shape
print (df.shape)

# To print some initial rows. use df.head(n) to specify the first n number of rows to fetch.
df.head()

# To print some last rows. use df.tail(n) to specify the last n number of rows to fetch.
df.tail()