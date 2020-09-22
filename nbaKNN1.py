# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from Nba_Clean_df import df_nba_west
from Nba_Clean_df import df_nba_east
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import sklearn.preprocessing
import matplotlib.pyplot as plt
import seaborn as sns



# Since we have discereet labels, we will use a classification algorithm
# For this, We are going to use sklearn's K Nearest Neighbors Algorithm



predict = df_nba_west["In_Playoffs"]


X = df_nba_west.iloc[:, 2:-3].values


y = df_nba_west["In_Playoffs"].values





# %%

df_nba_west.iloc[:, 2:-3].columns


# %%
west_corr = df_nba_west.corr()
sns.heatmap(west_corr)


# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)


# %%
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)



from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)



from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))



acc = classifier.score(X_test, y_test)
print(acc)



names = ["Made Playoffs", "Didn't Make Playoffs"]



#Function from Youtube channel 

for x in range(len(y_pred)):
    print(list(df_nba_west["Team"])[x], "Predicted: ", names[y_pred[x]], "Data : ", X_test[x], "Real : ", names[y_test[x]])
    n = classifier.kneighbors([X_test[x]], 5, True)
    print("N: ", n)




