# **📊 Employee Performance Score Prediction**

A machine learning project that predicts an employee's **Performance Score** using employee-related features such as years at the company, monthly salary, overtime hours, promotions, and employee satisfaction.

The project covers the complete machine learning workflow — from data exploration and visualization to model training, evaluation, explainability, model deployment, and a Streamlit prediction application.

---

# **🚀 Project Overview**

The goal of this project is to build a machine learning classification model capable of predicting an employee's **Performance Score** on a scale of **1 to 5**.

The project includes:

* 📥 Data loading and exploration
* 🧹 Data preprocessing
* 📊 Exploratory Data Analysis (EDA)
* 📈 Data visualization
* 🔍 Correlation analysis
* 🤖 Multiple machine learning models
* ⚙️ Hyperparameter tuning
* 📏 Model evaluation
* 🌳 Decision Tree visualization
* 💾 Model serialization
* 🖥️ Streamlit deployment

---

## **📁 Repository Structure**

```
employee-performance/
│
├── Extended_Employee_Performance_and_Productivity_Data.csv
│
├── Performance Prediction.ipynb
│
├── app.py
│
├── model.pkl
│
└── scaler.pkl
```

### File Description

| File                                                      | Description                                                                                    |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Extended_Employee_Performance_and_Productivity_Data.csv` | Employee performance and productivity dataset                                                  |
| `Performance Prediction.ipynb`                            | Complete data analysis, visualization, model training, evaluation, and explainability workflow |
| `app.py`                                                  | Streamlit web application for making employee performance predictions                          |
| `model.pkl`                                               | Trained Decision Tree classification model used by the Streamlit application                   |
| `scaler.pkl`                                              | Saved feature scaler from the preprocessing/model experimentation workflow                     |

> **Note:** The current Streamlit application uses the Decision Tree model in `model.pkl`, which was trained using the original unscaled features. Therefore, `scaler.pkl` is not required for the current prediction flow.

---

## **📊 Dataset**

The dataset contains **100,000 employee records** and **20 columns** covering employee demographics, employment information, productivity, compensation, and performance.

### Main Features

| Feature                       | Description                          |
| ----------------------------- | ------------------------------------ |
| `Employee_ID`                 | Unique employee identifier           |
| `Department`                  | Employee's department                |
| `Gender`                      | Employee gender                      |
| `Age`                         | Employee age                         |
| `Job_Title`                   | Employee's job title                 |
| `Hire_Date`                   | Employee hiring date                 |
| `Years_At_Company`            | Number of years spent at the company |
| `Education_Level`             | Employee education level             |
| `Performance_Score`           | Target variable ranging from 1 to 5  |
| `Monthly_Salary`              | Employee monthly salary              |
| `Work_Hours_Per_Week`         | Weekly working hours                 |
| `Projects_Handled`            | Number of projects handled           |
| `Overtime_Hours`              | Overtime hours                       |
| `Sick_Days`                   | Number of sick days                  |
| `Remote_Work_Frequency`       | Frequency of remote work             |
| `Team_Size`                   | Employee's team size                 |
| `Training_Hours`              | Training hours completed             |
| `Promotions`                  | Number of promotions                 |
| `Employee_Satisfaction_Score` | Employee satisfaction score          |
| `Resigned`                    | Whether the employee resigned        |

---

## **🔎 Exploratory Data Analysis**

The notebook performs several exploratory analyses, including:

* Dataset structure and data types
* Missing-value inspection
* Duplicate-value checking
* Statistical summaries
* Performance Score distribution
* Average salary by department
* Gender distribution
* Employee count by department
* Total overtime hours by department
* Average overtime hours by Performance Score and department
* Correlation matrix

The analysis helps identify patterns and relationships between employee characteristics and performance.

---

## **🤖 Machine Learning Models**

Several classification algorithms were explored:

### 1. Logistic Regression

Logistic Regression was trained using standardized features.

### 2. K-Nearest Neighbors

KNN was trained using standardized features, with **5-fold cross-validation** used to search for suitable values of:

* `n_neighbors`
* `weights`

### 3. Random Forest

A Random Forest classifier was trained using the original, unscaled features.

### 4. Decision Tree

A Decision Tree classifier was trained using the original, unscaled features.

The Decision Tree was selected for deployment in the Streamlit application.

---

## **🌳 Final Model**

The deployed model is a **Decision Tree Classifier**.

The model uses the following five features:

```
Years_At_Company
Monthly_Salary
Overtime_Hours
Promotions
Employee_Satisfaction_Score
```

The target variable is:

```
Performance_Score
```

with five possible classes:

```
1
2
3
4
5
```

The trained model is stored in:

```
model.pkl
```

---

## **💡 Model Explainability**

Feature importance was examined using the Decision Tree's built-in feature importance:

```
tree.feature_importances_
```

The analysis showed that `Monthly_Salary` had substantially higher impurity-based importance than the other selected features in the trained Decision Tree.


> **Important:** Feature importance indicates how the trained model uses features for prediction. It does not establish that a feature causes an employee's performance score to change.

---

## **🖥️ Streamlit Application**

The project includes an interactive Streamlit application that allows users to enter employee information and receive a predicted Performance Score.

The application accepts:

* 📅 Years at Company
* 💰 Monthly Salary
* ⏰ Overtime Hours
* 🚀 Promotions
* 😊 Employee Satisfaction Score

The interface uses sliders and a select box for easy input.

After clicking **Predict the Performance Score**, the application displays:

* 🔮 Predicted Performance Score
* 📋 Employee information entered by the user
* 🎯 Score-specific feedback indicators

---

## **⚙️ Running the Application Locally**

### 1. Clone the repository

```
git clone https://github.com/m4h3k/employee-performance.git
```

### 2. Navigate to the project directory

```
cd employee-performance
```

### 3. Install the required libraries

```
pip install pandas numpy matplotlib seaborn scikit-learn shap streamlit joblib
```

### 4. Run the Streamlit application

```
streamlit run app.py
```

The application will open in your browser.

---

## **🧪 Machine Learning Workflow**

The overall workflow followed in this project is:

```
Dataset
   ↓
Data Inspection
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Decision Tree Selection
   ↓
Model Serialization
   ↓
Streamlit Deployment
```

---

## **🛠️ Technologies Used**

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 🎨 Seaborn
* 🤖 Scikit-learn
* 💾 Joblib
* 🖥️ Streamlit
* 📓 Jupyter Notebook

---

## **📌 Key Learning Outcomes**

This project demonstrates practical experience with:

* Data preprocessing
* Exploratory data analysis
* Data visualization
* Classification algorithms
* Train/test splitting
* Feature scaling
* Cross-validation
* GridSearchCV
* Model evaluation
* Decision Tree interpretation
* Model persistence with Joblib
* Building a machine learning web application with Streamlit

---

## **⚠️ Disclaimer**

This project is intended for **educational and demonstration purposes**.

The model's predictions should not be treated as a definitive assessment of an employee's actual performance. Model predictions depend on the dataset, selected features, training process, and assumptions used during development.

---

## **👨‍💻 Author**

**m4h3k**

GitHub repository: `m4h3k/employee-performance`
