import streamlit as st
import requests
from PIL import Image

image = Image.open('dataset-cover.jpg')
st.title("Aplikasi Car Insurance")
st.image(image)
education_format = {0:"None",1:"High School",2:"University"}
def ed_format(option):
        return education_format[option]
        
income_format = {0:"Poverty",1:"Working Class",2:"Middle Class",3:"Upper Class"}
def in_format(option):
        return income_format[option]
EDUCATION = st.selectbox("EDUCATION", options=list(education_format.keys()),format_func=ed_format)
INCOME = st.selectbox("INCOME", options=list(income_format.keys()),format_func=in_format)
CREDIT_SCORE = st.number_input("CREDIT_SCORE", min_value=0.00,max_value=0.99)
ANNUAL_MILEAGE = st.number_input("ANNUAL_MILEAGE", min_value=2000,max_value=22000)
SPEEDING_VIOLATIONS = st.number_input("SPEEDING_VIOLATIONS",min_value=0,max_value=22)
PAST_ACCIDENTS = st.number_input("PAST_ACCIDENTS",min_value=0,max_value=15)
DRIVING_EXPERIENCE = st.selectbox("DRIVING_EXPERIENCE", ['Newbie', 'Amateur', 'Advanced', 'Expert'])
VEHICLE_OWNERSHIP = st.selectbox("VEHICLE_OWNERSHIP", ['Yes', 'No'])
MARRIED = st.selectbox("MARRIED", ['Yes', 'No'])
CHILDREN = st.selectbox("CHILDREN", ['Yes', 'No'])
# inference
data = {'EDUCATION':EDUCATION,
        'INCOME':INCOME,
        'CREDIT_SCORE': CREDIT_SCORE,
        'ANNUAL_MILEAGE':ANNUAL_MILEAGE,
        'SPEEDING_VIOLATIONS':SPEEDING_VIOLATIONS,
        'PAST_ACCIDENTS':PAST_ACCIDENTS,
        'DRIVING_EXPERIENCE' : DRIVING_EXPERIENCE,
        'VEHICLE_OWNERSHIP' : VEHICLE_OWNERSHIP,
        'MARRIED' : MARRIED,
        'CHILDREN' : CHILDREN}

URL = "https://backendcarinsurance.streamlit.app/"

# komunikasi
if st.button('Predict'):
        r = requests.post(URL, json=data)
        res = r.json()
        if res['code'] == 200:
                st.title(res['result']['classes'])