# -*- coding: utf-8 -*-
"""Wine_quality_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/198WxwaELiTKgdsn2zlEtQzAFfnY4gVhJ

Importing Dependencies
"""

import numpy as np
import pandas as pd

"""Data Collection & Analysis & Preprocessing"""

wine_dataset = pd.read_csv('/content/winequality_dataset.csv')

"""

---

"""

wine_dataset.head()

wine_dataset.isnull().sum()

#number of values for each quality
import seaborn as sns
import matplotlib.pyplot as plt

sns.catplot(x="quality", data=wine_dataset, kind="count")

# Set plot labels and title
plt.xlabel("Wine Quality")
plt.ylabel("Count")
plt.title("Distribution of Wine Quality")

# Show the plot
plt.show()

# Create a scatter plot
sns.scatterplot(x="volatile acidity", y="quality", data=wine_dataset)

# Set plot labels and title
plt.xlabel

sns.barplot(x="quality", y="density", data=wine_dataset, ci=None)

# Set plot labels and title
plt.xlabel("Wine Quality")
plt.ylabel("Density")
plt.title("Density vs Wine Quality")

# Show the plot
plt.show()

#coorection heatmap

correlation = wine_dataset.corr()

# Set up the heatmap using Seaborn
plt.figure(figsize=(10, 10))
sns.set(font_scale=0.8)
sns.heatmap(data=correlation, annot=True, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)

# Set plot title
plt.title("Correlation Heatmap")

# Show the plot
plt.show()

#separating data and labels
X = wine_dataset.drop(columns='quality', axis=1)
print(X)

#label binarization

wine_dataset['quality'] = np.where(wine_dataset['quality'] > 7, 1, 0)

Y = wine_dataset['quality']

print(Y)

"""Train Test split"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

"""Model Training"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

model = RandomForestClassifier()

model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)

"""Predictive System"""

input_data = (7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0)

# changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the data as we are predicting the label for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')

