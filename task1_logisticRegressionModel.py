import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# loading the dataset
df = pd.read_csv('Data/agaricus-lepiota.csv')

# giving each column of the dataset a name
df.columns = ['poisonous?', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment',
              'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
              'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color',
              'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']

# Dropping the 'veil-color' column since it only has one value and is therefore useless
df = df.drop('veil-color', axis=1)


# Splitting the data into features and target variables
# dropping posisonous and assign the rest of the dataframe to X
X = df.drop('poisonous?', axis=1)
# assign poisonous column to y
y = df['poisonous?']

# Convert the categorical variables of X to dummy variables using one-hot encoding, the model can't use categorical values
X = pd.get_dummies(X, columns=X.columns)

# Split the data into training, testing, and dev sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)
X_train, X_dev, y_train, y_dev = train_test_split(X_train, y_train, test_size=0.2, random_state=43)

# Train a logistic regression model with L2 regularization
model = LogisticRegression(C=0.1, penalty='l2', solver='liblinear')
model.fit(X_train, y_train)


# Making predictions on the validation, train and test sets
y_dev_pred = model.predict(X_dev)
y_test_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)



# Evaluating the accuracies
dev_accuracy = accuracy_score(y_dev, y_dev_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
train_accuracy = accuracy_score(y_train, y_train_pred)

# printing out the accuracies
print(f'Accuracy of Logistic Regression on Dev Set: {dev_accuracy}')
print(f'Accuracy of Logistic Regression on Test Set: {test_accuracy}')
print(f'Accuracy of Logistic Regression on Training Set: {train_accuracy}')