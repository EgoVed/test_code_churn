import pandas as pd
import numpy as np

df = pd.read_csv('text.csv')
min = df['value'].min()
max = df['value'].max()
count_values_1 = df['value'].count()

sum = abs(df['value'].sum())
