
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

dataset = pd.read_csv('BreastCancer.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=0, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)

y_pred = classifier.predict(x_test)
y_pred[0:10]


comparison = np.concatenate((y_test.reshape(-1,1), y_pred.reshape(-1,1)), axis = 1)
comparison[0:10,:]



cm = confusion_matrix(y_test, y_pred)
print(cm)



plot_confusion_matrix(classifier, x_test, y_test)
plt.xlabel("Predicted tumor class")
plt.ylabel("True tumor class")
plt.show()


accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))



cancer = pd.read_csv("BreastCancer.csv")

cancer = cancer.drop('Id',axis=1)

le = preprocessing.LabelEncoder()

cancer.Class = le.fit_transform(cancer.Class)
x = cancer.iloc[:, :-1].values
y = cancer.iloc[:, 4].values
plt.scatter(x[:,0], x[:, 3], c=y, cmap ='flag')
plt.xlabel('True tumor class')
plt.ylabel('Prdicted tumor class')
plt.show()
