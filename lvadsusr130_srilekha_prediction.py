# -*- coding: utf-8 -*-
"""Lvadsusr130_srilekha_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11_ylAG9QUtxvQAicT137mSH-FzGpWl3T
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
df1 = pd.read_csv('Fare prediction.csv')
le= LabelEncoder()
df1['key'] = le.fit_transform(df1['key'])
df1['pickup_datetime'] = le.fit_transform(df1['pickup_datetime'])
imputer = SimpleImputer(strategy='median')
numerical_columns = ['key','pickup_datetime','fare_amount','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count']
df1[numerical_columns] = imputer.fit_transform(df1[numerical_columns])

print(df1.describe())
m = df1.drop(['key'], axis=1)
n = df1['fare_amount']
m_train, m_test, n_train, n_test = train_test_split(m, n, test_size=0.2, random_state=44)

scaler = StandardScaler()
m_train_scaled = scaler.fit_transform(m_train)
m_test_scaled = scaler.transform(m_test)

regress_model = LinearRegression()
regress_model.fit(m_train_scaled, n_train)

n_pred = regress_model.predict(m_test_scaled)

mse = mean_squared_error(n_test, n_pred)
mae = mean_absolute_error(n_test, n_pred)
r2 = r2_score(n_test, n_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)