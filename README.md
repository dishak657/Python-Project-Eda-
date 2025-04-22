NYC School Attendance & Chronic Absenteeism Analysis (2016–2021)
This Python project performs a comprehensive exploratory data analysis (EDA) on New York City public schools’ end-of-year attendance and chronic absenteeism data from the academic years 2016–17 to 2020–21. It includes data cleaning, visualization, and insights into attendance patterns across years, grades, and school categories.

🔍 Features
✅ Data Cleaning & Preprocessing

Handles missing and suppressed values ('s')

Converts relevant columns to numeric for analysis

Detects and removes outliers using IQR

📈 Trend Analysis

Yearly trends in attendance and chronic absenteeism

Pre-COVID vs. post-COVID attendance comparison

🏫 School & Grade Analysis

Grade-wise average attendance

Schools with highest and lowest attendance

Attendance comparison across categories (e.g., boroughs, types)

📊 Visualizations

Line plot for year-wise attendance

Bar plot for grade-wise attendance

Scatter plot (Days Present vs. % Attendance)

Box/Whisker plot for attendance distribution

Heatmap showing correlations among key metrics

Histogram of attendance distribution

Pie and donut charts of top chronic absentee categories

📁 Dataset
Source: NYC DOE public dataset (2016–2021)

Columns include:

# Days Present, # Days Absent, % Attendance

# Chronically Absent, % Chronically Absent

School Name, Grade, Category, Year, etc.

🛠️ Technologies Used
Python

Pandas

Matplotlib

Seaborn

NumPy

📌 How to Run
Clone the repository

Install required libraries using pip install -r requirements.txt

Place the CSV file in the same directory or update the path

Run the script to generate outputs and visualizations

📈 Sample Outputs
Visual insights into how COVID-19 impacted attendance

Distribution of chronic absenteeism across school categories

Identification of schools with attendance challenges

