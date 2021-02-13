import pandas as pd
import numpy as np
import sys

i = int(sys.argv[1])

df = pd.read_csv('../2001_Census/India_villdir.csv')
arr = df.to_numpy()
curr = arr[:, i]

print(np.min(curr), np.max(curr))

print(df.columns[i])
