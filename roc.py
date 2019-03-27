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
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.5,
                                                    random_state=0)

clf = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=7)
classifier = OneVsRestClassifier(clf)
y_score = classifier.fit(X_train, y_train).decision_function(X_test)
plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Detect Parked Domain using Random Forest')
plt.legend(loc="lower right")
plt.savefig('/home/kwang40/mlModel/roc.png', dpi=500)
