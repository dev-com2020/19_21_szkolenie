import pandas as pd

df = pd.read_csv('dane/homes.csv')

df.to_json('dane/domki.json')