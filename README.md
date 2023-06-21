# k_means_NLP

How to use this program:

0. Open main.py
1. In the file input_files.txt specify, which documents to use for this clusterization algorithm.
2. On line 62 specify, which directory the files should be located.
3. After line 173 you can add "data = TwoDData". It is artificial data made purely for the testing purposes of k-means clustering. The best supposed K should be = 3 and the clusters should be: 1. ['point1', 'point2', 'point3', 'point'4], 2. ['point5', 'point6', 'point7', 'point8', 'point9', 'point10'], 3. ['point11', 'point12', 'point13', 'point14', 'point15']
4. On line 189 you can set kmeans_clustering(k, 1000) to kmeans_clustering(k, 100). It will work faster then, but the lower that number is, the more likely it is that the data will be clusterized with errors and the elbow graph will also look very weird. An errorless elbow graph should have smaller variance the bigger the K is.
5. If you get the error "IndexError: list index out of range" then before line 183 ("k_values = range(a, b)") set "b = some smaller number"! If that doesn't work, try to run the program again!
