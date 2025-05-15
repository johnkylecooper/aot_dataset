# Transform data from individual tables to a database using Pandas

import matplotlib.pyplot as plt
import pandas as pd
import os

path_to_data = './military_member_data'
data_files = [f for f in os.listdir(path_to_data) if '.csv' in f]

example_df = pd.read_csv(os.path.join(path_to_data, 'Mikasa_Ackermann_(Anime).csv'))
example_column_names = example_df.iloc[:,0].values

df_agg = pd.DataFrame(columns=example_column_names)
for f in data_files:
    df = pd.read_csv(os.path.join(path_to_data, f))
    df_agg = pd.concat([df_agg, df.set_index('Unnamed: 0').T], axis=0, join='outer')

print(df_agg.columns)
print(df_agg['Weight'].value_counts())