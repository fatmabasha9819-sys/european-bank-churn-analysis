# European Bank Customer Churn Predictor

This repository contains a machine learning web application that predicts customer churn based on demographic and financial data from a European bank.

## 🔗 Project Links
* **Deployed Web App (Streamlit):** [Insert https://... link here]
* **Research Paper:** [Insert https://... link here]
* **Project Feedback Video:** [Insert https://... link here]

## 📊 Project Overview
Customer churn is a critical metric for financial institutions. This project utilizes a dataset of 10,000 bank customers to train a Random Forest Classifier. The model evaluates features such as Credit Score, Age, Account Balance, and Number of Products to predict the likelihood of a customer leaving the bank.

## 💻 Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-learn
* **Data Manipulation:** Pandas
* **Web Framework:** Streamlit

## 🚀 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Run the model training script to generate the `.pkl` files:
   `python train_model.py`
4. Launch the Streamlit application:
   `streamlit run app.py`
