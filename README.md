# Marathon Result Estimation Based on Weather

**Repo Contents**
|File/Folder|Contents|
|---|---|
|data               |folder of all event data that was scraped and weather information, further divided by each event and if it is original data vs cleaned|
|model testing      |collection of models tested separated on model type|
|scrape and api     |notebooks of code used to collect data separated on event|
|streamlit          |streamlit app and pickle file of trained model for each event|
|EDA                |graphs/charts to explore the data|
|Final Models       |top performing model for each event and their baseline|


## Introduction
In this project we have sought to construct models to predict the estimated completion time for a marathon. Features used were age and gender of athletes and the local weather conditions on the day of the event. Athlete data was scraped from various websites and weather data was collected via the Visual Crossing Weather API. 

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
The primary metric for evaluating model performace was mean absolute error. Root mean squared error was also looked at during testing.

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

### Top Result From Each Model Type
All model types tested are represented below. Top performing model is bolded but can be explicitly found under Best Model section. Initially I started with a basic linear regression model due to its speed so I could quickly get a feel for if features were distracting to my models. While on linear regression this is where I decided to focus just on years 2000-2018, dummying the age groups rather than just using a single value, and training on all results instead of a subsection (top 10k finishers, dropping fastest and slowest 20%).

|EVENT      |Linear|        Ridge   |Lasso|     Elastic Net |XGBoost|       GLM|
|---|---|---|---|---|---|---|
|Berlin     |**334.096**|   376.314 |356.284|   336.27      |349.424|       366.37|
|Boston     |**626.64**|    1072.017|1143.317|  1048.302    |1087.617|      1024.897|
|Chicago    |530.388|       592.249 |675.004|   522.734     |**373.298**|   578.535|
|London     |414.92|        503.633 |513.016|   **399.768** |409.823|       412.117|
|NYC        |265.863|       579.465 |284.953|   **256.442** |304.401|       331.092|
|Combined   |556.168|       971.907 |978.974|   **493.334** |897.832|       1146.631|


### Best Model
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
No one model reigns supreme but there are some feature that tend to stand out as important. Gender and age group have to be considered when examining a diverse dataset like the ones collected for this project. For weather; temperature, humidity, precipitation, and cloud cover carry the most significant coefficients. I am pleased with the models ability to make estimations. However, I believe they could continue to improve given additional time especially Boston.

## Going Forward
This project might be improved with more years of marathon results. The final models used focused on events occuring between 2000 and 2018 to try to limit models noticing growing popularity of marathons. Although, participation for berlin marathon doubled in this time frame. Adding earlier years may require implementing trend analysis.

A continuation of this I think would be interesting, is to make a model for each age group to find if weather conditions impact different age groups more or less than others. For this I recommend gathering additional data. More detailed weather data, additional results, and course profile could all be looked into. 