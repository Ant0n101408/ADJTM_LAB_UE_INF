from services.text_tokenizer import text_tokenizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def True_without_fake(sample_true, sample_fake):
    vectorizer1 = CountVectorizer(tokenizer=text_tokenizer)

    X_transform_sample_true = vectorizer1.fit_transform(sample_true)
    titles_true = (vectorizer1.get_feature_names_out())

    X_transform_sample_fake = vectorizer1.fit_transform(sample_fake)
    titles_fake = (vectorizer1.get_feature_names_out())

    true_minus_false = [x for x in titles_true if x not in titles_fake]

    vectorizer = CountVectorizer(tokenizer=text_tokenizer, vocabulary=true_minus_false)
    X_transform_sample = vectorizer.fit_transform(sample_true)

    titles = (vectorizer.get_feature_names_out())  # Get all tokens
    print(titles)
    array = X_transform_sample.toarray()
    print(array)  # Table [1,0,0....] is token in document

    """
    Jeśli do vectorizera liczebnościowego przekażemy jedynie jeden dokument, to jakie
    wartości będzie miała otrzymana macierz? Albo jakich nie będzie miała?

    Odpowiedz: Nie będzie miała zer.
    """

    """
    Display top 10 tokens
    """
    print("Display top 10 tokens")
    column_sum = np.sum(array, axis=0)  # Sum by column existance of token in row
    max_val_col = np.argpartition(column_sum, -10)[-10:]  # Indexes of top 10 tokens
    top_10_quantity = column_sum[max_val_col]  # Quantity of top 10 tokens
    top_10_tokens = titles[max_val_col]
    print(top_10_tokens)

    """
    Display top 10 documents
    """
    print("Display top 10 documents")
    row_sum = np.sum(array, axis=1)  # Amount of tokens in every document
    max_val_row = np.argpartition(row_sum, -10)[-10:]  # Indexes for top 10 rows
    top_10_docs_number = row_sum[max_val_row]  # Amount of tokens in every of top10 document

    # Bar plot of quantity top 10 tokens in true news

    df_1 = pd.DataFrame({'titles': top_10_tokens, 'quantity': top_10_quantity})
    df_1 = df_1.sort_values(by="quantity")
    plot = df_1.plot(kind='barh', x='titles', y='quantity',
                     title="Top 10 tytułów występujących tylko w prawdziwych wiadomościach")
    fig = plot.get_figure()
    fig.savefig('./images/true_without_fake.png')
    plt.show()

    print(tabulate(df_1, headers='keys', tablefmt='psql'))  # Pretty table

    return
