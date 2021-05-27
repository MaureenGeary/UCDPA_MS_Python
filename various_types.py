import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Import CSV data files as Pandas Dataframe
ms_global = pd.read_csv("MS_ATLAS_2013.csv")

# Print Head
print(ms_global.head(89))

# Print DataFrame Summary
print(ms_global.info())

# Removing Missing Values of MS_GLOBAL

missing_values_count = ms_global.isnull().sum()
droprows = ms_global.dropna()
dropcolumns = ms_global.dropna(axis=1)
cleaned_data = ms_global.fillna(0)
cleaned_data = ms_global.fillna(method='bfill', axis=0).fillna(0)
df = ms_global.drop_duplicates()

df.set_index("Country", inplace=True)
print(df)

def msTypePieChart(place):
    place = place[["% Relapsing Remitting MS", "% Primary Progressive MS", "% Progressive Relapsing MS"]]

    y = place.values[0]
    print(y)
    mylabels = ["Relapsing Remitting MS", "Primary Progressive MS", "Progressive Relapsing MS"]
    myexplode = [0.2, 0, 0]

    plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
    plt.show()

    return None

msTypePieChart(df.loc[['Ireland']])
msTypePieChart(df.loc[['United Kingdom']])
msTypePieChart(df.loc[['Spain']])
msTypePieChart(df.loc[['France']])


