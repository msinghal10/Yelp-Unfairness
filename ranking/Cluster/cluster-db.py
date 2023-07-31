import pandas as pd, numpy as np, matplotlib.pyplot as plt, time
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
kms_per_radian = 6371.0088
# Change the file name
df = pd.read_csv('LA.csv') 
# represent points consistently as (lat, lon)
coords = df[['Latitude', 'Longitude']].to_numpy()

# define epsilon as 0.2 kilometers, converted to radians for use by haversine
epsilon = 0.2 / kms_per_radian
start_time = time.time()
db = DBSCAN(eps=epsilon, min_samples=6, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
cluster_labels = db.labels_

# get the number of clusters
num_clusters = len(set(cluster_labels))

# all done, print the outcome
message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
print(message.format(len(df), num_clusters, 100*(1 - float(num_clusters) / len(df)), time.time()-start_time))
print('Silhouette coefficient: {:0.03f}'.format(metrics.silhouette_score(coords, cluster_labels)))

clusters = pd.Series([coords[cluster_labels==n] for n in range(num_clusters)])
clusters.to_csv('LA-cluster1.csv')




