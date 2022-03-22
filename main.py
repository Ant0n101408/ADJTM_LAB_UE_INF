from models import bow, stemming, stop_word, txt_cleaning, utils
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# read file
file = utils.readfile(r'D:\Antoni\UE\Text_mining\Lab3\Fake.csv')

# cleaning text from punctuation, numbers, html, whitespaces
cleaned_text = txt_cleaning.clean_text(file)

# cleaning text from stop words
without_stopwords = stop_word.stopwords_function(cleaned_text)

# stemming text
stemmed_txt = stemming.stemming_function(without_stopwords)

# creating Bag Of Words
bow_txt = bow.create_bow(stemmed_txt)

# creating Word Cloud
wordcloud = WordCloud(colormap='Spectral').generate_from_frequencies(bow_txt)
plt.figure(figsize=(8, 10), facecolor='w')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("wordcloud_fake.jpg")
plt.show()
