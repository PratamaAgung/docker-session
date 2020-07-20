import pandas as pd
from fbprophet import Prophet
import datetime
import sys

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")

future_predict = int(sys.argv[1]) 

data = pd.read_csv('data/train.csv', header=0)
data_train = data[['date', 'water_height']]
data_train['ds'] = data.date.apply(lambda x: parse_date(x))
data_train = data_train.rename(columns={
    'water_height': 'y'
})

model = Prophet(
    yearly_seasonality=False,
    weekly_seasonality=False, 
    daily_seasonality=False,
    changepoint_prior_scale=0.25, 
    growth='linear')

model.fit(data_train)

future = model.make_future_dataframe(periods=future_predict)
forecast = model.predict(future)

forecast.to_csv('data/prediction.csv', index=False)