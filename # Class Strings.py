# Class Strings

import pandas as pd 
import statsmodels.api as sm 
import seaborn as sns 
import matplotlib.pyplot as plt
import networkx as nx 
from pyvis.netork import Network 

lyrics = pd.read_csv("C:Users/schma/Downloads/sample_lyrics_2025.csv")

lyrics[['songwriter', 'week', 'lyrics']]

lyrics.loc[0, 'week']

lyrics['year'] = lyrics['week'].str.extract('(\d{4})').astype(int)

lyrics['fucks_given'] = lyrics['lyrics'].str.count('[Ff]uck') 

lyrics['profanity_ny'] = lyrics['lyrics'].str.contains(r'[Ff]uck|[Ss]hit|[Dd]amn|\b[Hh]ell\b', regex=True)

lyrics['profanity_ny'] = lyrics['profanity_ny'].apply(lambda x: 1 if x else 0)

sm.formula.logit('profanity_ny ~ year', data = lyrics)

fitted_model = model.fit()

fitted_model.summary()

predictions = fitted_model.predict() 

sns.scatterplot(x=lyrics['year'], y=predictions)
plt.show()

lyrics = lyrics.sample(200)

songwriters = pd.get_dummies(lyrics['songwriter'].str.split(',').explode(), dtype=int).groupby(level=0).sum()

songwritersT = songwriters.T

adj_matrix = songwritersT.dot(songwritersT.T)

def_edges = adj_matrix.stack().reset_index()

df_edges.columns = ['Source', 'Target', 'Weight']

df_edges = df_edges[(df_edges['Weight']>0)&(df_edges['Source']!=df_edges['Target'])]

G = nx.from_pandas_edgelist(
    df_edges, source="Source", target="Target", edge_attr=True
)

net.from_nx(G)

net.show_buttons()

net.show('C:/songwriters_network.html')

