import pandas as pd
import numpy as np

a = pd.read_csv('records.txt', sep=',', header=None)
print(a)
print(a.shape)
print(a[0])
b = np.array(a)
grades = b[1:11, 1:]
print(grades)