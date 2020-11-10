# Introduction
the file "tree_learn.py" is an implementation of the titanic data set challenge by Kaggle.com   
the initial dataset can be viewed in the file "train.csv"   
the resulting decision tree can be viewed in the file "tree.png"

## Data Cleaning Implementation
Data was necessary because sklearn's decision tree function only accepts nominal values. Many of the data fields contained Strings that needed to be adjusted. Here is a list of adjustments I made to the data

I kept the name feature as is, because I did not feel I could get any extra information off of unique strings when age and gender were already accounted for.   
I changed ticket information if it contained any letters to be at a hundredths place corresponding with the letter (A=100,O=200, etc)   
I changed the cabin information to be the ascii value of the first letter * 10 + the first available number if there was one. This way all of the cabins of similar letters are grouped together    
I changed the embarked feature to represent the ascii value of the character so that the data set can account for any amount of unique characters.    
