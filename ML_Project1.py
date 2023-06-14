import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Loading saved model
loaded_model = pickle.load(open('trained_model .sav', 'rb'))

# Creating prediction
def prediction(input_data):
    # Converting input data to numeric values
    input_data = [float(x) for x in input_data]

    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the np array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==1):
        print('Loan is approved')
    else:
        print('Loan is not approved')
        
def main():
    # Giving title
    st.title('Loan Status Prediction')
    # Getting input data from the user
    Loan_ID = st.text_input('Loan_ID')
    Gender= st.text_input('Gender')
    Married = st.text_input('Married ')
    Dependents= st.text_input('Dependents')
    Education = st.text_input('Education	 ')
    Self_Employed= st.text_input('Self_Employed	 ')
    ApplicantIncome= st.text_input('ApplicantIncome	 ')
    CoapplicantIncome = st.text_input('CoapplicantIncome		 ')
    LoanAmount = st.text_input('LoanAmount		 ')
    Loan_Amount_Term = st.text_input('Loan_Amount_Term		 ')
    Credit_History= st.text_input('Credit_History			 ')
    Property_Area= st.text_input('Property_Area		 ')
    
    
    # Code for prediction
    diagnosis = ""

    if st.button("User Result"):
        input_data = [Loan_ID,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
        diagnosis = prediction(input_data)

    st.success(diagnosis)
    
    

if __name__ == '__main__':
    main()