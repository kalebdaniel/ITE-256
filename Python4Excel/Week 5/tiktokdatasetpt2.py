import pandas as pd
df = pd.read_csv("TikTok_songs_2022.csv")
df.info(data)
df = pd.read_csv(index="track_name", columns='artist_name',
                 values="album)
