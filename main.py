import pandas as pd

ds = pd.read_csv(r'C:\Users\Thunderobot\Desktop\Обучение Python\ДЗ\AZ01\AZ01\spotify_top_songs_2024.csv', quotechar='"',encoding='utf-8')
#print(ds)

print(ds.head())
print(ds.info())
print(ds.describe())
