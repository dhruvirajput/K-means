import dataset
import kmeans
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
iris_data = dataset.load_dataset('iris.csv')

# Convert class names to numeric representations
iris_data, iris_classes = dataset.to_numeric(iris_data, 'species')

# Convert dataframe strings to floats
attrs_conv = list(iris_data.axes[1][:-1])
data = dataset.from_str(iris_data, attrs_conv)

# Convert dataset to matrix representation
iris_ds = dataset.to_matrix(iris_data)
print(type(iris_ds))
# Perform k-means clustering
centroids, cluster_assignments, iters, orig_centroids = kmeans.cluster(np.delete(iris_ds, 4, 1), 3)

# Output results
print ('Number of iterations:', iters)
print ('\nFinal centroids:\n', centroids)
print ('\nCluster membership and error of first 10 instances:\n', cluster_assignments[:10])
print ('\nOriginal centroids:\n', orig_centroids)

