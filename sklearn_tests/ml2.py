from sklearn import datasets, neighbors, linear_model,svm
import numpy as np 

# dataset = datasets.load_digits()
dataset = datasets.load_iris()
data = [dataset.data,dataset.target]



dt = []
for i in range(len(dataset.data)):
	t = list(dataset.data[i])
	t.append( dataset.target[i])
	dt.append(t)
data = np.array(dt)

np.random.shuffle(data)
X = [i[:-1] for i in data]
Y = [i[-1] for i in data]

xtrain = X[:-10]
ytrain = Y[:-10]

xtest = X[-10:]
ytest = Y[-10:]


print "kn"
learner = neighbors.KNeighborsClassifier()
learner.fit(xtrain,ytrain)
print learner.score(xtest,ytest)

print "linear"
# learner = linear_model.LinearRegression()
learner = linear_model.LinearRegression()
learner.fit(xtrain,ytrain)
print learner.score(xtest,ytest)
# print learner.predict(xtest)

print "svm "

learner = svm.SVC(kernel='rbf')
learner.fit(xtrain,ytrain)
print learner.score(xtest,ytest)

