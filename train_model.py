import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# load dataset
data = pd.read_csv("dataset.csv")

# features and target
X = data.drop("target", axis=1)
y = data["target"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")