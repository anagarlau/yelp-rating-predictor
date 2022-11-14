import pandas as pd
import os
import re
import nltk
import string
text = 'theLongAndWindingRoad ABC A'
#first_try = re.sub('(?<=.)(?=[A-Z]+)', r" ", text)
result = re.sub('(?<=.)(?=[A-Z][a-z])', r" ", text)
#d
result2 = re.sub(r'\b\w{1}\b', ' ', result)

print(result2)

#%%
