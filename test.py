import pandas as pd
import numpy as np

df = pd.read_csv('text.csv')
count_values_1 = df['value'].count()

sum = df['value'].sum()
total_final = (count_values_1/sum)*100
print(total_final)
print(sum)
