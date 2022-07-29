import pandas as pd

filepath = "files/sample.csv"
data = {'name': ['Raphael', 'Donatello'],
        'mask': ['red', 'purple'],
        'weapon': ['sai', 'bo staff']}
df = pd.DataFrame(data)
df.to_csv(filepath, index=False)