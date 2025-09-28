Egyptian Real Estate Price Prediction

Dataset: https://www.kaggle.com/datasets/hassankhaled21/egyptian-real-estate-listings 
CookieCutter Data Science (CCDS): https://cookiecutter-data-science.drivendata.org/

🏠 Egypt Real Estate Listings Dataset
📌 Overview

This dataset contains ~20,000 real estate property listings collected from PropertyFinder Egypt.
It includes detailed information about properties for sale such as price, size, location, type, number of bedrooms/bathrooms, availability, and payment methods.

The dataset can be used for:

    🧮 Price prediction models (ML/Regression).
    📊 Exploratory Data Analysis on the Egyptian real estate market.
    📝 NLP tasks using property descriptions (Arabic + English mix).
    📍 Geospatial analysis of property locations in Cairo, Giza, Red Sea, etc.

📑 Data Dictionary
Column 	Description
url 	Direct link to the property listing on PropertyFinder Egypt.
price 	Property price in Egyptian Pounds (string, contains comma separators).
description 	Detailed property description (English/Arabic mixed text).
location 	Full location including compound, city, and governorate.
type 	Property type (Apartment, Villa, Townhouse, etc.).
size 	Property size in both square feet and square meters.
bedrooms 	Number of bedrooms (can be numeric or string like 3+ Maid).
bathrooms 	Number of bathrooms.
available_from 	Availability date for the property (nullable).
payment_method 	Payment method (e.g., Cash, Installments).
down_payment 	Down payment amount (only available for ~5k listings).
🔍 Key Notes

    Some fields have missing values (down_payment, available_from).
    price and size are stored as strings with separators (need cleaning for ML).
    description contains mixed Arabic/English text → suitable for NLP preprocessing.
    Data collected in August 2025.

🚀 Example Use Cases

    Predict housing prices in Cairo/New Cairo using regression.
    Analyze popular locations and property types.
    Text analysis of property descriptions (keyword extraction, clustering).
    Compare payment methods (Cash vs. Installments) across locations.

📜 License

This dataset is released under CC BY 4.0 License.
Attribution is required if used in research or commercial projects.
🙌 Acknowledgements

Data source: PropertyFinder Egypt

Kaggle Author: Hassan Khaled

Plan
- Clean data
- Process data (turn to usd or make another column for usd, etc.)
	- create a new column that categorizes into a city, suburbs, rural, etc. (maybe)


