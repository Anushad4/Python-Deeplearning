# import packages required for clustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.decomposition import PCA

from sklearn.metrics import silhouette_score

white_wine = pd.read_csv('./dataset/winequality_white.csv')

# Null values
nulls = pd.DataFrame(white_wine.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# handling the missing value
data = white_wine.select_dtypes(include=[np.number]).interpolate().dropna()

# find the most correlated features
numeric_features = white_wine.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[:4], '\n')

# Preprocessing the data
scaler = preprocessing.StandardScaler()
scaler.fit(data)
X_scaled_array = scaler.transform(data)
X_scaled = pd.DataFrame(X_scaled_array, columns = data.columns)

wcss = []
# elbow method to know the number of clusters
for i in range(2,12):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
    score = silhouette_score(data, kmeans.labels_, metric='euclidean')
    print("For n_clusters = {}, silhouette score is {})".format(i, score))

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()