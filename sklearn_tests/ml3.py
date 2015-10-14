from sklearn import datasets, neighbors, linear_model,svm,cross_validation
import numpy as np 

dataset = datasets.load_digits()
# dataset = datasets.load_iris()
data = [dataset.data,dataset.target]



dt = []
for i in range(len(dataset.data)):
	t = list(dataset.data[i])
	t.append( dataset.target[i])
	dt.append(t)
data = np.array(dt)

np.random.shuffle(data)
X = np.array([i[:-1] for i in data])
y = np.array([i[-1] for i in data])



svc = svm.SVC(kernel='linear')
C_s = np.logspace(-10, 0, 10)

a = []

for C in C_s:
	svc.C = C
	s = cross_validation.cross_val_score(svc,X,y,n_jobs=1)
	a.append((np.mean(s),np.std(s)))

print a