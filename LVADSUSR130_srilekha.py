# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pjkEVPEo6XSp7oF-pCkNmDh0j6_mHMN-
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#1
data=pd.read_excel('/content/Walmart_Dataset Python_Final_Assessment.xlsx')
data.info()

#2
data.isnull().sum()
data.fillna(0)
data.duplicated().sum()
data.drop_duplicates()

#3
print("Mean= ", data.mean())
print("Median= ",data.median())
print("Standard Deviation= ",data.std())
print("Mode= ",data.mode())

#4
import matplotlib.pyplot as plt
import seaborn as sns

# Count plot
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x='Product Name')
plt.title('Count of most saled product')
plt.xlabel('Product Name')
plt.ylabel('Count')
plt.show()

# Scatter plot
plt.figure(figsize=(9, 5))
sns.scatterplot(data=data, x='Geography', y='Sales')
plt.title('Geography vs Sales')
plt.xlabel('Geography')
plt.ylabel('Sales')
plt.show()

# Box plot
plt.figure(figsize=(9, 5))
sns.boxplot(data=data, x='Category', y='Sales')
plt.title(' Category vs Sales')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# Histogram
plt.figure(figsize=(9, 5))
sns.histplot(data['Sales'], bins=21, kde=True)
plt.title('Histogram of Sales')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.show()

#5
correlation = data.corr()
print("Correlation :")
print(correlation)

plt.figure(figsize=(11, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".3f")
plt.title('Correlation')
plt.show()

#6
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
outliers = ((data< (Q1 - 1.5 * IQR)) | (data> (Q3 + 1.5 * IQR))).sum()
print("Number of outliers:")
print(outliers)

#7
#trend analysis
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
yearly_data = data.groupby('Year').agg({
    'Sales': 'sum',
    'Profit': 'sum'}).reset_index()
plt.figure(figsize=(6, 6))
plt.plot(yearly_data['Year'], yearly_data['Sales'], marker='o', label='Total Sales', color='blue')
plt.plot(yearly_data['Year'], yearly_data['Profit'], marker='o', label='Total Profit', color='green')
plt.title('Sales and Profit Trends vs the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(yearly_data['Year'])
plt.legend()
plt.show()
category_sales = data.groupby(['Year', 'Category'])['Sales'].sum().unstack()
plt.figure(figsize=(12, 8))
category_sales.plot(kind='line', marker='o')
plt.title('Sales Trend of Each Product Category Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(yearly_data['Year'])
plt.legend(title='Category')
plt.show()

"""Trend Analysis
Looking at both the trends of sales and profits over the period of years we can find a bit similarity in both the trends since the sales has a drastic growth which is directly proportional to profit which also is seen that the profit has a drastic growth in the later increase of sales which means the demand is more hence the price increased so the profit.
Also looking at data we can say that"Chairs" category has the most growth in Sales over the years.
"""

#7
#Customeranalysis
customer= data.groupby('EmailID')
orders_customer = customer.size()
total_sales_per_customer = customer['Sales'].sum()
customer_stats = pd.DataFrame({
    'No of Orders': orders_customer,
    'Total Sales': total_sales_per_customer
})
sorted_customers = customer_stats.sort_values(by=['No of Orders', 'Total Sales'], ascending=False)
top_5_cust = sorted_customers.head(5)
print("Top 5 Customers:")
print(top_5_cust)

"""So the top5 customers are William,Arthur,RickWilson,GregGuthri,Zuschuss based on their orders placed abd their sales . Looking at this data we can give a insight about these 5 customers as they are the most frequently users of this service ."""