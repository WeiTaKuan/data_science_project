import os 
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as stat


def columnType(df):
    numeric = list()
    category = list()
    
    for i in df.columns:
        # binary value in the column
        if len(df[i].unique()) == 2:
            df[i] = df[i].astype("category")
            category.append(i)
        else:
            numeric.append(i)
    return (df, category, numeric)