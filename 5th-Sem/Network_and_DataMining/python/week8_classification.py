"""Week 8: Classification using Decision Tree (ID3/J48 analogue), Naive Bayes, k-NN.
Computes entropy, kappa, confusion matrix, and ROC curves on Iris dataset.
"""
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, cohen_kappa_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt

def entropy_of_labels(y):
    probs = np.bincount(y) / len(y)
    probs = probs[probs>0]
    return -np.sum(probs * np.log2(probs))

def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    print("Entropy of target:", entropy_of_labels(y))
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
    dt = DecisionTreeClassifier(criterion='entropy', random_state=1) # ID3-like
    dt.fit(X_train,y_train)
    print("Decision tree rules:\n", export_text(dt, feature_names=iris.feature_names))
    y_pred_dt = dt.predict(X_test)
    print("Confusion matrix (DT):\n", confusion_matrix(y_test,y_pred_dt))
    print("Kappa (DT):", cohen_kappa_score(y_test,y_pred_dt))
    # Naive Bayes
    nb = GaussianNB()
    nb.fit(X_train,y_train)
    y_pred_nb = nb.predict(X_test)
    print("Confusion matrix (NB):\n", confusion_matrix(y_test,y_pred_nb))
    print("Kappa (NB):", cohen_kappa_score(y_test,y_pred_nb))
    # k-NN
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train,y_train)
    y_pred_knn = knn.predict(X_test)
    print("Confusion matrix (k-NN):\n", confusion_matrix(y_test,y_pred_knn))
    print("Kappa (k-NN):", cohen_kappa_score(y_test,y_pred_knn))
    # ROC curves (one-vs-rest)
    y_test_b = label_binarize(y_test, classes=[0,1,2])
    y_score_dt = dt.predict_proba(X_test)
    fpr = dict(); tpr = dict(); roc_auc = dict()
    for i in range(3):
        fpr[i], tpr[i], _ = roc_curve(y_test_b[:,i], y_score_dt[:,i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    # plot ROC for class 0..2
    for i in range(3):
        plt.plot(fpr[i], tpr[i], label=f'class {i} (AUC = {roc_auc[i]:.2f})')
    plt.plot([0,1],[0,1],'k--')
    plt.xlabel('FPR'); plt.ylabel('TPR'); plt.legend()
    plt.title('ROC curves (Decision Tree)')
    plt.savefig('week8_roc_dt.png')
    print('ROC curve saved to week8_roc_dt.png')

if __name__=='__main__':
    main()
