# !pip install matplotlib
# !pip install seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import RFE
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset
df = pd.read_csv("output/44123-data-nona.csv")

# Define the response variable and explanatory variables
response_variable = "Mean Temp (°C)"
explanatory_variables = ["Temperature", "Max Temp (°C)", "Min Temp (°C)", "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)"]

# Create lagged features for the explanatory variables
lags = 3  # Number of lagged features to create
for var in explanatory_variables:
    for lag in range(1, lags+1):
        df[f"{var}_lag{lag}"] = df[var].shift(lag)

# Drop rows with missing values (first 3 colmns)
df.dropna(inplace=True)

# identify NAs
# meantemp = df["Mean Temp (°C)"]
# meantemp[meantemp.isna()]
# mintemp = df["Min Temp (°C)"]
# mintemp[mintemp.isna()]
# maxtemp = df["Max Temp (°C)"]
# maxtemp[maxtemp.isna()]
# rows_with_na = df[df.isna().any(axis=1)]
# for i in rows_with_na.index:
#     print(df.loc[i])

# Split the dataset into train and test sets
X = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', "Max Temp (°C)", "Min Temp (°C)", "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)"])
X['Month'] = pd.to_datetime(X['Date']).dt.month
X['Quater'] = np.where(X['Month'].isin([1, 2, 3]), 1,
                        np.where(X['Month'].isin([4, 5, 6]), 2,
                                 np.where(X['Month'].isin([7, 8, 9]), 3,
                                          4)))

def perform_linear_regression(X_quarter, y):
    model = LinearRegression()
    rfe = RFE(model)
    rfe = rfe.fit(X_quarter, y)
    selected_columns = X_quarter.columns[rfe.support_]
    X_selected = X_quarter[selected_columns]
    model.fit(X_selected, y)
    return model, selected_columns

quarters = [1,2,3,4]
models = {}
selected_variables = {}

for quarter in quarters:
    X_quarter = X[X['Quater'] == quarter].drop(['Date', 'Month', 'Quater'], axis=1)
    y_quarter= X_quarter[response_variable]
    X_quarter= X_quarter.drop(response_variable, axis=1)
    
    model, selected_cols = perform_linear_regression(X_quarter, y_quarter)
    models[quarter] = model
    selected_variables[quarter] = selected_cols

kf = KFold(n_splits=8, shuffle=True, random_state=42)

for quarter, model in models.items():
    X_quarter = X[X['Quater'] == quarter].drop(['Date', 'Month', 'Quater'], axis=1)
    y_quarter= X_quarter[response_variable]
    X_quarter= X_quarter.drop(response_variable, axis=1)
    
    mse_scores = []
    fig, axs = plt.subplots(ncols=2, nrows=8, figsize=(6,8), layout="constrained")
    plt_index = 0
    for train_index, test_index in kf.split(X_quarter):
        X_train, X_test = X_quarter.iloc[train_index], X_quarter.iloc[test_index]
        y_train, y_test = y_quarter.iloc[train_index], y_quarter.iloc[test_index]
        
        model.fit(X_train[selected_variables[quarter]], y_train)
        y_pred = model.predict(X_test[selected_variables[quarter]])
        mse = np.mean((y_pred - y_test) ** 2)
        mse_scores.append(mse) 
        axs[plt_index,0].plot(list(range(1,1+len(y_pred))),y_pred, color='b')
        axs[plt_index,1].plot(list(range(1,1+len(y_test))),y_test, color='y')
        plt_index = plt_index+1
    print(mse_scores)
    plt.savefig(f"pic/Predicted-and-Tested_{quarter}.png")  # Save the plot as PNG file

for quarter, model in models.items():
    X_quarter = X[X['Quater'] == quarter]
    X_quarter['Year'] = pd.to_datetime(X['Date']).dt.year
    mse_scores = []
    fig, axs = plt.subplots(ncols=2, nrows=8, figsize=(6,8), layout="constrained")
    plt_index = 0
    for year in range(2016,2024):
        print(year)
        X_test = X_quarter[X_quarter['Year']==year][selected_variables[quarter]]
        y_test = X_quarter[X_quarter['Year']==year][response_variable]
        y_pred = model.predict(X_test)
        mse = np.mean((y_pred - y_test) ** 2)
        mse_scores.append(mse) 
        axs[plt_index,0].plot(list(range(1,1+len(y_pred))),y_pred, color='b')
        axs[plt_index,0].set_xlabel("Days")
        axs[plt_index,0].set_ylabel(str(year))
        axs[plt_index,1].plot(list(range(1,1+len(y_test))),y_test, color='y')
        axs[plt_index,1].set_xlabel("Days")
        #axs[plt_index,1].set_ylabel("True Temperature")
        plt_index = plt_index+1
    print(mse_scores)
    axs[0,0].set_title(f'Q{quarter} Predicted Temperature')
    axs[0,1].set_title(f'Q{quarter} True Temperature')
    plt.savefig(f"pic/Predicted-and-Tested-InSeq_{quarter}.png")  # Save the plot as PNG file


# Test the fitted model in new weather station 51459
df = pd.read_csv("output/51459-data-nona.csv")
# Create lagged features for the explanatory variables
lags = 3  # Number of lagged features to create
for var in explanatory_variables:
    for lag in range(1, lags+1):
        df[f"{var}_lag{lag}"] = df[var].shift(lag)

# Drop rows with missing values (first 3 colmns)
df.dropna(inplace=True)

X = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', "Max Temp (°C)", "Min Temp (°C)", "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)"])
X['Month'] = pd.to_datetime(X['Date']).dt.month
X['Quater'] = np.where(X['Month'].isin([1, 2, 3]), 1,
                        np.where(X['Month'].isin([4, 5, 6]), 2,
                                 np.where(X['Month'].isin([7, 8, 9]), 3,
                                          4)))
for quarter, model in models.items():
    X_quarter = X[X['Quater'] == quarter]
    X_quarter['Year'] = pd.to_datetime(X['Date']).dt.year
    mse_scores = []
    fig, axs = plt.subplots(ncols=2, nrows=8, figsize=(6,8), layout="constrained")
    plt_index = 0
    for year in range(2016,2024):
        print(year)
        X_test = X_quarter[X_quarter['Year']==year][selected_variables[quarter]]
        y_test = X_quarter[X_quarter['Year']==year][response_variable]
        y_pred = model.predict(X_test)
        mse = np.mean((y_pred - y_test) ** 2)
        mse_scores.append(mse) 
        axs[plt_index,0].plot(list(range(1,1+len(y_pred))),y_pred, color='b')
        axs[plt_index,0].set_xlabel("Days")
        axs[plt_index,0].set_ylabel(str(year))
        axs[plt_index,1].plot(list(range(1,1+len(y_test))),y_test, color='y')
        axs[plt_index,1].set_ylabel("Days")
        plt_index = plt_index+1
    print(mse_scores)
    axs[0,0].set_title(f'Q{quarter} Predicted Temperature')
    axs[0,1].set_title(f'Q{quarter} True Temperature')
    plt.savefig(f"pic/Predicted-and-Tested-InSeq-51459_{quarter}.png")  # Save the plot as PNG file
