import streamlit as st
import joblib
import pandas as pd

st.title("🏦 European Bank Churn Predictor")
st.write("Enter customer details below to predict if they are likely to leave the bank.")

# 1. Load the saved files
@st.cache_resource # This makes the app run faster
def load_models():
    model = joblib.load('churn_model.pkl')
    le_geo = joblib.load('le_geo.pkl')
    le_gender = joblib.load('le_gender.pkl')
    return model, le_geo, le_gender

model, le_geo, le_gender = load_models()

# 2. Create the web layout
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 900, 600)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 18, 100, 40)
    tenure = st.number_input("Tenure (Years)", 0, 10, 3)

with col2:
    balance = st.number_input("Balance", 0.0, value=60000.0)
    num_products = st.number_input("Number of Products", 1, 4, 2)
    has_cr_card = st.selectbox("Has Credit Card?", [1, 0])
    is_active = st.selectbox("Is Active Member?", [1, 0])
    salary = st.number_input("Estimated Salary", 0.0, value=50000.0)

# 3. Predict Button
if st.button("Predict Churn Risk"):
    new_data = {
        'CreditScore': [credit_score],
        'Geography': [geography],
        'Gender': [gender],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active],
        'EstimatedSalary': [salary]
    }
    
    new_customer = pd.DataFrame(new_data)
    
    # Apply encoders
    new_customer['Geography'] = le_geo.transform(new_customer['Geography'])
    new_customer['Gender'] = le_gender.transform(new_customer['Gender'])
    
    # Make Prediction
    prediction = model.predict(new_customer)
    
    st.markdown("---")
    if prediction[0] == 1:
        st.error("⚠️ Prediction: This customer is high-risk and likely to CHURN.")
    else:
        st.success("✅ Prediction: This customer is low-risk and likely to STAY.")