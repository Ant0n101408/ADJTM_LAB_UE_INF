import txt_cleaning
import stop_words
import stemming

text = '''
 Donald Trump Sends Out Embarrassing New Year€™s Eve Message; 
 This is Disturbing,"Donald Trump just couldn t wish all Americans a Happy New Year and leave it at that. 
 Instead, he had to give a shout out to his enemies, haters and  the very dishonest fake news media.  
 The former reality show star had just one job to do and he couldn t do it. 
 As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, 
 and even the very dishonest Fake News Media, a Happy and Healthy New Year,  President Angry Pants tweeted.  
 2018 will be a great year for America!'''


cleaned_text = txt_cleaning.clean_text(text)
without_stopwords = stop_words.stopwords_function(cleaned_text)
stemmed_txt = stemming.stemming_function(without_stopwords)
print(text)
print(cleaned_text)
print(without_stopwords)
print(stemmed_txt)