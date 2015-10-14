from numpy import genfromtxt
from sklearn import linear_model


import numpy as np

my_data = genfromtxt('data/OnlineNewsPopularity/OnlineNewsPopularity.csv', delimiter=',')

# print my_data[1]

data = [i[1:-1] for i in my_data[1:-1]]

#Y is at [-1]


np.random.shuffle(data)

n = len(data)

f = 0.15 #eliminate non zero from linear
t = 0.40


# X = [i[0:-2] for i in data]
# Y = [i[-1] for i in data]


# xtrain = X[:int(f*n)]
# ytrain = Y[:int(f*n)]


# regr = linear_model.LinearRegression()

# regr.fit(xtrain,ytrain)


# dt = []
# for i in data:
# 	a = []
# 	for c in range(len(regr.coef_)):
# 		if regr.coef_[c]>0:
# 			a.append(i[c])
# 	dt.append(a)

# data = np.array(dt)

# np.random.shuffle(data)



X = [i[0:-2] for i in data]
Y = [i[-1] for i in data]

xtrain = X[:int(t*n)]
xtest = X[int(t*n):]

ytrain = Y[:int(t*n)]
ytest = Y[int(t*n):]

regr = linear_model.Ridge()
	
regr.fit(xtrain,ytrain)

print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(xtest) - ytest) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(xtest, ytest))