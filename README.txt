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

Overview
- Converted 'type' column from string to int (1 through 10) where 1 represented the most frequent type of real estate, and 10 represented the least frequent
	- removed 4 types of real estate (Roof, Full Floor, Palace, and Whole Building) as they are weird entries
- Converted 'maid_room' column from binary to int (True: 1, False: 0)
- Compared Linear Regression and Random Forest Regression -> Random Forest Regression performed much better, so I proceeded with a Random Forest Regression model
- Discovered the most important features for the models -> size, type, and bathrooms were the top 3 with size being the most important
- Converted 'type' variable from string to number, ranked by the occurence in the dataset: apartment, chalet, villa were the top 3 where the apartment type covers around 45% of observations in this dataset
- Created residual plots to observe train vs test residuals
- Calculated and plotted learning curve for random forest regression between the train and test set
- Observed individual predictions vs actual prices -> major errors due to user-errors as the method of data collection relied on user-input
	- Some prices were way beyond a fair market value due to the data scraping from a real estate site that is similar to ebay where sellers can list at any prices they want

Validation
- Hyperparameter Tuning: Grid Search CV and Randomized Search CV
- K-Fold Cross Validation (10 folds) -> average of 0.49 R-squraed score

Future Concerns
- Look into the locations feature and condense it down to just the city in order to use it in the regression models
- Remove extreme prices 
- Consider Gradient Boosting Trees model for more complex and accurate predictions (risk of overfitting though)



