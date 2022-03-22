# pip install -U nltk
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def stopwords_function(text: str) -> str:
    stop_words = stopwords.words('english')
    word_token = word_tokenize(text)
    cleaned = [x for x in word_token if x not in stop_words]
    return " ".join(cleaned)
