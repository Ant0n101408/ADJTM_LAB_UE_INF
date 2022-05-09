# pip install sklearn
# pip install nltk
# pip install -U scikit-learn

import pandas as pd
from sklearn import metrics, __all__
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from functions import True_without_Fake, Fake_without_True, TF_IDF, Binary_weight
from services.text_tokenizer import text_tokenizer
from services.vectorizing import vectorizing, vectorizing_voc

dataset_true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])  # Read file
dataset_true['True'] = 1
dataset_fake = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])
dataset_fake['True'] = 0

together_dataset = pd.concat([dataset_true, dataset_fake]).sample(10000)
# print(together_dataset)
together_dataset_vector, together_dataset_titles = vectorizing(together_dataset['title'])

X_train, X_test, y_train, y_test = train_test_split(together_dataset['title'], together_dataset["True"], test_size=0.33,
                                                    random_state=42)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

X_train_vector, X_train_titles = vectorizing_voc(X_train, together_dataset_titles)
# print(X_train_vector)
# print(X_train_titles)
X_test_vector, X_test_titles = vectorizing_voc(X_test, together_dataset_titles)
# print(X_test_vector)
# print(X_test_titles)

DTC = DecisionTreeClassifier()
DTC.fit(X_train_vector, y_train)
y_pred = DTC.predict(X_test_vector)
print("Accuracy DTC:", metrics.accuracy_score(y_test, y_pred))
print("Accuracy another way:", DTC.score(X_test_vector, y_test))

RFC = RandomForestClassifier()
RFC.fit(X_train_vector, y_train)
y_pred = RFC.predict(X_test_vector)
print("Accuracy RFC:", metrics.accuracy_score(y_test, y_pred))
print("Accuracy another way:", RFC.score(X_test_vector, y_test))
#
#
svc = SVC()
svc.fit(X_train_vector, y_train)
# y_pred=SVC.predict(X_test_vector)
# print("Accuracy SVC:",metrics.accuracy_score(y_test, y_pred))
print("Accuracy SVC another way:", svc.score(X_test_vector, y_test))

ABC = AdaBoostClassifier()
ABC.fit(X_train_vector, y_train)
y_pred = ABC.predict(X_test_vector)
print("Accuracy ABC:", metrics.accuracy_score(y_test, y_pred))
print("Accuracy another way:", ABC.score(X_test_vector, y_test))

BC = BaggingClassifier()
BC.fit(X_train_vector, y_train)
y_pred = BC.predict(X_test_vector)
print("Accuracy BC:", metrics.accuracy_score(y_test, y_pred))
print("Accuracy another way:", BC.score(X_test_vector, y_test))

# sample_true = dataset_true['title'][:10]  # Take a sample of data
# sample_fake = dataset_fake['title'][:10]


# True_without_Fake.True_without_fake(sample_true, sample_fake)
# Fake_without_True.Fake_without_true(sample_true, sample_fake)
# TF_IDF.TF_IDF(sample_fake)
# Binary_weight.Binary_weight(sample_fake)

# dataset = pd.read_csv('./data/Mgr.csv', usecols=['tekst'])
# sample = dataset['tekst']
# TF_IDF.TF_IDF(sample)
# Binary_weight.Binary_weight(sample)
