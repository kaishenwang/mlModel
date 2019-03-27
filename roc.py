from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
import pandas
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import matplotlib.pyplot as plt
from itertools import cycle

# load dataset
training_file = sys.argv[1]
dataframe = pandas.read_csv(training_file)

# split into labels and features, assuming labels are in first column
array = dataframe.values
X = array[:,1:len(array[0])]
Y = array[:,0]
y = label_binarize(Y, classes=[0,1])
n_classes = y.shape[1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.5,
                                                    random_state=7)

clf = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=7)
classifier = OneVsRestClassifier(clf)
y_score = classifier.fit(X_train, y_train).predict_proba(X_test)
#print(len(X_test))
#print(y_score)
y_score = [x[1] for x in y_score]
fpr = {}
tpr = {}
roc_auc = {}
# Compute micro-average ROC curve and ROC area
fpr[0], tpr[0], _ = roc_curve(y_test.ravel(), y_score)
roc_auc[0] = auc(fpr[0], tpr[0])
plt.figure()
lw = 2
plt.plot(fpr[0], tpr[0], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[0])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Detect Parked Domain using Random Forest')
plt.legend(loc="lower right")
plt.savefig('/home/kwang40/mlModel/roc.png', dpi=500)
