Egyptian Real Estate Price Prediction

Predict real estate valuation based on a variety of factors to ensure fair market value for potential investors/buyers of real estate in Egypt.

Dataset: https://www.kaggle.com/datasets/hassankhaled21/egyptian-real-estate-listings 
CookieCutter Data Science (CCDS): https://cookiecutter-data-science.drivendata.org/

🏠 Egypt Real Estate Listings Dataset
📌 Overview

This dataset contains ~20,000 real estate property listings collected from PropertyFinder Egypt.
It includes detailed information about properties for sale such as price, size, location, type, number of bedrooms/bathrooms, availability, and payment methods.

📑 Columns
Column 	        Description
url 	        Direct link to the property listing on PropertyFinder Egypt.
price 	        Property price in Egyptian Pounds (string, contains comma separators).
description 	Detailed property description (English/Arabic mixed text).
location 	    Full location including compound, city, and governorate.
type 	        Property type (Apartment, Villa, Townhouse, etc.).
size 	        Property size in both square feet and square meters.
bedrooms 	    Number of bedrooms (can be numeric or string like 3+ Maid).
bathrooms 	    Number of bathrooms.
available_from 	Availability date for the property (nullable).
payment_method 	Payment method (e.g., Cash, Installments).
down_payment 	Down payment amount (only available for ~5k listings).

Kaggle Author: Hassan Khaled


🪴 Sprint 2: Data Cleaning and Processing
- Clean data (missing data, standardize columns, etc.)
- Process data (turn to usd or make another column for usd, etc.)
	- create a new column that categorizes into a city, suburbs, rural, etc. (maybe)
- Train model to predict valuation of real estate on a variety of factors
I feel that I have accomplished quite a lot in terms of progress towards the final product. I have cleaned the data by standardizing columns, removing extreme outliers, removing odd fields that were due to user-input error, and creating new columns that enhance the analysis as I had to parse some columns in order to work with multiple values in a single column

🌳 Sprint 3: The Model
Plan:
- Compare various models to determine which model is ideal for this dataset
- Analyze the strongest features for each model
- Finetune hyperparameters to find the best parameters 
- Using test statistics such as MSE, RMSE, and R-Squared score

## Overview
- Converted 'type' column from string to int (1 through 10) where 1 represented the most frequent type of real estate, and 10 represented the least frequent
	- removed 4 types of real estate (Roof, Full Floor, Palace, and Whole Building) as they are weird entries
- Converted 'maid_room' column from binary to int (True: 1, False: 0)

### Validation
- Hyperparameter Tuning: Grid Search CV and Randomized Search CV
- K-Fold Cross Validation (10 folds)




