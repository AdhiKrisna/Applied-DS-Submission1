import pandas as pd
import joblib

# Load pipeline model
pipeline = joblib.load("model/model.pkl")

# Contoh data baru
data = {
    'Age': [30],
    'DailyRate': [900],
    'DistanceFromHome': [5],
    'HourlyRate': [70],
    'MonthlyIncome': [5000],
    'MonthlyRate': [20000],
    'NumCompaniesWorked': [3],
    'PercentSalaryHike': [14],
    'TotalWorkingYears': [8],
    'TrainingTimesLastYear': [3],
    'YearsAtCompany': [4],
    'YearsInCurrentRole': [2],
    'YearsSinceLastPromotion': [1],
    'YearsWithCurrManager': [2],
    
    'Education': [3],
    'EnvironmentSatisfaction': [3],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobSatisfaction': [2],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [3],
    'StockOptionLevel': [1],
    'WorkLifeBalance': [3],
    
    'BusinessTravel': ['Travel_Rarely'],
    'Department': ['Research & Development'],
    'EducationField': ['Life Sciences'],
    'Gender': ['Male'],
    'JobRole': ['Sales Executive'],
    'MaritalStatus': ['Single'],
    'OverTime': ['Yes']
}

new_data = pd.DataFrame(data)

# Prediksi
prediction = pipeline.predict(new_data)[0]
print("Predicted Attrition:", "Yes (1)" if prediction == 1 else "No (0)")