import numpy as np
import pandas as pd
import pickle

def predict_time(event, age, male, temperature, relative_humidity, wind_speed, 
            precipitation, precipitation_cover, cloud_cover, conditions):
    """
    predict average completion time for given parameters

    Args:
        takes in all user inputs, makes them numeric 
    Returns:
        time in seconds for estimated average completion time 
    """
    with open(event.lower() + '_model.pkl', 'rb') as f:
        model = pickle.load(f)

    if male == 'Male':
        male = 1
    elif male == 'Female':
        male = 0


    if age == '18-39':
        age = [0,0,0,0,0,0,0]
    elif age == '40-44':
        age = [1,0,0,0,0,0,0]
    elif age == '45-49':
        age = [0,1,0,0,0,0,0]
    elif age == '50-54':
        age = [0,0,1,0,0,0,0]
    elif age == '55-59':
        age = [0,0,0,1,0,0,0]
    elif age == '60-64':
        age = [0,0,0,0,1,0,0]
    elif age == '65-69':
        age = [0,0,0,0,0,1,0]
    else:
        age = [0,0,0,0,0,0,1]


    if conditions == 'Clear':
        conditions = [0,0,0]
    if conditions == 'Overcast':
        conditions = [1,0,0]
    if conditions == 'Partially Cloudy':
        conditions = [0,1,0]
    if conditions == 'Rain':
        conditions = [0,0,1]


    if event in ['Berlin', 'London', 'NYC']:
        features = pd.DataFrame([[male, temperature, relative_humidity, wind_speed, precipitation,
            precipitation_cover, cloud_cover, conditions[0], conditions[1], conditions[2], 0,
            age[0], age[1], age[2], age[3], age[4], age[5], age[6]]], columns=model.feature_names_in_)

    elif event == 'Boston':
        features = pd.DataFrame([[male, temperature, relative_humidity, wind_speed, precipitation,
            precipitation_cover, cloud_cover, conditions[2], 0, age[0], age[1], age[2], age[3],
            age[4], age[5], age[6]]], columns=model.feature_names_in_)

    elif event == 'Chicago':
        features = pd.DataFrame([[male, temperature, relative_humidity, wind_speed, precipitation,
            precipitation_cover, cloud_cover, conditions[2], 0, age[0], age[1], age[2], age[3], age[4], age[5], age[6]]], columns=model.feature_names_in_)

    return model.predict(features)



def hms_time(time_seconds):
    '''Take a time in seconds and convert it to hours : minutes : seconds'''

    hours = int(time_seconds // (60 * 60))
    minutes = int((time_seconds % (60 * 60)) // 60)
    seconds = int((time_seconds % (60 * 60)) % 60)

    while len(str(minutes)) < 2:
        minutes = f'0{minutes}'

    while len(str(seconds)) < 2:
        seconds = f'0{seconds}'

    return f'{hours}:{minutes}:{seconds}'