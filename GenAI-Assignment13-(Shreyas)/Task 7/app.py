#Task 7 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('../performance.csv')
df = df[['Hours_Studied', 'Attendance', 'Parental_Involvement',
       'Access_to_Resources', 'Sleep_Hours', 'Motivation_Level', 'Internet_Access',
        'Family_Income', 'Teacher_Quality', 'Gender',
       'Exam_Score']]
#handling missing values
df['Teacher_Quality'] = df['Teacher_Quality'].astype('category')
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0])

oh = OneHotEncoder(sparse_output=False)
temp = pd.DataFrame(
    oh.fit_transform(df[['Teacher_Quality']]),
    columns=oh.get_feature_names_out()
)

print(temp)
