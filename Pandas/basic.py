import pandas as pd

data = {'Name' : ["Mahy","Bgu"],
      'Age' : [24,23]}
data
df= pd.DataFrame(data)
row = df.loc[1]
row
