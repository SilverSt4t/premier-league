import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()
    le = LabelEncoder()
    df['home_team_encoded'] = le.fit_transform(df['home_team'])
    df['away_team_encoded'] = le.transform(df['away_team'])
    df['result'] = df.apply(lambda row: 'H' if row['home_score'] > row['away_score'] else ('A' if row['home_score'] < row['away_score'] else 'D'), axis=1)
    df['result_encoded'] = le.fit_transform(df['result'])
    return df, le

def train_model(df):
    X = df[['home_team_encoded', 'away_team_encoded']]
    y = df['result_encoded']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def predict_result(model, home_team, away_team, le):
    home_encoded = le.transform([home_team])[0]
    away_encoded = le.transform([away_team])[0]
    prediction = model.predict([[home_encoded, away_encoded]])[0]
    result_label = le.inverse_transform([prediction])[0]
    return result_label
