import pandas as pd

data = pd.read_csv("TikTok_songs_2022.csv")

pd.pivot_table(data, index="track_information", columns='artist_information', values='fact_information')

print(pivot)
print(df)

df(head)
df = pd.DataFrame(data)
print(df)

print(df.info())

df.index.name = "user_id"

print(df)
print(df.loc[18])

print(df)

df.groupby(["TikTok songs 2022"]).mean()
pivot = pd.pivot_table(data,
                 index="track_name", columns='artist_name',
                 values="album",
                 aggfunc='mean')
print(pivot)

print(pd.melt(pivot.iloc[:-1,:-1].reset_index(),
        id_vars="track",
        value_name="TikTok songs 2022"))

import numpy as np
%matplotlib inline

df = pd.DataFrame(data)
df.index.name = "track_name"
df.columns.name = "artist_name"
df(print)

df.plot()

