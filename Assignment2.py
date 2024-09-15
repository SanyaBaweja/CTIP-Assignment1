import pandas as pd
weather = pd.read_csv("aus_weather_data/WeatherTrainingData.csv", index_col="row ID")
weather
null_pct = weather.apply(pd.isnull).sum()/weather.shape[0]
null_pct
weather.apply(pd.isnull).sum()
valid_columns = weather.columns[null_pct < 0.05]
valid_columns
weather = weather[valid_columns].copy()
weather
weather = weather.ffill()
weather.apply(pd.isnull).sum()
weather.dtypes
weather.Location.value_counts().sort_index()
