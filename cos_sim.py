import nltk
import numpy as np
import math


d1 = "As with just about every other commodity, from push-up bras and sneakers to shampoo and candy bars, the wellness industry taps into consumers’ fears and insecurities to move product."
d2 = "Nate Higgins, founder of Portland-based juice bar chain Kure, is well aware of the modern superpower that is marketing. “The internet has also given us the opportunity to explore our own mortality in a way that has never been experienced before,” he says."
d3 = "The word “toxin” is a buzzword in the wellness industry and a propagator of fear in consumers. Its “toxic” connotations imply that those who do not flush their bodies are being poisoned by them. The truth is pretty much the opposite: Human organs are designed to do most of the heavy lifting." 
d1 = "This is a foo bar sentence ."
d2 = "This sentence is similar to a foo bar sentence ."
d3 = "What is this string ? Totally not related to the other two lines ."

documents = [d1, d2, d3]
tokens = [item.lower() for document in documents for item in nltk.word_tokenize(document)]
tokens = list(set(tokens))
tokens.sort(key=len)
# print(tokens)
common_words = ['”', 'a', '“', '.', ':', '’', ',', 'by', 'do', 'to', 'as', 'in', 'of', 'is', 'us', 'he', 'our', 'own', 'who', 'way', 'bar', 'not', 'and', 'its', 'the', 'has', 'are','much', 'that', 'most', 'with', 'been', 'those']

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def compare3(vectors):
    first = np.array(vectors[0], dtype=float)
    second = np.array(vectors[1], dtype=float)
    third = np.array(vectors[2], dtype=float)
    print("first, second: sim = ", cos_sim(first, second))
    print("first, third: sim = ", cos_sim(first, third))
    print("second, third: sim = ", cos_sim(second, third))

def token_count(doc, token):
    return nltk.Text(item.lower() for item in nltk.word_tokenize(doc)).count(token)

def vectorize3(tokens):
    return [[token_count(documents[i], token) for token in tokens] for i in range(3)]

print("# normal")
# print(vectorize3(tokens))
compare3(vectorize3(tokens))

print("# without_common_words")
without_common = [token for token in tokens if token not in common_words]
# print(without_common)
compare3(vectorize3(without_common))

print("# idf")

def idf_vectorize3(tokens):
    return [[math.log(3 / sum([1 if token_count(documents[j], token) > 0 
        else 0 for j in range(3)])) * token_count(documents[i], token)
        for token in tokens] for i in range(3)]

compare3(idf_vectorize3(tokens))


