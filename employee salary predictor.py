import pandas as pd
import numpy as np
import joblib
import streamlit as st

def main():
  html_temp = """<h1>Salary Predictor</h1>"""

  model = joblib.load("salary_prediction")

  st.markdown(html_temp, unsafe_allow_html=True)
  st.markdown("This app will help you to predict your annual salary package")

  p1 = st.number_input("Please enter age ", 18, 70, step=1)
  p2 = st.number_input("Please enter experience years ", 0, 40, step=1)
  p3 = st.slider("How many certifications", 0, 15)
  p4 = st.number_input("Please enter overtime hours ", 0, 60, step=1)
  p5 = st.number_input("Please enter company tenure ", 0.0, 15.0, step=1.1)
  p6 = st.slider("How many projects completed", 0, 30)

  s1 = st.selectbox("Select the education", ('Diploma', 'Bachelor', 'PhD', 'Master'))
  if s1 == 'Diploma':
    p7 = 0
  elif s1 == "Bachelor":
    p7 = 1
  elif s1 == "PhD":
    p7 = 2
  else:
    p7 = 3

  s2 = st.selectbox("select your department", ('Operations', 'IT', 'Finance', 'Sales', 'HR', 'Marketing'))
  if s2 == "Operations":
    p8 = 0
  elif s2 == "IT":
    p8 = 1
  elif   s2 == "Finance":
    p8 = 2
  elif s2 == "Sales":
    p8 = 3
  elif s2 == "HR":
    p8 = 4
  elif s2 == "Marketing":
    p8 = 5

  s3 = st.selectbox("Select your job level", ('Junior', 'Manager', 'Mid', 'Senior', 'Lead'))
  if s3 == "Junior":
    p9 = 0
  elif s3 == "Manager":
    p9 = 1
  elif s3 == "Mid":
    p9 = 2
  elif s3 == "Senior":
    p9 = 3
  elif s3 == "Lead":
    p9 = 4

  p10 = st.slider("Performance Rating", 0, 5)

  s4 = st.selectbox("Select your city", ('Hyderabad', 'Mumbai', 'Pune', 'Chennai', 'Bangalore', 'Delhi'))
  if s4 == "Hyderabad":
    p11 = 0
  elif s4 == "Mumbai":
    p11 = 1
  elif s4 == "Pune":
    p11 = 2
  elif s4 == "Chennai":
    p11 = 3
  elif s4 == "Bangalore":
    p11 = 4
  elif s4 == "Delhi":
    p11 = 5

  s5 = st.selectbox("Remote Work", ('Yes', 'No'))
  if s5 == 'No':
    p12 = 0
  else:
    p12 = 1

  p13 = st.number_input("Please enter skill score ", 0.0, 100.0, step=0.5)

  data_new = pd.DataFrame({
    'Age': p1,
    'Education': p7, 
    'Experience_Years': p2,
    'Department': p8,
    'Job_Level': p9,
    'Performance_Rating': p10,
    'Certifications': p3,
    'Overtime_Hours': p4,
    'Remote_Work': p12,
    'City': p11,
    'Company_Tenure': p5,
    'Projects_Completed': p6,
    'Skill_Score': p13
  },index=[0])

  if st.button("Predict"):
    pred = model.predict(data_new)
    st.success("You can expect {:.2f} LPA".format(pred[0]))



if __name__ == '__main__':
  main()