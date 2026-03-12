# ❤️ Heart Disease Risk Analysis & Prediction System

## 📌 Project Overview
Heart disease remains one of the leading causes of mortality worldwide. Early detection of risk factors and preventive care play a crucial role in reducing cardiovascular risk.

This project combines Data Analytics, Machine Learning, and Web Development to build a comprehensive Heart Disease Risk Analysis & Prediction System.

The project transforms healthcare data into:

📊 Actionable insights through data visualization

🧠 Predictive risk modeling using Machine Learning

🌐 Interactive web-based risk simulation

The goal is to help individuals and healthcare professionals better understand heart disease risk and the potential impact of lifestyle changes.

## 🚀 Project Components
### 📊 1. Healthcare Data Analytics (Tableau Dashboard)

The Tableau dashboard analyzes heart disease data to uncover patterns and identify major risk factors.

### Dashboard Insights

#### Demographic Analysis

* Age distribution of heart disease cases
* Gender-based comparison
* Identification of high-risk age groups

#### Lifestyle Risk Factors
* Smoking impact on heart disease
* Physical inactivity correlation
* BMI and obesity trends

#### Clinical Indicators
* Cholesterol level impact
* Blood pressure patterns
* Existing medical conditions

#### Regional Analysis
* Urban vs Rural prevalence
* Geographic disease distribution

#### 🔗 View Live Dashboard:

https://public.tableau.com/views/heart_disease_analysis_story/Dashboard?:language=en-US&:embed=y&:sid=&:redirect=auth&:embed_code_version=3&:loadOrderID=0&:display_count=y&publish=yes&:origin=viz_share_link

## 📖 Data Storytelling (Tableau Story)

To make insights easier to understand, the project also includes a Tableau Story.

The story walks through the data step-by-step and explains:
* How heart disease patterns emerge
* Which lifestyle factors contribute most to risk
* Which population groups are most vulnerable
* What preventive insights can be derived

This storytelling approach helps non-technical audiences understand healthcare data clearly.

#### 🔗 View Live Data Story:

https://public.tableau.com/views/heart_disease_analysis_story/Story?:language=en-US&:embed=y&:sid=&:redirect=auth&:embed_code_version=3&:loadOrderID=0&:display_count=y&publish=yes&:origin=viz_share_link

## 🧠 Machine Learning Risk Prediction System

The project also includes a Machine Learning-based prediction system that estimates the probability of heart disease based on health and lifestyle inputs.

Users can:
* Enter personal health factors
* Predict heart disease probability
* Simulate lifestyle improvements
* Visualize risk reduction

## 🎨 Interactive Web Application

An interactive web interface allows users to explore risk predictions in a visually intuitive way.

Web App Features

✔ Heart disease probability prediction

✔ Dynamic risk level classification

✔ Lifestyle improvement simulation

✔ Interactive visual charts

✔ Risk reduction comparison

✔ Clean and responsive UI

The system demonstrates how AI can support preventive healthcare awareness.

## ⚙️ Machine Learning Pipeline
### Data Preprocessing

The dataset undergoes several preprocessing steps:

* Missing value handling
* Outlier detection using IQR
* Outlier capping
* Encoding categorical variables
* Duplicate removal
* Data cleaning

### Model Training

Multiple models were trained and evaluated:

* Logistic Regression
* Random Forest
* XGBoost

Models were compared using:

* ROC-AUC score
* F1 score
* Classification performance

### Probability Calibration

To improve probability reliability, the final model uses:

### CalibratedClassifierCV

This ensures predicted probabilities better reflect real-world likelihood.

### Threshold Optimization

Instead of using the default threshold (0.5), the classification threshold is optimized using F1-score maximization.

This improves prediction balance for imbalanced healthcare data.

## 📊 Example Prediction Insight

Example output from the system:

Current Risk: 18.5% (Medium)

After lifestyle improvements:

Improved Risk: 11.2%

Risk Reduction: 7.3%

This helps users understand how lifestyle changes can significantly influence cardiovascular health.

## 🏗 System Architecture
<img width="311" height="449" alt="image" src="https://github.com/user-attachments/assets/04b2fd0f-d514-4cb3-85e1-2a4306167276" />


## 🛠 Technologies Used
### Programming

Python

### Machine Learning

Scikit-learn
XGBoost
Pandas
NumPy

### Web Development

Flask
HTML
CSS
JavaScript

### Data Visualization

Tableau

### Model Serialization

Joblib

## 📂 Project Structure

<img width="553" height="513" alt="image" src="https://github.com/user-attachments/assets/501c48d0-7cf6-432d-a2da-ea1fd05ad71c" />


## 🔍 Key Insights from Data

The analysis highlights several important patterns:

* Middle-aged individuals show higher disease prevalence
* Smoking significantly increases cardiovascular risk
* Sedentary lifestyle strongly correlates with heart disease
* High BMI groups show elevated risk levels
* Elevated cholesterol levels strongly influence disease probability

## 🏥 Real-World Applications

This project demonstrates how data science can support healthcare through:

✔ Preventive health awareness

✔ Risk screening tools

✔ Healthcare data analytics

✔ Policy planning support

✔ Educational data science projects


## 🎯 Future Improvements

Possible future enhancements include:

* Explainable AI using SHAP
* Deep learning model comparison
* Real-time health monitoring integration
* Cloud deployment
* Docker containerization
* Integration with healthcare APIs

## 👨‍💻 Author

### Saqib Khan

## 👥 Team Members

### Satyam Pandey
### Shakib Khan
### Satyam Shrivastav

#### ⭐ If you found this project interesting, consider giving it a star!
