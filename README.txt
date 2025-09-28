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

Plan
- Clean data (missing data, standardize columns, etc.)
- Process data (turn to usd or make another column for usd, etc.)
	- create a new column that categorizes into a city, suburbs, rural, etc. (maybe)
- Train model to predict valuation of real estate on a variety of factors




