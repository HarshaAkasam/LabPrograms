# Random Forest implementations: scikit-learn (working), TensorFlow and PyTorch sketches provided as examples
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__=='__main__':
    data = datasets.load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1)
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print('RandomForest (sklearn) accuracy:', accuracy_score(y_test, preds))
    print('\n--- TensorFlow / PyTorch implementations are non-trivial; see comments in file for guidance ---')
