import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Employee Performance Predictor", layout="wide")

model = joblib.load("models/performance_model.pkl")

st.title("💼 Employee Performance Predictor")

col1, col2 = st.columns([1, 2])
st.markdown("""
### 🎯 Project Overview
This tool predicts employee performance using Machine Learning.
It helps HR teams make better decisions in promotions, training, and retention.
""")

# INPUT
with col1:
    st.header("Employee Input")

    age = st.slider("Age", 20, 60, 30)
    exp = st.slider("Experience", 1, 20, 5)
    salary = st.slider("Salary", 30000, 150000, 50000)
    train = st.slider("Training Hours", 10, 100, 40)
    dept = st.selectbox("Department", ["HR", "IT", "Sales"])

    predict = st.button("Predict")

# PROCESS
input_df = pd.DataFrame({
    "Age":[age],
    "Experience":[exp],
    "Salary":[salary],
    "TrainingHours":[train],
    "Department":[dept]
})

input_df = pd.get_dummies(input_df)

for col in model.feature_names_in_:
    if col not in input_df:
        input_df[col] = 0

input_df = input_df[model.feature_names_in_]

# OUTPUT
with col2:
    st.header("Prediction Result")

    if predict:
        pred = model.predict(input_df)[0]
        probs = model.predict_proba(input_df)[0]

        labels = {0:"Low",1:"Medium",2:"High"}
        result = labels[pred]

        st.success(f"Prediction: {result}")

        st.subheader("Confidence")
        c1,c2,c3 = st.columns(3)
        c1.metric("Low", round(probs[0],2))
        c2.metric("Medium", round(probs[1],2))
        c3.metric("High", round(probs[2],2))

# DATA + INSIGHTS
if os.path.exists("data/employee_data.csv"):
    data = pd.read_csv("data/employee_data.csv")

    st.subheader("Dataset")
    st.dataframe(data.head())

    st.subheader("Performance Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x="Performance", data=data, ax=ax)
    st.pyplot(fig)

    st.subheader("HR Insights")
    st.write("High performers:", (data["Performance"]=="High").sum())
    st.write("Low performers:", (data["Performance"]=="Low").sum())

    st.markdown("---")
st.markdown("👨‍💻 Developed by: Vayunandan mishra")
st.markdown("📊 Project: Employee Performance Predictor")