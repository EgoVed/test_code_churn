import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('text.csv')
count_values_1 = df['value'].count()

sum = df['value'].sum()
total = count_values_1/sum
