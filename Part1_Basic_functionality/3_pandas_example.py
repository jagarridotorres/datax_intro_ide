
import pandas as pd
import sklearn.datasets

data = sklearn.datasets.load_iris()

df = pd.DataFrame(data=data.data, columns=data.feature_names)

print(df.head(5))
print('Example 3. Done')
