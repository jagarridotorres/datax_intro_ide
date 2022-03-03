
import time

start = time.time()

from sklearn.datasets import make_blobs
from sklearn.model_selection import LeaveOneOut
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Create dataset.
X, y = make_blobs(n_samples=100, random_state=1)

# Leave-one-Out cross-validation using sklearn.
cv = LeaveOneOut()

# Enumerate splits.
y_true, y_pred = list(), list()
for train_ix, test_ix in cv.split(X):
    # Split data
    X_train, X_test = X[train_ix, :], X[test_ix, :]
    y_train, y_test = y[train_ix], y[test_ix]
    # Fit model
    model = GradientBoostingClassifier(random_state=1)
    model.fit(X_train, y_train)
    # Evaluate model
    yhat = model.predict(X_test)
    # Store splits
    y_true.append(y_test[0])
    y_pred.append(yhat[0])

# Calculate accuracy.
acc = accuracy_score(y_true, y_pred)
print('Accuracy: %.3f' % acc)
end = time.time()

print(f" Elapsed time: {end - start}.")
