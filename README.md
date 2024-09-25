# CTIP-Assignment2

# Weather Prediction and Energy Usage Forecasting

This project uses machine learning models to predict next day’s minimum and maximum temperatures (`tmin`, `tmax`) and energy usage based on weather data from multiple cities.

## Installation

To get started, clone this repository and set up your environment:

```bash
git clone https://github.com/yourusername/weather-forecasting.git
cd weather-forecasting
```

### 1. Create a Conda Environment

```bash
conda create -n weather_env python=3.9
conda activate weather_env
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Data Processing

1. Load weather data for cities such as New York, Dubai, Melbourne, and Sydney.
2. Clean the data and handle missing values.
3. Perform **feature engineering**: Calculate features like temperature range (`tmax - tmin`) and wind chill.

```python
combined_weather_data['temp_range'] = combined_weather_data['tmax'] - combined_weather_data['tmin']
combined_weather_data['wind_chill'] = combined_weather_data['tavg'] - (combined_weather_data['wspd'] * 0.7)
```

## Model Training

### Random Forest and Gradient Boosting Models

1. **Training**:
   - Use `RandomForestRegressor` and `GradientBoostingRegressor` to predict next day’s `tmin` and `tmax`.

```python
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

rf_model = RandomForestRegressor(n_estimators=100)
gbr_model_tmin = GradientBoostingRegressor(n_estimators=100)

# Train the models
rf_model.fit(X_train, y_train)
gbr_model_tmin.fit(X_train, y_train_tmin)
```

2. **Prediction**:
   - Use the trained models to predict temperature and energy consumption for the next day.

```python
y_pred = rf_model.predict(X_test)
```

## Using the Model

To use the model for prediction:

1. Load the trained model using `joblib`.
2. Input new weather data to make predictions for the next day’s temperatures or energy usage.

```python
import joblib
rf_model = joblib.load('random_forest_model.pkl')
```

## Results

After training the models, you can compare the actual and predicted temperatures and energy consumption:

```python
results = pd.DataFrame({
    'Actual Tmin': y_test['tmin_next_day'],
    'Predicted Tmin': y_pred[:, 0]
})
print(results.head())
```
