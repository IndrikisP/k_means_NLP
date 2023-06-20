import random
import math
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += math.pow((point1[i] - point2[i]), 2)
    return math.sqrt(squared_distance)

def initialize_centers(k):
    centers = random.sample(data_points, k)
    return centers

def assign_points_to_clusters(centers):
    clusters = [[] for _ in range(len(centers))]
    
    for point in data_points:
        distances = [euclidean_distance(point, center) for center in centers]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    
    #for entry in clusters:
    #    print("In assigned to clusters func")
    #    print(entry)
    return clusters

def update_centers(clusters):
    new_centers = []
    
    i = 0
    for cluster in clusters:
        print(i, ". cluster: ", cluster)
        i = i + 1
        cluster_center = [sum(coords) / len(coords) for coords in zip(*cluster)]
        new_centers.append(cluster_center)
    
    return new_centers

def calculate_wcss(clusters, centers):
    wcss = 0
    
    for i in range(len(clusters)):
        cluster = clusters[i]
        center = centers[i]
        
        for point in cluster:
            wcss += math.pow(euclidean_distance(point, center), 2)
    
    return wcss

def find_angle(line1_slope, line2_slope):
    angle1 = 180 + math.degrees(math.atan(line1_slope))
    angle2 = math.degrees(math.atan(line2_slope))

    angle_diff = abs(angle1 - angle2)
    
    return angle_diff

def kmeans_clustering(k, max_iterations=5000):
    centers = initialize_centers(k)
    
    for _ in range(max_iterations):
        clusters = assign_points_to_clusters(centers)
        new_centers = update_centers(clusters)
        
        if new_centers == centers:
            break
        
        centers = new_centers
    
    return clusters, centers


# Input dictionary
OneDdata = {
    "point1": {"coord1": 45}, "point2": {"coord1": 85}, "point3": {"coord1": 135}, "point4": {"coord1": 170},
    "point5": {"coord1": 305}, "point6": {"coord1": 337}, "point7": {"coord1": 375}, "point8": {"coord1": 400},
    "point9": {"coord1": 488}, "point10": {"coord1": 520}, "point11": {"coord1": 548}, "point12": {"coord1": 590}
}

TwoDdata = {
    "point1": {"coord1": 67, "coord2":82}, "point2": {"coord1": 76, "coord2":44}, "point3": {"coord1": 112, "coord2":32}, "point4": {"coord1": 166, "coord2":106},
    "point5": {"coord1": 335, "coord2":57}, "point6": {"coord1": 405, "coord2":15}, "point7": {"coord1": 400, "coord2":60}, "point8": {"coord1": 455, "coord2":55}, "point9": {"coord1": 370, "coord2":105}, "point10": {"coord1": 450, "coord2":138},
    "point11": {"coord1": 230, "coord2":205}, "point12": {"coord1": 280, "coord2":200}, "point13": {"coord1": 340, "coord2":230}, "point14": {"coord1": 230, "coord2":250}, "point15": {"coord1": 300, "coord2":250}
}

data = TwoDdata

# Extracting the values from the dictionary
data_points = [list(point.values()) for point in data.values()]

# Set the range of K values to try
a = 1
b = 10
k_values = range(a, b)

# Initialize list to store the variations values
variations = []

# Iterate over different K values
for k in k_values:
    # Run k-means clustering
    clusters, centers = kmeans_clustering(k, 5000)
    
    # Calculate WCSS
    wcss = calculate_wcss(clusters, centers)
    
    # Append variation value to the list
    variations.append(wcss / len(data))

angles = []

for k in k_values:
    if k == a or k == b-1:
        continue
    else:
        i = k-1
        angles.append(find_angle(
                (variations[i-1]-variations[i])/((i-1)-i), 
                (variations[i+1]-variations[i])/((i+1)-i)
            ))

#for i in range(len(angles)):
#   print(i, ". ", angles[i])
print("Best supposed K:", angles.index(min(angles))+2)

# Plot the elbow graph
plt.plot(k_values, variations, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Variations')
plt.title('Elbow Method')
plt.show()