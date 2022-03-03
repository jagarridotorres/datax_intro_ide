
import pandas as pd
import sklearn.datasets
import matplotlib.pyplot as plt
import seaborn as sns

data = sklearn.datasets.load_iris()

df = pd.DataFrame(data=data.data, columns=data.feature_names)

sns.pairplot(data=df)
plt.show()

print('Example 4. Done')
