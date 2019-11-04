import pandas as pd
import numpy as np
df = pd.read_csv('EtsySoldOrderItems2018.csv')

df['var_cl'] = df['Variations'].str.split('US').str[0]
df['var_cl'] = df['var_cl'].str.split(':').str[1]
print(df['var_cl'].value_counts())
