from services import stemming, stop_word, txt_cleaning
from nltk.tokenize import word_tokenize


def text_tokenizer(text: str):

    cleaned_text = txt_cleaning.clean_text(text)
    tokens = word_tokenize(cleaned_text)
    without_stopwords = stop_word.stopwords_function(tokens)
    stemmed_text = stemming.stemming_function(without_stopwords)

    return [w for w in stemmed_text if len(w) > 3]