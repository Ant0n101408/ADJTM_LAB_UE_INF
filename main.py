
from services.text_tokenizer import text_tokenizer
# pip install sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np

dataset_true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])  # Read file

sample = dataset_true['title'][:14] # Take a sample of data

# text_tokenized = text_tokenizer(joinedSampledTex)  # Tokenize text by own function


vectorizer = CountVectorizer(tokenizer=text_tokenizer)
vectorizer_tf = TfidfVectorizer(tokenizer=text_tokenizer)

X_transform_sample = vectorizer.fit_transform(sample)
titles_true = (vectorizer.get_feature_names_out())
X_transform_sample_tf = vectorizer_tf.fit_transform(sample)

titles = (vectorizer.get_feature_names_out())  # Get all tokens
array = X_transform_sample.toarray()  # Table [1,0,0....] is token in document
array_tf = X_transform_sample_tf.toarray()

"""
Jeśli do vectorizera liczebnościowego przekażemy jedynie jeden dokument, to jakie
wartości będzie miała otrzymana macierz? Albo jakich nie będzie miała?

Odpowiedz: Nie będzie miała zer.
"""

# Display top 10 tokens

print("Display top 10 tokens")
column_sum = np.sum(array, axis=0)  # Sum by column existance of token in row
max_val_col = np.argpartition(column_sum, -10)[-10:]  # Indexes of top 10 tokens
top_10_quantity = column_sum[max_val_col]  # Quantity of top 10 tokens
top_10_tokens = titles[max_val_col]
print(top_10_tokens)

# Display top 10 documents

print("Display top 10 documents")
row_sum = np.sum(array, axis=1)  # Amount of tokens in every document
max_val_row = np.argpartition(row_sum, -10)[-10:]  # Indexes for top 10 rows
top_10_docs_number = row_sum[max_val_row]  # Amount of tokens in every of top10 document

# Print top 10 documents
top_10_docs = []
for i in max_val_row:
    top_10_docs.append(sample[i])
print(top_10_docs)

# Display top 10 most important tokens

print("Display top 10 most important tokens")
tf_col_sum = np.sum(array_tf, axis=0)
max_tf_val_col = np.argpartition(tf_col_sum, -10)[-10:]
top_10_tf_quantity = tf_col_sum[max_tf_val_col]
top_10_tf_tokens = titles[max_tf_val_col]
print(top_10_tf_tokens)
