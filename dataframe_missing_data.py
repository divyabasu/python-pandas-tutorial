import pandas as pd

# handle missing records and data
df = pd.read_excel("weather_details.xlsx", parse_dates=["day"])
df.set_index("day", inplace=True)

df2 = df.fillna(0)
# print(df2)

df3 = df.fillna({
    'temperature' : 0,
    'windSpeed' : 0,
    'event' : "No event"
})

# print(df3)

# carry forward previous days value
# df4 = df.fillna(method="ffill")
# limit number of copies
df4 = df.fillna(method="ffill", limit=1)
# copy next days value
# df4 = df.fillna(method="bfill")
# copy data vertically
# df4 = df.fillna(method="bfill", axis="columns")
# print(df4)


# interpolate values for missing data
new_df = df.interpolate()
# to get better results
# new_df = df.interpolate(method="time")
# print(new_df)

# drop all records with na value
# dropped_df = df.dropna()
# drop only if all values are missing
# dropped_df = df.dropna(how="all")
# atleast one non NA values, keep the row
dropped_df = df.dropna(thresh=1)
# print(dropped_df)

# Insert missing dates
dt = pd.date_range("2017-01-01", "2017-01-06")
idx = pd.DatetimeIndex(dt)
df_complete = df.reindex(idx)
print(df_complete)