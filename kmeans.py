import numpy as np
import scipy.spatial.distance as metric

'''
k-means clustering algorithm
'''

def initialize(ds, k):


	# Number of columns in dataset
	n = np.shape(ds)[1]
     


	# The centroids
	centroids = np.mat(np.zeros((k,n)))

	# Create random centroids
	for j in range(n):
		min_j = min(ds[:,j])
		range_j = float(max(ds[:,j]) - min_j)
		centroids[:,j] = min_j + range_j * np.random.rand(k, 1)

	# Return centroids as numpy array
	return centroids


def euclidean_dist(A, B):
	return metric.euclidean(A, B)


def cluster(ds, k):

	# Number of rows in dataset
	m = np.shape(ds)[0]

	# Hold the instance cluster assignments
	cluster_assignments = np.mat(np.zeros((m, 2)))

	# Initialize centroids
	cents = initialize(ds, k)

	# Preserve original centroids
	cents_orig = cents.copy()

	changed = True
	num_iter = 0

	# Loop until no changes to cluster assignments
	while changed:

		changed = False

		# For every instance (row in dataset)
		for i in range(m):

			# Track minimum distance, and vector index of associated cluster
			min_dist = np.inf
			min_index = -1

			# Calculate distances
			for j in range(k):

				dist_ji = euclidean_dist(cents[j,:], ds[i,:])
				if dist_ji < min_dist:
					min_dist = dist_ji
					min_index = j

			# Check if cluster assignment of instance has changed
			if cluster_assignments[i, 0] != min_index: 
				changed = True

			# Assign instance to appropriate cluster
			cluster_assignments[i, :] = min_index, min_dist**2

		# Update centroid location
		for cent in range(k):
			points = ds[np.nonzero(cluster_assignments[:,0].A==cent)[0]]
			cents[cent,:] = np.mean(points, axis=0)

		# Count iterations
		num_iter += 1

	# Return important stuff when done
	return cents, cluster_assignments, num_iter, cents_orig