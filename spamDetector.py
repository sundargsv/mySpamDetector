# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:20:35 2018

@author: Sundar Gsv
"""

import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle

def make_dictionary():
    directory = "emails/"
    files = os.listdir(directory)
    
    emails = [directory + email for email in files]
    
    words = []
    count = len(emails)
    for email in emails:
        file = open(email, encoding = "ISO-8859-1")
        blob = file.read()
        words += blob.split(" ")
        print(count)
        count -= 1
        
     
    ## print(words)
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""
            
    ## Eliminate all Non - Alphabetic
    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

def make_dataset(dictionary):
    directory = "emails/"
    files = os.listdir(directory)
    
    emails = [directory + email for email in files]
    
    feature_set = []
    labels = []
    count = len(emails)
    for email in emails:
        data = []
        file = open(email, encoding = "ISO-8859-1")
        words = file.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        ## checking for whether a file is a harm/ spam in order to track it
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(count)
        count -= 1
    return feature_set, labels    

 
dictionary = make_dictionary()
feature, labels = make_dataset(dictionary)

## print(len(feature), len(labels))
        
X_train, X_test, Y_train, Y_test = tts(feature, labels, test_size = 0.2)
classifier = MultinomialNB()
classifier.fit(X_train, Y_train)
prediction = classifier.predict(X_test)

print(accuracy_score(Y_test, prediction))
clf_pickle = open("generatedModel/text-classifier.pickle", 'wb')
pickle.dump(classifier, clf_pickle)
clf_pickle.close()


""" input_features = []
inputEmail = "hey"
for word in dictionary:
    input_features.append(inputEmail.count(word[0]))
result = classifier.predict([input_features])
print(["Spam!", "Not Spam!"][result[0]])
"""    