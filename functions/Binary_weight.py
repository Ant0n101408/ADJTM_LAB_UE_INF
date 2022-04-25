from services.text_tokenizer import text_tokenizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def Binary_weight(sample):
    vectorizer = CountVectorizer(tokenizer=text_tokenizer, binary=True)
    X_transform_sample = vectorizer.fit_transform(sample)
    titles = (vectorizer.get_feature_names_out())
    array = X_transform_sample.toarray()

    column_sum = np.sum(array, axis=0)
    max_val_col = np.argpartition(column_sum, -10)[-10:]
    top_10_quantity = column_sum[max_val_col]
    top_10_tokens = titles[np.argpartition(column_sum, -10)[-10:]]

    df = pd.DataFrame({'titles': top_10_tokens, 'quantity': top_10_quantity})
    df = df.sort_values(by="quantity")
    plot = df.plot(kind='barh', x='titles', y='quantity', title="Crucial tokens based on binary weight")
    fig = plot.get_figure()
    fig.savefig('./images/Binary_weight.png')
    plt.show()

    print(tabulate(df, headers='keys', tablefmt='psql'))

    return
