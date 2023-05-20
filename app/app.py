import streamlit as st
import pandas as pd

st.title('Gapminder')
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")
 
'''# Load data
@st.cache
def load_data():
    # Load and preprocess data here
    df = pd.read_csv('data.csv')
    return df

df = load_data()

# Create widgets
year = st.slider('Year', min_value=df['year'].min(), max_value=df['year'].max())
countries = st.multiselect('Country', options=df['country'].unique())

# Filter data based on widget values
df = df[(df['year'] == year) & (df['country'].isin(countries))]

# Create bubble chart
fig = px.scatter(df, x='gni_per_capita', y='life_expectancy', size='population', color='country', log_x=True)
st.plotly_chart(fig)
'''