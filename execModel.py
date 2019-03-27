import pandas
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection

# load training dataset
training_file = 'data.csv'
dataframe = pandas.read_csv(training_file)
# split into labels and features, assuming labels are in first column
array = dataframe.values
X = array[:,1:len(array[0])]
Y = array[:,0]
# prepare random seed for cross validation test harness
seed = 7
clf = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=0)
clf.fit(X, Y)
# output feature importance
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
feat_labels = dataframe.columns[1:]
for f in range(X.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))

# apply model
dataframe = pandas.read_csv('fullDataPrepared.csv')
array = dataframe.values
predictRes = clf.predict(array[:,1:len(array[0])])
print('Finish predicting.')
with open('predictionResult.txt', 'w') as f:
    for i in predictRes:
        f.write(str(i) + '\n')
