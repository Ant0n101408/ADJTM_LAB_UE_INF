
# pip install sklearn
# pip install nltk

import pandas as pd


from functions import True_without_Fake, Fake_without_True, TF_IDF, Binary_weight

dataset_true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])  # Read file
dataset_fake = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])

sample_true = dataset_true['title']  # Take a sample of data
sample_fake = dataset_fake['title']

True_without_Fake.True_without_fake(sample_true, sample_fake)
# Fake_without_True.Fake_without_true(sample_true, sample_fake)
# TF_IDF.TF_IDF(sample_fake)
# Binary_weight.Binary_weight(sample_fake)
