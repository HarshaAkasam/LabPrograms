# SVM on Heart Disease dataset (UCI - processed from sklearn's heart dataset substitute)
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__=='__main__':
    # Use sklearn's breast_cancer dataset as substitute if heart not available; interface is same demo
    data = datasets.load_breast_cancer()  # substitute; replace with heart CSV for real task
    X = data.data; y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1)
    clf = svm.SVC(kernel='rbf', C=1.0)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print('SVM accuracy:', accuracy_score(y_test, preds))
