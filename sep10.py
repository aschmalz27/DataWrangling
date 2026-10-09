import pandas as pd 
import glob
from functools import reduce

artist_net_worth = pd.read_csv("c:/Users/schma/Downloads/artist_net_worth.csv")
artist_number_one_hits = pd.read_csv("c:/Users/schma/Downloads/artist_number_one_hits.csv")

artist_data = pd.merge(artist_net_worth, artist_number_one_hits, how='left', left_on='Artist', right_on='artist', validate="1:1")

files = glob.glob("C:/Users/schma/Downloads/artist_data/*.csv")

df_list = []

for i in files: 
    df = pd.read_csv(i)
    df = df.drop_duplicates()
    df_list.append(df)

artist_complete = reduce(lambda left, right: pd.merge(left, right, on="Artists", how="left"), df_list)

artist_complete.merge(deleted_item, how='left', Left_on='Artist', right_on='artist')

artist_complete.to_csv("artist_complete.csv", index=False)