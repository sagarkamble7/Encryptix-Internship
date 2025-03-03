import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open(r"D:\Encryptix task 1\rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define feature names (Update based on your dataset)
feature_names = ['PassengerId','Pclass','SibSp','Parch','Sex_female','Sex_male','Embarked_C','Embarked_Q','Embarked_S']

# Streamlit UI
st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival.")

# User input form
with st.form("prediction_form"):
    user_input = []
    for feature in feature_names:
        value = st.number_input(f"{feature}", min_value=0.0, step=1.0)
        user_input.append(value)

    # Submit button
    submit = st.form_submit_button("Predict 🚀")

# Process input and make predictions
if submit:
    # Convert input into a DataFrame
    new_data = pd.DataFrame([user_input], columns=feature_names)

    # Predict
    prediction = model.predict(new_data)
    result = "✅ Survived" if prediction[0] == 1 else "❌ Did Not Survive"

    # Display the result
    st.subheader("Prediction Result:")
    st.success(result)
