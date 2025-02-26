import streamlit as st
import requests
import json
import pandas as pd 


from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
	with open(filepath, 'r') as file:
		return json.load(file)


def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	else:
		return r.json()

col1, col2 = st.columns(2)

with col1:
	reg_lottie = load_lottiefile("assets/an2.json")
	st_lottie(reg_lottie)


with col2:
	reg_lottie = load_lottiefile("assets/an3.json")
	st_lottie(reg_lottie)


# with col3:
# 	reg_lottie = load_lottiefile("assets/an4.json")
# 	st_lottie(reg_lottie)


# with col4:
# 	reg_lottie = load_lottiefile("assets/an2.json")
# 	st_lottie(reg_lottie)

df = pd.read_csv('src/ajiralink_dummy_data.csv')

# st.dataframe(df.head())

st.subheader(" Welcome to AjiraLink – Your Ultimate Talent Hub! 🎯")

st.write('''

		Looking for top-tier professionals or specific skills? You’re in the right place! Our platform connects you with qualified experts across various industries—whether you need a developer, designer, marketer, or any specialized talent, we’ve got you covered.

		Simply enter the skills or profession you're looking for, and our intelligent system will match you with the best candidates from our database—quickly and efficiently.

		#### 🚀 Why Choose Us?
		- ✅ Access a diverse pool of skilled professionals.
		- ✅ Smart matching system for quick and accurate results.
		- ✅ Verified talent to ensure quality and reliability.
		- ✅ Seamless hiring experience at your fingertips.

		Start exploring today and find the perfect professional for your needs! 💡✨

	''')

st.divider()

search_col1, search_col2 = st.columns(2)

with search_col1:
	category = st.selectbox("I am looking for....", df['SKILLS'].unique())


with search_col2:
	response_win = st.empty()
	grp = df.groupby('SKILLS')
	get_grp = grp.get_group(category)
	st.dataframe(get_grp[['OFFICIAL_NAMES', 'GENDER', 'WORK_REGION', 'AVAILABILITY']])
	
