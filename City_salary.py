
import pandas as pd

df = pd.read_csv(r'C:\Users\Thunderobot\Desktop\Обучение Python\ДЗ\AZ01\AZ01\dz.csv', quotechar='"',encoding='utf-8')

print(df.groupby('City')['Salary'].mean().sort_values(ascending=False))
