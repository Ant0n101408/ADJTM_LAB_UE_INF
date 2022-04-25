from services.text_tokenizer import text_tokenizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def TF_IDF(sample):
    vectorizer_tf = TfidfVectorizer(tokenizer=text_tokenizer)
    X_transform_sample_tf = vectorizer_tf.fit_transform(sample)
    titles = (vectorizer_tf.get_feature_names_out())
    array_tf = X_transform_sample_tf.toarray()

    # Display top 10 most important tokens

    print("Display top 10 most important tokens")
    tf_col_sum = np.mean(array_tf, axis=0)
    max_tf_val_col = np.argpartition(tf_col_sum, -10)[-10:]
    top_10_tf_quantity = tf_col_sum[max_tf_val_col]
    top_10_tf_tokens = titles[max_tf_val_col]
    print(top_10_tf_tokens)

    # ''' Bar plot of TF-IDF indexes top 10 most important tokens in true news'''

    df_2 = pd.DataFrame({'titles': top_10_tf_tokens, 'TFIDF': top_10_tf_quantity})
    df_2 = df_2.sort_values(by="TFIDF")
    plot2 = df_2.plot(kind='barh', x='titles', y='TFIDF', title="Kluczowe tokeny wiadomości na podstawie miary TF-IDF")
    fig2 = plot2.get_figure()
    fig2.savefig('./images/TF_IDF.png')
    plt.show()
    print(tabulate(df_2, headers='keys', tablefmt='psql'))  # Pretty table

    return
