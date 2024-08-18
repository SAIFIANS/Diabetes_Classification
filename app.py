import numpy as np
import pickle
import streamlit as st
import sklearn
import warnings
import time as t

warnings.filterwarnings("ignore")


# loading the saved model
loaded_model = pickle.load(open('model/finalized_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]


  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction')
    st.sidebar.title("Project Author Details")
    st.sidebar.markdown("### Project Author :")
    st.sidebar.info("Mohammad Saifi Ansari")
    st.sidebar.info("+919711619185",icon="📱")
    st.sidebar.markdown("###  Email :")
    st.sidebar.link_button("Gmail", url="mailto: saifiansari17@gmail.com")
    st.sidebar.markdown("###  LinkedIn :")
    st.sidebar.link_button("LinkedIn", url="https://www.linkedin.com/in/mohammad-saifi-ansari/")
    st.sidebar.markdown("###  Github :")
    st.sidebar.link_button("Github", url="https://github.com/SAIFIANS")
    st.sidebar.link_button("Check out the Complete Github Repo", url="https://github.com/SAIFIANS/Diabetes_Classification")

    # getting the input data from the user
    
    
    Pregnancies = st.number_input('Number of Pregnancies', min_value = 0, max_value = 100)
    Glucose = st.number_input('Glucose Level', min_value = 0, max_value = 200)
    BloodPressure = st.number_input('Blood Pressure value', min_value = 0, max_value = 100)
    SkinThickness = st.number_input('Skin Thickness value', min_value = 0, max_value = 100)
    Insulin = st.number_input('Insulin Level', min_value = 0, max_value = 200)
    BMI = st.number_input('BMI value', min_value = 0.000, max_value = 100.000 , step = 0.001)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value = 0.001, max_value = 100.000 , step = 0.001)
    Age = st.number_input('Age of the Person', min_value = 0, max_value = 100)
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        with st.spinner("Processing your request"):
            t.sleep(2)
        if (diagnosis == 0):
            st.success('The person is not diabetic')
            st.balloons()
        else:
            st.success('The person is diabetic')  
       
    
if __name__ == '__main__':
    main()
    
