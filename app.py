# creating stream lit web app
import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

#load the trained model
model = tf.keras.models.load_model('model.h5')

#load the preprocessorss now
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)     

with open('onehot_encoder.pkl', 'rb') as file:
    onehot_encoder = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

    ## streamlit app
st.title("Customer Churn Prediction")

# UI - User input for the features- we encode the categorical features using the loaded encoders
geography = st.selectbox("Geography", onehot_encoder.categories_[0]) # catefories learnt during training
gender = st.selectbox("Gender", label_encoder.classes_) # catefories learnt during training
age = st.number_input("Age", min_value=18, max_value=100, value=30)
credit_score = st.number_input("Credit Score")
balance = st.number_input("Balance")
num_of_products = st.number_input("Number of Products", 1,4)
estimated_salary = st.number_input("Estimated Salary")
tenure = st.number_input("Tenure", 0, 10)
has_credit_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

# Preparingg the input data for prediction
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder.transform([gender])[0]], #encdoing here directly
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

#encoding the geography column using the loaded onehot encoder
geography_encoded = onehot_encoder.transform([[geography]]) # encoding the geography column
geography_encoded_df = pd.DataFrame(geography_encoded, columns=onehot_encoder.get_feature_names_out(['Geography'])) 

# now combine the encoded geography columns with the rest of the input data
input_data = pd.concat([input_data.reset_index(drop=True), geography_encoded_df], axis=1)

# Scaling the input data
input_scaled = scaler.transform(input_data)

# Now predicting churn
if st.button("Predict Churn"):

    # Predict churn
    prediction = model.predict(input_scaled)
    prediction_probability = prediction[0][0]

    st.write(f"Churn Probability: {prediction_probability:.2%}")

    if prediction_probability > 0.5:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is not likely to churn.")
#yaa done!! :)