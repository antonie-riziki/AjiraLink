import streamlit as st
import pandas as pd
import africastalking
import os
import requests
# import cv2
import google.generativeai as genai

from streamlit_lottie import st_lottie
from PIL import Image


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime

col1, col2 = st.columns(2)

@st.cache(allow_output_mutation=True)
def get_data():
    return []

df = pd.read_csv(r"src/ajiralink-dataset.csv", encoding='latin-1', on_bad_lines='skip')


# if "df" not in st.session_state:
#     try:
#         st.session_state.df = pd.read_csv(r"src/ajiralink-dataset.csv", encoding='latin-1', on_bad_lines='skip')
#     except FileNotFoundError:
#         st.session_state.df = pd.DataFrame(columns=[
#             "OFFICIAL_NAMES", "GENDER", "USERNAME", "EMAIL", "PHONE_NUMBER",
#             "SKILLS", "YOE", "WORK_REGION", "LINKEDIN", "GITHUB", "WEBSITE",
#             "BIO", "PROFILE", "PASSCODE"
#         ])

data = []

with col1:
	with st.form(key="user_registration"):
	    st.subheader("User Self Registration")
	    names = st.text_input("Official Names")
	    gender_text = st.write('Gender')
	    
	    chk_male, chk_female = st.columns(2)
	    
	    with chk_male:
	    	gender = st.checkbox('Male')
	    
	    with chk_female: 
	    	gender = st.checkbox('Female')
	    
	    username = st.text_input('Username:')
	    email = st.text_input("Email: ")
	    phone_number = st.number_input("Phone Number:", value=None, min_value=0, max_value=int(10e10))
	    password = st.text_input('Passowrd', type="password")
	    confirm_password = st.text_input('Confirm password', type='password')

	    checkbox_val = st.checkbox("Subscribe to our Newsletter")

	    submit_personal_details = st.form_submit_button("Submit")

	    # Every form must have a submit button.
	    if password != confirm_password:
	    	st.error('Password mismatch', icon='⚠️')

	    else:
		    
		    if not (email and password):
		    	st.warning('Please enter your credentials!', icon='⚠️')
		    else:
		    	st.success('Proceed to engaging with the system!', icon='👉')

		    	

		    	if submit_personal_details:

			        amount = "10"
			        currency_code = "KES"

			        recipients = [f"+254{str(phone_number)}"]

			        # airtime_rec = "+254" + str(phone_number)

			        print(recipients)
			        print(phone_number)

			        # Set your message
			        message = f"Welcome to AjiraLink, Looking for top-tier professionals or specific skills? You’re in the right place! Our platform connects you with qualified experts across various industries!";

			        # Set your shortCode or senderId
			        sender = 20880

			        try:
			        	# responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)
			        	response = sms.send(message, recipients, sender)

			        	print(response)

			        	# print(responses)

			        except Exception as e:
			        	print(f'Houston, we have a problem: {e}')

	

	# st.write("Outside the form")


def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	else:
		return r.json()


with col2:
	reg_lottie = load_lottieurl("https://lottie.host/701a9d68-8f75-41a1-8c96-3e4b026a3d3f/zeKp8UyfVz.json")
	st_lottie(reg_lottie)




if submit_personal_details == True:

	st.subheader('Professional Information')

	with st.form(key="prof_info"):
		sect_1, sect_2 = st.columns(2)

		with sect_1:
			st.write('Skills')
			skills = st.multiselect(
				"Select the field that best describes your expertise (e.g., Graphic Designer, Gym Trainer, SEO Specialist).",
	    		["Mama Fua", "Chef", "Cleaner", "Care Giver", "Secretary", "Driver", "Designer", "Nurse", "Developer", "Baby sitter"])

			st.divider()

			st.write('Years of Experience')
			yoe_opt = ["0-3 yrs", "4-6 yrs", "7-10 yrs", "above 10yrs"]
			yoe = st.pills("", yoe_opt)

			st.divider()

			st.write('Location')
			location = st.multiselect(
				"Specify your current location or preferred work region.",
	    		["Nairobi", "Nakuru", "Kiambu", "Naivasha", "Kericho", "Kapsabet", "Kitale", "Kisumu", "Kakamega", "Marakwet", "Sugoi", "Mombasa", "Malindi", "Voi", "Kwale", "Anywhere", "Other"])

			if location == "Other":
				st.text_input("Specify location")

			st.divider()

			st.write('Availability')
			availability = st.selectbox(
				"Let clients know if you are available for work immediately or open to offers",
	    		["Full-time", "Part-time", "Hourly", "Unavailable"])

			st.divider()

			st.write('Work Rate')
			work_rate = st.multiselect(
				"Specify your preferred hourly rate",
	    		["2-3k", "4-8k", "9-12k", "12k and above", "Negotiable", "Non Negotiable"])

			st.divider()


		with sect_2:
			st.write("Bio")
			bio = st.text_area(label='Briefly describe yourself', height=400, max_chars=500)

			# st.write("Linkedln (optional)")
			linkedln = st.text_input("Linkedln (optional)", key='linkedln')

			# st.write("Github (optional)")
			github = st.text_input("Github (optional)", key='github')

			# st.write("Website (optional)")
			website = st.text_input("Website (optional)", key='website')


			profile_picture = st.file_uploader("Passport Photo...", type=["jpg", "jpeg", "png"], label_visibility="hidden")

			
			if profile_picture is not None:
				image = Image.open(profile_picture)

				st.image(image, width=70)

			# st.number_input("Phone number...", max_value=13, min_value=0, value=0)


		submit_professional_details = st.form_submit_button("activate account")

	if submit_professional_details == True:

		registration_data = pd.DataFrame({
				'OFFICIAL_NAMES': [names],
				'GENDER': [gender],
				'USERNAME': [username],
				'EMAIL': [email],
				'PHONE_NUMBER': ["0" + phone_number],
				'SKILLS': [skills],
				'YOE': [yoe],
				'WORK_REGION': [location],
				'LINKEDIN': [linkedln],
				'GITHUB': [github],
				'WEBSITE': [website],
				'BIO': [bio],
				'PROFILE': [profile_picture.name if profile_picture else None],
				'PASSCODE': [password],
			})


		get_data().append(registration_data)

st.write(pd.DataFrame(get_data()))











