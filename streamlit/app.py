import pickle
import numpy as np
import streamlit as st
from predict import predict_time, hms_time

st.title('Effect of Weather Conditions on Marathon Times')


with st.form('Event Parameters'):
    event = st.selectbox(
        'Select Event',
        ('Berlin', 'Boston', 'Chicago', 'London', 'NYC'))


    col1, col2 = st.columns(2)

    with col1:
        age = st.selectbox(
            'Select Age Group',
            ('18-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70+'))

        temperature = st.number_input('Temperature (Fahrenheit)', 0.0, 100.0)

        wind_speed = st.number_input('Wind Speed (MPH)', 0.0, 40.0)

        cloud_cover = st.number_input('Cloud / Sky Coverage (%)', 0.0, 100.0)


    with col2:
        male = st.selectbox(
            'Select Gender',
            ('Male', 'Female'))

        relative_humidity = st.number_input('Relative Humidity (%)', 0.0, 100.0)

        precipitation = st.number_input('Expected Precipitation (in) ', 0.0, 10.0)

        precipitation_cover = st.number_input('Percent of Day Raining (%)', 0.0, 100.0)


    conditions = st.selectbox(
        'Select General Condition',
        ('Clear', 'Partially Cloudy', 'Overcast', 'Rainy'))
    

    submit_button = st.form_submit_button('Submit')


nl = '\n'

st.text(f' Expected average completion time is: \n{hms_time(predict_time(event, age, male, temperature, relative_humidity, wind_speed, precipitation, precipitation_cover, cloud_cover, conditions))}')

