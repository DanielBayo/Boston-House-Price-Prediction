"""
This is a web app created with Streamlit to host this project. Feel free to use this file as a guide or visit my
article on the topic (linked below).
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

st.header("Predicting Selling Price of Boston House")



st.write("""
Created By: Daniel Bayo Ayangbile

This is a Streamlit web app created so users could predict the selling price of their home. 

Use the sidebar to provide information about your house and the click the predict button.
""")
st.image(Image.open('boston_house.jpg'), width = 400)

st.sidebar.header('Welcome! Please input your details below')

def main():
    title=st.sidebar.selectbox("Title",("Mr.","Mrs.","Miss."))
    name=st.sidebar.text_input("Name of Buyer","Type here")
    no_rm=st.sidebar.slider("Number of Rooms in the House",1,10,1)
    poverty_level=st.sidebar.slider("Neighborhood poverty Level(%)",5,100,5)
    student_teacher_ratio=st.sidebar.slider("Ratio of Student to Teacher in Nearby School",10,25,1)
    data = {"Title":title,"Name":name,"Number of Room":no_rm,"Student_Teacher Ratio":student_teacher_ratio,
            "Poverty_Level":poverty_level}
    
    
    features = pd.DataFrame(data, index=[0])
    input_data=[[no_rm,poverty_level,student_teacher_ratio]]


    #Write out input selection
    st.subheader('User Input Table')
    st.write(features)

    #Load in model
    regressor = pickle.load(open('regressor.pkl', 'rb'))

    # Apply model to make predictions
    #Displaying your prediction
    if st.sidebar.button("Predict"):
        result=regressor.predict(input_data)
        st.success("Dear {0} {1} you should consider selling your house at :$ {2}".format(title,name,np.round(result[0],0)))



#st.subheader('Exploratory Data Analysis')
#st.write("""
#We identified some important features in the readmittance rate that you can explore below. To begin, here is the distribution
#of the classes in the original data set. We see that a majority of patients are not readmitted within a year. Patients that 
#are readmitted often have complications to their diabetes or the specific care recieved.
#""")
#st.image(Image.open('Images/Readmit_rate.png'), width = 500)

#st.write("""
#Now looking at the patient population given the long-term blood sugar HbA1c test, we see only about 20% of patients received
#this test, but, of those, 50% then had their medication changed and were less likely to be readmitted.
#""")
#st.image(Image.open('Images/HbA1c_test.png'), width = 500)

#st.write("""
#Finally, we see that age plays an important role. As expected, older patients have more complications due to their diabetes.
#Age was binned according to this chart into 0-30, 30-60, and 60-100.
#""")
#st.image(Image.open('Images/Readmit_vs_age.png'), width = 500)

#st.subheader('More Information')
#st.write("""
#For a deeper dive into the project, please visit the [repo on GitHub](https://github.com/ArenCarpenter/Diabetes_Hospitalizations) 
#where you can find all the code used in analysis, modeling, visualizations, etc. You can also read my 
#[articles](https://arencarpenter.medium.com/) in Towards Data Science on my other projects. 
#""")
if __name__=='__main__':
  main()
