import pandas as pd
data = pd.read_csv("Grades.csv")
df = pd.DataFrame(data)
print(df)

print(df.info())

df.index
df.index.name = "user_id"
print(df)

print(df.loc[572], "Grades", "GPA")
print(df.columns)
df.columns.name = "Properties"

df.rename(columns={"Grades", "GPA": "Students": "Scores"})
print(df)
