import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
st.title('World Cities by Shang')
df = pd.read_csv('worldcities.csv')

population_filter = st.slider('select minimal population', 0.0, 40.0, 3.6)

capital_filter = st.sidebar.multiselect('capital select', df.capital.unique(), ['primary'])

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

df = df[df.population >= population_filter]

df = df[df.capital.isin(capital_filter)]

if country_filter != 'ALL':
    df = df[df.country == country_filter]

st.map(df)
st.write(df)
fig, ax = plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar()
st.pyplot(fig)