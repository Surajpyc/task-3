# -*- coding: utf-8 -*-
"""task 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UPI7sRpt20jICo6dByRKSyFDhKiwstvh
"""

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 2 Load Data
df=pd.read_csv('Housing.csv')
df.head(5)

df.shape

df.isnull().sum()

df.describe()

df.info()

# Convert categorical variables to numeric using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# 3. Feature Selection
X = df.drop("price", axis=1)
y = df["price"]

# 4. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Linear Regression Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = lr.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# 7. Coefficients and Intercept
coeff_df = pd.DataFrame(lr.coef_, index=X.columns, columns=["Coefficient"])
print("\nModel Coefficients:")
print(coeff_df)

# 8. Plotting Actual vs Predicted
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.grid(True)
plt.show()



