# Wine Quality Data: Data Wrangling Project 
import pandas as pd
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
X = wine_quality.data.features 
y = wine_quality.data.targets 
  
# metadata 
print(wine_quality.metadata) 
  
# variable information 
print(wine_quality.variables) 

wine_quality_names = pd.read_csv("winequality.names_csv")
red_wine_quality = pd.read_csv("winequality-red_csv")
white_wine_quality = pd.read_csv("winequality-white_csv")

wine_quality.head()


