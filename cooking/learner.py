
import json
from pprint import pprint
import numpy as np

with open('data/train.json') as data_file:    
    data = json.load(data_file)

X = []
y = []
# print data[0]
for i in data:
	s = "" 
	for j in i['ingredients']:
		s+= j + " "
	X.append(s)
	y.append(i['cuisine'])


#making the bag of words. 
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
vectorizer.fit(X)
X_bag = vectorizer.fit_transform(X)

# from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn import svm
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
# clf = svm.SVC(kernel='linear', C=1)

clf = MultinomialNB()
# scores = cross_validation.cross_val_score(clf, X_bag, y, cv=3)

# print scores
clf.fit(X_bag,y)



#Produce the output. 

with open('data/test.json') as data_file:    
    data = json.load(data_file)

X = []
ids = []
# print data[0]
for i in data:
	s = "" 
	for j in i['ingredients']:
		s+= j + " "
	X.append(s)
	ids.append(i['id'])

print np.shape(X_bag[0])

#making the bag of words. 
X_bag = vectorizer.transform(X)

# print np.shape(X_bag[0])

p = clf.predict(X_bag)

import csv
predictions_file = open("output.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["id","cuisine"])
open_file_object.writerows(zip(ids, p))
predictions_file.close()