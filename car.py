import pandas as pd
import streamlit as st
import seaborn as sns

link = 'https://raw.githubusercontent.com/LucaSainteCroix/teaching-resources/main/exercises-data/cars.csv'
car = pd.read_csv(link)
st.write(car)








# Add radio buttons for filtering by region
regions = car['continent'].unique()  # Get unique continents from the 'continent' column
selected_region = st.radio('Select a region', regions)

# Filter the dataframe based on selected region
filtered_car = car[car['continent'] == selected_region]

# Display filtered results
st.write(filtered_car)

# Display heatmap for filtered data
if not filtered_car.empty:
    car_correlation = sns.heatmap(filtered_car.corr(), center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(car_correlation.figure)
else:
    st.write("No data to display for the selected region. Please choose a different region.")

