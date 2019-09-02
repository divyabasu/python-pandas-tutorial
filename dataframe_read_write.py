import pandas as pd
from openpyxl import Workbook

df = pd.read_csv("weather_data_nyc_2016.csv")
# if there are additional rows to skip
# df1 = pd.read_csv("weather_data_nyc_2016.csv", skiprows=1)
# df1 = pd.read_csv("weather_data_nyc_2016.csv", header=1)

# if no headers are present
# numeric column names
# df1 = pd.read_csv("weather_data_nyc_2016.csv", header=None)
# supply names for headers
# df1 = pd.read_csv("weather_data_nyc_2016.csv", header=None, names=["day", "temperature", "windspeed", "event"])

# read only first 3 rows from the dataframes
# df2 = pd.read_csv("weather_data_nyc_2016.csv", nrows=3)

# read empty values, provide the values to ne converted to NaN
# df2 = pd.read_csv("weather_data_nyc_2016.csv", na_values=["not available", "n.a"])

# Supply a dictionary to selectively convert to NaN
# df2 = pd.read_csv("weather_data_nyc_2016.csv", na_values={
# #     'days' : ["not available", "n.a"],
# #     'temperature' : ["not available", "n.a", -1]
# # })

# Writing to CSV
# df.to_csv("new.csv")
# write particular columns
# df.to_csv("new.csv", columns=["days", "temperature"])
# do not write headers
# df.to_csv("new.csv", columns=["days", "temperature"], header=False)
# if no index is required
# df.to_csv('new.csv', index=False)


# writing to Excel
revenue_details = {
    'tickers' : ['GOOGL', 'WMT', 'MSFT', 'RIL', 'TATA'],
    'eps' : [27.82, 4.61, -1, 'not available', 5.6],
    'revenue' : [87, 484, 85, 50, -1],
    'price' : [845, 65, 64, 1023, 'n.a'],
    'people' : ['larry page', 'n.a', 'bill gates', 'mukesh ambani', 'ratan tata']
}

revenue_df = pd.DataFrame(revenue_details)
revenue_df.to_excel("revenue_details.xlsx", sheet_name="sheet1")
# start writing from an offset
# revenue_df.to_excel("revenue_details.xlsx", sheet_name="sheet1", startcol=1, startrow= 2)


def convert_people_cell(cell):
    if cell=="n.a":
        return "sam walton"
    return cell


def convert_eps_cell(cell):
    if cell == "not available":
        return None
    return cell


revenue_df1 = pd.read_excel("revenue_details.xlsx", "sheet1", converters={
    'people' : convert_people_cell,
    'eps' : convert_eps_cell
})

# write 2 data frmaes to two sheets in exxcel

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windSpeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

weather_df = pd.DataFrame(weather_data)

with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    revenue_df.to_excel(writer, sheet_name="revenue")
    weather_df.to_excel(writer, sheet_name="weather")