
import pandas as pd

"""
Note: 
This code should fail if you run it locally (since the file is only available in the remote machine).
"""

df = pd.read_csv('tutorial.csv')

print('Dataframe:', df.head(5))
print('Done.')
