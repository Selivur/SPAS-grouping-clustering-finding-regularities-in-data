# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV

BreastCancer = pd.read_csv("BreastCancer.csv", sep=',')
color_wheel={
    0:"r",
    1:"g"}
colors=BreastCancer["Class"].map(lambda x: color_wheel.get(x))
scatter_matrix(BreastCancer, color=colors)
plt.show()
BreastCancer_size=BreastCancer.iloc[:,:-1].values
BreastCancer_class=BreastCancer.iloc[:,10].values
classifier=LogisticRegression(C=100, random_state=1, solver='lbfgs', multi_class='ovr')
classifier.fit(BreastCancer_size,BreastCancer_class)
new_size=[[1000026,5,1,6,4,5,6,6,7,2],
          [1000027,5,1,1,1,5,3,6,9,2],
          [1000024,5,1,6,4,5,4,6,5,2]]
class_predict = classifier.predict(new_size)
new_BreastCancer=pd.DataFrame(new_size)
new_BreastCancer["10"]=class_predict
new_BreastCancer.columns=BreastCancer.columns
Size_train, Size_test,Class_train,Class_test=\
train_test_split(BreastCancer_size,BreastCancer_class, test_size=0.3)
scaler=StandardScaler()
scaler.fit(Size_train)
Size_train=scaler.transform(Size_train)
Size_test=scaler.transform(Size_test)
Size_new_scaler= scaler.transform(new_size)
classifier_linear=LogisticRegressionCV()
classifier_linear.fit(Size_train,Class_train)
test_predict=classifier_linear.predict(Size_test)
score_linear=classifier_linear.score(Size_test,Class_test)
print("correct predictions= ",score_linear,"\n")
cm= confusion_matrix(Class_test,test_predict)
disp= ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classifier_linear.classes_)
disp.plot()
plt.show()
print(classification_report(Class_test,test_predict),"\n")
new_BreastCancer["New"]=classifier_linear.predict(Size_new_scaler)

