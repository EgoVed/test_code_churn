import pandas as pd

df = pd.read_csv('text.csv')
min = df['value'].min()
max = df['value'].max()
mean = df['value'].mean()
