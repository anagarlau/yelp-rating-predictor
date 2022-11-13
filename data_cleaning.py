import pandas as pd
import os
import re
import nltk
import string


yelp = pd.read_csv('german_merged.csv')
yelp.columns.values[0]="ID"
yelp = yelp.rename(columns={'Overall Rating':'Overall_Rating',
                            "Total Reviews":'Total_Reviews',
                            "Restaurant Name":"Restaurant_Name",
                            "Price Range":"Price_Range"})
comments = yelp[['ID', 'Comment']][:3]
print(type(comments))

pd.set_option('max_colwidth', 800)
print(comments)
#%%
