import nltk
import math
from nltk.stem import WordNetLemmatizer
import random
import matplotlib.pyplot as plt

input_files = []


with open('input_files.txt', 'r') as file:
    for line in file:
        # Process the line
        input_files.append(line.strip())

print(input_files)


# file read and tf-idf calculation functions

def tokenize_text_into_array_of_words(text_string):
    lower_case_text = text_string.lower()
    words_array = nltk.word_tokenize(lower_case_text)
    return words_array

def lemmatize_array(arr):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in arr:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words

def calculate_tf(word, document):
    word_count = document.count(word)
    tf = word_count
    return tf

# def calculate_tf(word, document):
#     word_count = document.count(word)
#     tf = word_count / len(document)
#     return tf

def calculate_idf(word, corpus):
    document_count = 0
    for document in corpus:
        if word in document:
            document_count += 1
    idf = math.log(len(corpus) / (document_count), 2)
    return idf

def calculate_tfidf(word, document, corpus):
    tf = calculate_tf(word, document)
    idf = calculate_idf(word, corpus)
    tfidf = tf * idf
    return tfidf

document_words = []
word_occurence = {}
all_file_contents = ""
all_words = []
for file_name in input_files:
    with open("documents/mixed/"+file_name, 'r', encoding="utf8") as file2:
        file_contents = file2.read()
        all_file_contents += file_contents + " "
        document_words.append(lemmatize_array(tokenize_text_into_array_of_words(file_contents)))

all_words = list(set(lemmatize_array(tokenize_text_into_array_of_words(all_file_contents))))
index = 1
data = {}
document_names = ["cyan.txt", "green.txt", "grey.txt", "magenta.txt", "yellow.txt"]
for content in document_words:
    doc_array = {}
    for word in all_words:
        tfidf = calculate_tfidf(word, content, document_words)
        doc_array[word] = tfidf
    data[input_files[index-1]] = doc_array
    index += 1

# k means clustering functions

def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += math.pow((point1[i] - point2[i]), 2)
    return math.sqrt(squared_distance)

def initialize_centers(k):
    samples = random.sample(data_points, k)
    centers = [sample[0] for sample in samples]
    return centers

def assign_points_to_clusters(centers):
    clusters = [[] for _ in range(len(centers))]
    
    for point in data_points:
        distances = [euclidean_distance(point[0], center) for center in centers]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def update_centers(clusters):
    new_centers = []
    
    for cluster in clusters:
        cluster_point_coords_2D_array = []
        for coords in cluster:
            cluster_point_coords_2D_array.append(coords[0])
        cluster_center = [sum(coords) / len(coords) for coords in zip(*(cluster_point_coords_2D_array))]
        new_centers.append(cluster_center)
    
    return new_centers

def calculate_wcss(clusters, centers):
    wcss = 0
    
    for i in range(len(clusters)):
        cluster = clusters[i]
        center = centers[i]
        
        for point in cluster:
            wcss += math.pow(euclidean_distance(point[0], center), 2)
    
    return wcss

def find_angle(line1_slope, line2_slope):
    angle1 = 180 + math.degrees(math.atan(line1_slope))
    angle2 = math.degrees(math.atan(line2_slope))

    angle_diff = abs(angle1 - angle2)
    
    return angle_diff

def get_clusters_and_centers(k):
    centers = initialize_centers(k)
    
    while True:
        clusters = assign_points_to_clusters(centers)
        new_centers = update_centers(clusters)
        
        if new_centers == centers:
            break
        
        centers = new_centers
    
    return clusters, centers

def kmeans_clustering(k, iterations):
    best_clusters_version = (([], ""), -1)
    for _ in range(iterations):
        clusters, centers = get_clusters_and_centers(k)
        
        # Calculate WCSS
        wcss = calculate_wcss(clusters, centers)
        
        # Append variation value to the list
        total_variation = wcss / len(data)

        if(best_clusters_version[1] == -1 or best_clusters_version[1] > total_variation):
            best_clusters_version = (clusters, total_variation)

    return best_clusters_version, total_variation


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

# Extracting the values from the dictionary
data_points = [(list(point.values()), key) for key, point in data.items()]

# Set the range of K values to try
a = 1
b = 9
k_values = range(a, b)

# Initialize list to store the variations values
variations = []

# Iterate over different K values
for k in k_values:
    # Run k-means clustering
    best_clusters_version = kmeans_clustering(k, 1000)
    variations.append(best_clusters_version[1])

    print("Which document was assigned to which cluster (k="+str(k)+"):")
    for cluster in best_clusters_version[0][0]:
        print([c[1] for c in cluster])
    print()

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

# old input files

# iot.txt
# stoicism.txt
# nietzsche.txt
# judaism.txt
# islam.txt
# christianity.txt
# prototypes.txt
# crypto_hash.txt
# chinese_philosophy.txt