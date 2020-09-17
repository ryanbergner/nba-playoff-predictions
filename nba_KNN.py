from Nba_Clean_df import df_nba_west
from Nba_Clean_df import df_nba_east
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import sklearn.preprocessing


# Since we have discereet labels, we will use a classification algorithm
# For this, We are going to use sklearn's K Nearest Neighbors Algorithm

# Help from youtube channel: Programming Knowledge KNN Implementation

#MUST DELETE "TEAMS" Column 


predict = df_nba_west["In_Playoffs"]


X = df_nba_west.iloc[:, :-3]


y = df_nba_west.iloc[:, -2]



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .0204)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)


from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))