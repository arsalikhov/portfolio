# This code looks for key words in a DataFrame column (Column Text in this code) and assigns rating based on impressions
# that participants wrote down, the impressions are taken from a survey. These could take any form, due to ability
# to change the key words.



# # Importing data


### Importing the required modules ###

import pandas as pd
import numpy as np

### Importing the data and creating a Data Frame ###

data = pd.read_csv('data_file_location')
df = pd.DataFrame(data)



# # Assigning impression rating to the responses


### List of the words to search for in order to find the impressions ###
### The format is searchfor(n), where n is the impression rating ###

searchfor1 = ["bad", "dire", "terrible", "disastrous", "devil", "hell",
              "depression", "harmful", "disturbing"]
searchfor2 = ["negative", "not good", "bad", "not right", "wrong", "selfish"]
searchfor3 = ["okay", "neutral", "unchainged", "regardless",
              "doesn't matter", "normal"]
searchfor4 = ["good", "fine", "alright", "positive"]
searchfor5 = ["great", "awesome", "amazing", "very positive"]

### Creates a column called 'Impression' where the score is assigned from 1 to 5,
    ### very negative to very positive accordingly ###

df['Impression'] = pd.np.where(df.Text.str.contains('|'.join(searchfor1)),"1",         #very negative
                   pd.np.where(df.Text.str.contains('|'.join(searchfor2)),"2",         #negative
                   pd.np.where(df.Text.str.contains('|'.join(searchfor3)),"3",         #neutral
                   pd.np.where(df.Text.str.contains('|'.join(searchfor4)),"4",         #positive
                   pd.np.where(df.Text.str.contains('|'.join(searchfor5)),"5", 0)))))  #very positive

### 0 is codded for NA ###



# # Assigning the intentions to the responses


### List of the words to search for in order to find the intentions ###
### The format is searchfor(2_n), where n is the intention rating ###

searchfor2_1 = ["generous", "kind", "thoughtful", "understanding", "patient", ]
searchfor2_2 = ["This person seems", "writer seems", "author seems", "OP seems", "OP",
               "author is", "author preferes", "self"]

### Creates a column called 'Intention' where the score is assigned from 1 to 2,
    ### other-focused to self-focused accordingly ###

df['Intention'] = pd.np.where(df.Text.str.contains('|'.join(searchfor2_1)),"1",       #other-focused
                   pd.np.where(df.Text.str.contains('|'.join(searchfor2_2)),"2", 0))  #self-focused

### 0 is codded for NA ###



# # Exporting the coded data


### Exports coded data ###

df.to_csv("coded_data.csv")

