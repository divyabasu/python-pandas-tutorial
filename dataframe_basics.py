import pandas as pd

# Make dataframe, option 1
# df = pd.read_csv("weather_data_nyc_2016.csv")
# print(df.head(1))

# Make dataframe option 2
# df = pd.read_excel("weather_data_nyc_2016.xlsx", "sheet1")

# Made dataframe, option3 from python dictionary
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windSpeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

df1 = pd.DataFrame(weather_data)
print(df1.head(1))

# Make dataframe, option 4
weather_data_new = {
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017', 35,7,'Sunny'),
    ('1/3/2017', 28,2,'Snow'),
    ('1/4/2017', 32, 5, 'Snow')
}

df_new = pd.DataFrame(weather_data_new, columns=["day", "temperature", "windSpeed", "event"])

# Made dataframe, option4 from list of python dictionary
weather_data_last = [
    {'day' : '1/1/2017', 'temperature' : '32', 'windSpeed' : '6', 'event' : 'Rain'}
]

df2 = pd.DataFrame(weather_data_last)
print(df2.head())

# more informations at IO Tools Pandas