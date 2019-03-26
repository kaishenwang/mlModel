import pandas
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection

# load dataset
training_file = sys.argv[1]
dataframe = pandas.read_csv(training_file)

# split into labels and features, assuming labels are in first column
array = dataframe.values
XT = array[:18000,1:len(array[0])]
YT = array[:18000,0]
XV = array[18000:,1:len(array[0])]
YV = array[18000:,0]
X = array[:,1:len(array[0])]
Y = array[:,0]
# prepare random seed for cross validation test harness
seed = 7
clf = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=0)
clf.fit(XT, YT)

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
feat_labels = dataframe.columns[1:]
for f in range(XT.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))
YG = clf.predict(XV)

for i in range(len(YG)):
    if YV[i] != YG[i]:
        print ("At %d get %d instead of %d"%(i+18002, YG[i], YV[i]))
for score in ['accuracy', 'precision', 'recall']:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    clf2 = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=0)
    cv_results = model_selection.cross_val_score(clf2, X, Y, cv=kfold, scoring=score)
    msg = "%s: %f (%f)" % (score, cv_results.mean(), cv_results.std())
    print (msg)
