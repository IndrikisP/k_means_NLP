import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def extract_keywords(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words and filter out stopwords
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for sentence in sentences
             for word in word_tokenize(sentence)
             if word.isalnum() and word.lower() not in stop_words]
    
    # Calculate word frequency distribution
    word_freq = FreqDist(words)
    
    # Retrieve the most common keywords
    keywords = [word for word, freq in word_freq.most_common(5)]
    
    return keywords

# Example usage
text = "Natural language processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. Keyword extraction is a key task in NLP."
keywords = extract_keywords(text)
print(keywords)