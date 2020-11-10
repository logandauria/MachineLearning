"""
Kaggle Challenge - Cleaning titanic dataset and using a decision tree classifier from sklearn
to predict survivors
@author: Logan D'Auria
@contributor: Christopher Homan
11/9/2020
"""

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import tree
from sklearn.model_selection import learning_curve

# hyper parameter for tuning decision tree
MAX_DEPTH = 3

def main():
    # download Titanic dataset and place in working directory, so that this command will find your file
    train = pd.read_csv("train.csv")
    # initialize decision tree classifier
    clf = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH)
    # Divide input data X from labeled values to predict Y
    X = train.loc[:, 'Pclass':]
    Y = train.loc[:, 'Survived']

    # Clean up the data so that it can processed by the decision tree
    X['Name'] = [len(name) for name in X['Name']]
    X['Sex'] = [0 if sex == 'male' else 1 for sex in X['Sex']]

    # assign those with a special letter ticket to a hundreds place
    X['Ticket'] = [0 if str(ticket)[0] == 'S' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [100 if str(ticket)[0] == 'A' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [200 if str(ticket)[0] == 'P' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [300 if str(ticket)[0] == 'C' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [400 if str(ticket)[0] == 'W' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [500 if str(ticket)[0] == 'L' else ticket for ticket in X['Ticket']]
    X['Ticket'] = [400 if str(ticket)[0] == 'F' else ticket for ticket in X['Ticket']]
    # catch any outliers that aren't numeric
    X['Ticket'] = [ticket if type(ticket) == int or type(ticket == float) else 0 for ticket in X['Ticket']]

    # if person does not have an assigned cabin, assign default cabin 'Z'
    X['Cabin'] = ['Z' if pd.isnull(cabin) or cabin == '' else cabin for cabin in X['Cabin']]
    # assign cabin as the ascii value of the cabin letter * 10 + the first available cabin number
    X['Cabin'] = [ord(str(cabin)[0]) * 10 if len(str(cabin)) <= 2 else ord(str(cabin)[0]) * 10 + findCabinNum(cabin) for
                  cabin in X['Cabin']]
    # assign embarked as the ascii value of given letter
    X['Embarked'] = [ord(str(embarked)[0]) for embarked in X['Embarked']]
    # fill empty spots with 0
    X = X.fillna(0)

    # train the model
    clf = clf.fit(X, Y)
    # run predictions
    clf.predict(X)

    import matplotlib.pyplot as plt
    # outputs the decision tree as a png file
    fig = plt.figure(figsize=(100, 100))
    _ = tree.plot_tree(clf, feature_names=X.columns, filled=True)
    fig.savefig("tree.png")


# finds the first number to appear in a cabin string and returns it, otherwise ret 0
def findCabinNum(cabin):
    token_list = cabin.split()
    for token in token_list:
        if len(token) > 1:
            return int(token[1:])
    return 0

main()