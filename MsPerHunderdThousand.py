#Graph MS per 100,000 for relevant countries and regions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import CSV data files as Pandas Dataframe
ms_global = pd.read_csv("MS_GLOBAL_STATS.csv")

# Print Headers
print(ms_global.head(89))

# Print DataFrame Summary
print(ms_global.info())

# Removing Missing Values of MS_GLOBAL

missing_values_count = ms_global.isnull().sum()
droprows= ms_global.dropna()
dropcolumns = ms_global.dropna(axis=1)
cleaned_data = ms_global.fillna(0)
cleaned_data = ms_global.fillna(method='bfill', axis=0).fillna(0)
df = ms_global.drop_duplicates()

df.set_index("Country", inplace=True)

df = df[["Prevalence of MS per 100,000"]]

df = df.loc[['Ireland', 'United Kingdom', 'United States of America', 'Spain', 'France', 'China', 'Global', 'European'], :]

sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Prevalence of MS per 100,000", y=df.index, data=df)
plt.show()




