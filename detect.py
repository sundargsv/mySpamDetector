# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:20:35 2018

@author: Sundar Gsv
"""

import os
import pickle
from collections import Counter





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

dictionary = make_dictionary()
list_unpickle = open("generatedModel/text-classifier.pickle", 'rb')
classifier = pickle.load(list_unpickle)


features = []
inputEmail = "Hi"
for word in dictionary:
    features.append(inputEmail.count(word[0]))
    
result = classifier.predict([features])
print(result[0])
print(["Not Spam", "Spam!"][result[0]])

 
    