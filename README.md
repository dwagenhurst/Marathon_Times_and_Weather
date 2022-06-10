# Capstone Project

## Introduction
In this project we have sought to construct models to predict the estimated completion time for  a marathon. Features used were age and gender of athletes and the local weather conditions on the day of the event. Athlete data was scraped from various websites and weather data was collected via the Visual Crossing Weather API. 

## Problem Statement
How do weather conditions impact the time it takes to complete a marathon?

## Data Dictionary
For features in Clean_{event}_Results_Weather.csv files

Feature                  |Type|      Description
|---|---|---|
|year                    |float64|   year the event occured|
|age                     |object|    age of participant grouped on age divisions|
|male                    |float64|   indicator of gender 1 for male 0 for female|
|time_seconds            |float64|   time taken to finish marathon in seconds|
|minimum_temperature     |float64|   minimum temperature observed|
|maximum_temperature     |float64|   maximum temperature observed|
|temperature             |float64|   average temperature observed|
|relative_humidity       |float64|   relative humidity|
|wind_speed              |float64|   average wind speed observed|
|precipitation           |float64|   amount of liquid equivalent precipitation (rain, snow etc.)|
|precipitation_cover     |float64|   percentage of time where measurable precipitation occurred|
|cloud_cover             |float64|   percentage of sky that is covered by cloud|
|clear                   |int64|     weather calculated as clear based on other weather elements|
|overcast                |int64|     weather calculated as overcast based on other weather elements|
|partially_cloudy        |int64|     weather calculated as partially cloudy based on other weather elements|
|rain                    |int64|     weather calculated as rain based on other weather elements|

## Models
The primary metric for evaluating model performace was mean absolute error.

### Baseline
For each event evaluated the baseline was generated by predicting the simple average of completion time. Mean absolute errors were:

|Event      |Model|     MAE (Seconds)|
|---|---|---|
|Berlin     |Baseline|  1287|
|Boston     |Baseline|  1456|
|Chicago    |Baseline|  1349|
|London     |Baseline|  1289|
|NYC        |Baseline|  1559|
|Combined   |Baseline|  2547|

### Best
A variety of models were examined. Specifically; Linear, Ridge, Lasso, Elastic Net, XGBoost Regressor, and GLM Gamma Regressor. Interestingly, the top performing model type varied event to event despite seemingly being very similar problems and having access to the same information. Each event was put through all model types and was tested against a variety of model parameters and input features. Best performace for each event was:

|Event      |Model|                 MAE (Seconds)|
|---|---|---|
|Berlin     |Linear Regression|     334.096|
|Boston     |Linear Regression|     626.640| 
|Chicago    |XGBoost Regressor|     373.298| 
|London     |Elastic Net|           399.768| 
|NYC        |Elastic Net|           256.442| 
|Combined   |Elastic Net|           490.407|  

## Conclusion
No one model reigns supreme but there are some feature that tend to stand out as important. Gender and age group have to be considered when examining a diverse dataset like the ones collected for this project. For weather; temperature, humidity, precipitation, and cloud cover carry the most significant coefficients.

## Going Forward
This project might be improved with more years of marathon results. The final models used focused on events occuring between 2000 and 2018 to try to limit models noticing growing popularity of marathons. Although, participation for berlin marathon doubled in this time frame. Adding earlier years may require implementing trend analysis.

A continuation of this I think would be interesting, is to make a model for each age group to find if weather conditions impact different age groups more or less than others. For this I recommend gathering additional data. More detailed weather data, additional results, and course profile could all be looked into. 