import pmdarima as pm
import joblib
import pandas as pd
import os

input_file = os.environ.get('INPUT_PATH', '/data/data.csv')
output_file = os.environ.get('OUTPUT_PATH', 'model.pickle')

try:
    data = pd.read_csv(input_file, header=0)
    train = data["water_height"].values.tolist()

    sxmodel = pm.auto_arima(train,
        start_p=0, start_q=0,
        test='adf',
        max_p=2, max_q=2,
        seasonal=False,
        d=0, trace=False,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True)

    joblib.dump(sxmodel, output_file)
    print("Successfully train model!")

except Exception as e:
    print("Error occured {}".format(e))
