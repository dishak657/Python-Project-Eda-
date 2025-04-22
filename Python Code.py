import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv(r"C:\Users\hp\Downloads\2016-17_-_2020-21_School_End-of-Year_Attendance_and_Chronic_Absenteeism_Data (4).csv", encoding='ISO-8859-1')


print(df) 
print(df.shape) 
print(df.info()) 
print(df.dtypes) 
print(df.head(10)) 
print(df.tail(10)) 
print(df.isnull().sum().sum().sum()) 
print(df.isnull().sum()) 
print(df.describe().round(2))   


# Convert relevant columns to numeric (handle 's')
columns_to_convert = [
    '# Days Absent', '# Days Present', '# Total Days',
    '% Attendance', '# Chronically Absent', '% Chronically Absent'
]
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col].replace("s", np.nan), errors='coerce')


# Yearly attendance trend
attendance_by_year = df.groupby('Year')['% Attendance'].mean()
print("\nYearly % Attendance:\n", attendance_by_year)


# Yearly chronic absenteeism trend
chronic_by_year = df.groupby('Year')['% Chronically Absent'].mean()
print("\nYearly % Chronically Absent:\n", chronic_by_year)


# Grade-wise attendance analysis
attendance_by_grade = df.groupby('Grade')['% Attendance'].mean()
print("\nGrade-wise % Attendance:\n", attendance_by_grade)


# Schools with highest absenteeism
lowest_attendance = df[['School Name', '% Attendance']].sort_values('% Attendance').dropna().head(10)
print("\nLowest Attendance Schools:\n", lowest_attendance)


# Category-based attendance comparison
attendance_by_category = df.groupby('Category')['% Attendance'].mean()
print("\nAttendance by Category:\n", attendance_by_category)


# Detect and handle outliers in % Attendance
Q1 = df['% Attendance'].quantile(0.25)
Q3 = df['% Attendance'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['% Attendance'] < (Q1 - 1.5 * IQR)) | (df['% Attendance'] > (Q3 + 1.5 * IQR))]
print("\nOutliers in % Attendance:\n", outliers[['School Name', '% Attendance']])


# Correlation heatmap
df_corr = df[columns_to_convert].corr()
sns.heatmap(df_corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# Pre- and Post-COVID Attendance
pre_covid = df[df['Year'].astype(str) < '2020']['% Attendance'].mean()
post_covid = df[df['Year'].astype(str) >= '2020']['% Attendance'].mean()
print("\nPre-COVID Attendance:", pre_covid)
print("Post-COVID Attendance:", post_covid)


# Top/Bottom schools
top_schools = df[['School Name', '% Attendance']].sort_values('% Attendance', ascending=False).dropna().head(10)
print("\nTop Attendance Schools:\n", top_schools)


# Histogram of % Attendance
sns.histplot(df['% Attendance'].dropna(), bins=30, kde=True)
plt.title('Histogram of % Attendance')
plt.xlabel('% Attendance')
plt.ylabel('Frequency')
plt.show()


# Suppressed values count (now all handled)
suppressed_counts = (df[columns_to_convert] == 's').sum()
print("\nSuppressed Value Counts (post-cleaning):\n", suppressed_counts)


# Create Attendance Ratio metric
df['Attendance Ratio'] = df['# Days Present'] / df['# Total Days']
print("\nSample Attendance Ratio Values:\n", df[['# Days Present', '# Total Days', 'Attendance Ratio']].head())


# Line Plot: Attendance over Years
attendance_by_year.plot(marker='o', linestyle='-', color='green')
plt.title('Line Plot of Average % Attendance by Year')
plt.ylabel('% Attendance')
plt.grid(True)
plt.show()


# Bar Plot: Grade-wise Attendance
attendance_by_grade.plot(kind='bar', color='skyblue')
plt.title('Bar Plot of % Attendance by Grade')
plt.ylabel('% Attendance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Scatter Plot: Days Present vs % Attendance
sns.scatterplot(data=df, x='# Days Present', y='% Attendance')
plt.title('Scatter Plot of Days Present vs % Attendance')
plt.xlabel('# Days Present')
plt.ylabel('% Attendance')
plt.tight_layout()
plt.show()


# Box Plot: Attendance by Grade
sns.boxplot(data=df, x='Grade', y='% Attendance')
plt.title('Box Plot of % Attendance by Grade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Pie Chart: Chronic absenteeism by top categories
top_chronic = df.groupby('Category')['# Chronically Absent'].sum().nlargest(5)
plt.pie(top_chronic, labels=top_chronic.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart - Top 5 Categories by Chronic Absenteeism')
plt.tight_layout()
plt.show()




