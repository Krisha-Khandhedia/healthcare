# -*- coding: utf-8 -*-
"""Healthcare Database.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZKH-lY7vX0TUSk7k_l6uAkZ3Nspjzr_N
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

!pip install numerize

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import warnings
warnings.filterwarnings('ignore')
from numerize import numerize
import plotly.express as px


pd.set_option('display.max_columns',None)

from zipfile import ZipFile
import zipfile

filepath = os.getcwd()
with zipfile.ZipFile('healthcare_dataset.csv.zip','r') as zip_ref:
    zip_ref.extractall(filepath)

df = pd.read_csv('healthcare_dataset.csv')

df.head()

#Remove all unwanted white space from dataset
df = df.replace(r'\s+', ' ', regex=True)

#Change the name of columns
df.columns = df.columns.str.replace(" ","_")

#Checking null values percentage
print("==="*25)
print("Checking Data has null values or not")
print("==="*25)
print(round(df.isnull().sum() * 100 / len(df),2))

#Information
print("Data Information")
print("==="*25)
print(df.info())

df.describe().T

df.describe(include=object).T

#Dividing dataset into numerical columns and categorical columns
df1=df.copy()
#Separating numerical and categorical columns
num=[]
cat=[]
for col in df1.columns:
    if pd.api.types.is_numeric_dtype(df1[col]):
        num.append(col)
    elif pd.api.types.is_object_dtype(df1[col]):
        cat.append(col)

print('Numerical columns : ',num)
print('Categorical columns : ',cat)

# Calculate the correlation matrix
numerical_columns = df.select_dtypes(include=['int64','float64']).corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(20, 6))
sns.heatmap(numerical_columns, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Print the column names in the DataFrame
print("Column Names:", df.columns)

def get_recommendations_for_condition(medical_condition):
    condition_data = df[df['Medical_Condition'] == medical_condition]

    # Check if the condition_data DataFrame is not empty
    if not condition_data.empty:
        hospital_recommendation = condition_data['Hospital'].mode().values[0]
        doctor_recommendation = condition_data['Doctor'].mode().values[0]
        medication_recommendation = condition_data['Medication'].mode().values[0]

        print(f"Recommendations for {medical_condition}:")
        print(f"Hospital Recommendation: {hospital_recommendation}")
        print(f"Doctor Recommendation: {doctor_recommendation}")
        print(f"Medication Recommendation: {medication_recommendation}")
    else:
        print(f"No recommendations available for {medical_condition}.")

# Get user input for medical condition
user_medical_condition = input("Enter the medical condition: ")
get_recommendations_for_condition(user_medical_condition)

