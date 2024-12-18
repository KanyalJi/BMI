import streamlit as st


st.title('BMI Calculator')

with st.form(key = 'BMI Calculator',clear_on_submit = False):
    col1,col2,col3 = st.columns([2,2,1])
with col1:
    weight = st.number_input('Enter Your Weight in Kg')
with col2:
    height = st.number_input('Enter Your Height in Meter')
with col3:
    submit = st.form_submit_button(label = 'Calculate')

if submit:
  BMI = round((weight / (height**2)),2)

  st.write(BMI)

  if(BMI <= 18.5):
     st.error('UnderWeight')
  
  elif(BMI > 18.5 and BMI <=24.9):
     st.success('Normal')
  
  elif(BMI >= 25 and BMI < 29.9):
     st.warning('Overweight')
  
  else:
     st.error('Obese')


