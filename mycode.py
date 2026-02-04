import pandas as pd
import os

data ={'Name':['Lavishka','Harsh','Rohan'],
       'Age':[24,22,25],
       'City':['Pune','Mumbai','Chennai']
       }

df=pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)
print(f"CSV saved to {file_path}")