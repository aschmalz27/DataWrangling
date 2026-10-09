import pandas as pd
import matplotlib.pyplot as plt 

# Load the wine datasets
red_wine = pd.read_csv("winequality-red.csv", sep=";")
white_wine = pd.read_csv("winequality-white.csv", sep=";")

# Look at the first five rows
print("Red Wine Data:")
print(red_wine.head())

print("White Wine Data:")
print(white_wine.head())

# Check the size of each dataset
print("Red wine shape:", red_wine.shape)
print("White wine shape:", white_wine.shape)

# Check the quality ratings
print("Red wine quality ratings:")
print(red_wine["quality"].value_counts().sort_index())

print("White wine quality ratings:")
print(white_wine["quality"].value_counts().sort_index())

import os

print("Current folder:", os.getcwd())
print("Files in this folder:", os.listdir())
red_wine = pd.read_csv("winequality-red.csv", sep=";")
white_wine = pd.read_csv("winequality-white.csv", sep=";")