import pandas as pd

def preprocess_data(data):
    data = pd.get_dummies(data, columns=["Department"], drop_first=True)

    X = data.drop("Performance", axis=1)
    y = data["Performance"]

    y = y.map({"Low": 0, "Medium": 1, "High": 2})

    return X, y