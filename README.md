# Task 3: Linear Regression on Housing Dataset

## Objective
To implement and understand simple and multiple linear regression using the Housing dataset.

## Tools Used
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn

## Steps Followed

1. **Data Import and Preprocessing**
   - Loaded `Housing.csv` using `pandas`.
   - Applied one-hot encoding to categorical features.
   - Checked for missing values.

2. **Train-Test Split**
   - Used `train_test_split` to split the dataset into 80% training and 20% testing data.

3. **Model Training**
   - Trained a linear regression model using `sklearn.linear_model.LinearRegression`.

4. **Model Evaluation**
   - Metrics used: MAE, MSE, R² score.

5. **Visualization**
   - Plotted actual vs predicted prices to visualize model performance.

## Results

- **Mean Absolute Error (MAE):** _printed in notebook_
- **Mean Squared Error (MSE):** _printed in notebook_
- **R² Score:** _printed in notebook_

## File Structure
- `linear_regression_housing.ipynb`: Jupyter notebook with complete implementation.
- `Housing.csv`: Dataset used for training and evaluation.

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
