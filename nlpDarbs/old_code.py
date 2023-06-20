# old code for building structure
# for content in document_words:
#     doc_array = []
#     for word in all_words:
#         tfidf = calculate_tfidf(word, content, document_words)
#         map1 = {"word":word, "value":tfidf}
#         doc_array.append(map1)
#     map2 = {"index": index, "tf_idf_row" : doc_array}
#     tf_idf_arr.append(map2)
#     index += 1