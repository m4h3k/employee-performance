# Importing required libraries

import streamlit as st
import joblib
import pandas as pd


# Loading the trained Decision Tree model

model = joblib.load("model.pkl")


# Streamlit application

st.title("📊 Employee Performance Score Prediction")

st.divider()

st.write(
    "👤 Enter the employee details below and click the "
    "'🔮 Predict' button to predict the employee's Performance Score."
)

st.divider()


# Taking input from the user

years = st.slider(
    "📅 Years at Company",
    min_value=0,
    max_value=15,
    value=2,
    step=1
)

salary = st.slider(
    "💰 Employee's Monthly Salary",
    min_value=1000,
    max_value=10000,
    value=5000,
    step=100
)

overtime = st.slider(
    "⏰ Overtime Hours",
    min_value=0,
    max_value=100,
    value=0,
    step=1
)

promotions = st.slider(
    "🚀 Promotions",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

satisfaction = st.selectbox(
    "😊 Employee Satisfaction Score",
    options=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
    index=2
)


st.divider()


# Prediction button

prediction_button = st.button("🔮 Predict the Performance Score")


if prediction_button:

    # Creating a DataFrame with the same
    # feature names and order used during training

    input_data = pd.DataFrame({
        "Years_At_Company": [years],
        "Monthly_Salary": [salary],
        "Overtime_Hours": [overtime],
        "Promotions": [promotions],
        "Employee_Satisfaction_Score": [satisfaction]
    })


    # Making the prediction

    prediction = model.predict(input_data)[0]


    # Displaying prediction based on Performance Score

    if prediction == 5:
        st.success(
            f"🌟 Predicted Performance Score: {prediction} 🏆"
        )

    elif prediction == 4:
        st.success(
            f"⭐ Predicted Performance Score: {prediction} ✅"
        )

    elif prediction == 3:
        st.info(
            f"📊 Predicted Performance Score: {prediction} 📈"
        )

    elif prediction == 2:
        st.warning(
            f"⚠️ Predicted Performance Score: {prediction} 📉"
        )

    else:
        st.error(
            f"🔴 Predicted Performance Score: {prediction} ❗"
        )


    st.divider()


    # Adding predicted score to employee information

    employee_information = input_data.copy()

    employee_information["Predicted_Performance_Score"] = prediction


    # Displaying employee information table

    st.subheader("📋 Employee Information")

    st.table(employee_information)


else:

    st.info(
        "💡 Please enter the employee details and click "
        "the 🔮 'Predict the Performance Score' button."
    )
