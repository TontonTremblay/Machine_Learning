def raw_input_fnc():
    d = open("input.in")
    for i in d:
        yield i

# def check_output(r):
#     d = open("output.out")
#     i = 0
#     for l in d:

#         if not r[i] == l.replace("\n",""):
#             print i
#             print l
#             print r[i]
#             break 
#         i+=1

#g.next() -> raw_input()
g = raw_input_fnc()
raw_input = g.next

###Start of the code here!!!

t = open('trainingdata.txt')

import numpy as np


X = []
y = []
for i,l in enumerate(t):
    # if i is 0:
    #     continue
    
    s = l[0:-3]
    a = s.split(",")

    # print len(a)
    # s1,s2 = "",""
    # for i in a[:5]:
    #     s1 += i +' '
    # for i in a[5:-1]:
    #     s2 += i +' '
    # X.append([s1,s2])       
    X.append(a)
    X.append(a[5:]+a[:5])

    # print X[0]
    # print X[1]
    # quit()
    
    y.append(int(l[-2]))
    if y[-1] is 1:
        y.append(2)
    else:
        y.append(1)

uniqueNames =  np.unique(X)

dictpos = dict()
for i in range(len(uniqueNames)):
    dictpos[uniqueNames[i]]=i

X_new = []

for v in X:
    a = [0 for i in range(len(uniqueNames)*2)]
    for h in v[:5]:
        a[dictpos[h]] = 1
    for h in v[5:]:
        a[len(uniqueNames)+dictpos[h]] = 1
    X_new.append(a)




# X = []
# y = []
# for i,l in enumerate(t):
#     # if i is 0:
#     #     continue
    
#     s = l[0:-3]
#     a = s.split(",")

#     # print len(a)
#     # s1,s2 = "",""
#     # for i in a[:5]:
#     #     s1 += i +' '
#     # for i in a[5:-1]:
#     #     s2 += i +' '
#     # X.append([s1,s2])       
#     X.append(a)
#     # print X
#     # quit()
    
#     y.append(int(l[-2]))

# a =  np.unique(X)

# nameValue = dict()

# for i in range(len(a)):
#     if 
#     nameValue[a[i]] = 1 

# X_new = []

# for i in X:
#     at = []
#     for v in i :
#         at.append(nameValue[v])
#     X_new.append(at)



# # from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
# # from sklearn.feature_extraction.text import CountVectorizer

# # print X[0]

# # count_vect = CountVectorizer()
# # X_train_counts = count_vect.fit_transform(X)


from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn import cross_validation
from sklearn import linear_model
from sklearn.linear_model import SGDClassifier
# from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
# # clf = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
# clf = SVC(kernel="linear", C=0.025)
# clf = linear_model.LogisticRegression()
# clf = GaussianNB()
clf = KNeighborsClassifier(2)
# this_scores = cross_validation.cross_val_score(clf, X_new, y, n_jobs=1,cv = 10)
# print this_scores
clf.fit(X_new, y)

n = int(raw_input())
totest = []
for i in range(n):
    t = raw_input().replace('\n','').split(",")

    a = [0 for i in range(len(uniqueNames)*2)]
    for h in t[:5]:
        a[dictpos[h]] =1
    for h in t[5:]:
        a[len(uniqueNames)+dictpos[h]] =1
    totest.append(a)


for i in clf.predict(totest):
    print i

