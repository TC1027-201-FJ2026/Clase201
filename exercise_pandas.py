import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = {'A': [114, 93, 78, 84],
        'B': [23, 19, 21, 18],
        'C': [5, 8, 9, 11]
        }

df = pd.DataFrame(data)

corr_matrix = df.corr()

sn.heatmap(corr_matrix, annot=True)
plt.show()