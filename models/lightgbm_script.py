import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load your dataset
data = pd.read_csv('data/Resampled.csv')

# Calculate the number of rows with Default=1
num_ones = len(data[data['Default'] == 1])
num_zeros = len(data[data['Default'] == 0])

# Randomly sample 50% of 1s and 0s
sampled_ones = data[data['Default'] == 1].sample(n=num_ones // 2, random_state=42)
sampled_zeros = data[data['Default'] == 0].sample(n=num_zeros // 2, random_state=42)

# Combine the selected rows to create a balanced dataset
balanced_data = pd.concat([sampled_ones, sampled_zeros])

# Define your features and target variable
X = balanced_data.drop(columns=['Ind','Default'])
y = balanced_data['Default']

# Split the data into training and testing sets (70:30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create LightGBM datasets for train and test
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Set hyperparameters
params = {
    "objective": "binary",
    "metric": "binary_logloss",
    "boosting_type": "gbdt",
    "num_leaves": 31,
    "learning_rate": 0.05,
    "feature_fraction": 0.9,
}

# Train the LightGBM model
num_round = 100
bst = lgb.train(params, train_data, num_round, valid_sets=[test_data])

# Get probabilistic predictions on the test set
y_test_prob = bst.predict(X_test, num_iteration=bst.best_iteration)

# Calculate evaluation metrics for the test set
test_accuracy = accuracy_score(y_test, (y_test_prob >= 0.5).astype(int))
test_precision = precision_score(y_test, (y_test_prob >= 0.5).astype(int))
test_recall = recall_score(y_test, (y_test_prob >= 0.5).astype(int))
test_f1 = f1_score(y_test, (y_test_prob >= 0.5).astype(int))
print("Test Set Metrics:")
print(f"Accuracy: {test_accuracy}")
print(f"Precision: {test_precision}")
print(f"Recall: {test_recall}")
print(f"F1 Score: {test_f1}")

# Add probabilities to the test set DataFrame
test_set_with_probs = X_test.copy()
test_set_with_probs['Prediction'] = (y_test_prob >= 0.5).astype(int)
test_set_with_probs['Prob_0'] = 1 - y_test_prob
test_set_with_probs['Prob_1'] = y_test_prob
test_set_with_probs['Default'] = y_test  # Add 'Default' back

# Save the test set with probabilities to a CSV file
test_set_with_probs.to_csv('models/test.csv', index=False)

# Create a test set with remaining 0s and 1s
unseen_X = data.loc[~data.index.isin(balanced_data.index)].drop(columns=['Ind','Default'])
unseen_y = data.loc[~data.index.isin(balanced_data.index)]['Default']

# Make predictions on the unseen test set
unseen_test_prob = bst.predict(unseen_X, num_iteration=bst.best_iteration)

# Calculate evaluation metrics for the unseen test set
unseen_test_accuracy = accuracy_score(unseen_y, (unseen_test_prob >= 0.5).astype(int))
unseen_test_precision = precision_score(unseen_y, (unseen_test_prob >= 0.5).astype(int))
unseen_test_recall = recall_score(unseen_y, (unseen_test_prob >= 0.5).astype(int))
unseen_test_f1 = f1_score(unseen_y, (unseen_test_prob >= 0.5).astype(int))

# Add probabilities to the unseen test set DataFrame
unseen_test_set_with_probs = unseen_X.copy()
unseen_test_set_with_probs['Prediction'] = (unseen_test_prob >= 0.5).astype(int)
unseen_test_set_with_probs['Prob_0'] = 1 - unseen_test_prob
unseen_test_set_with_probs['Prob_1'] = unseen_test_prob
unseen_test_set_with_probs['Default'] = unseen_y  # Add 'Default' back

# Save the unseen test set with probabilities to a CSV file
unseen_test_set_with_probs.to_csv('models/unseen_test.csv', index=False)

# Create DataFrames for metrics
test_metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Value": [test_accuracy, test_precision, test_recall, test_f1]
})

unseen_test_metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Value": [unseen_test_accuracy, unseen_test_precision, unseen_test_recall, unseen_test_f1]
})

# Save metrics to CSV files
test_metrics.to_csv('models/test_metrics.csv', index=False)
unseen_test_metrics.to_csv('models/unseen_test_metrics.csv', index=False)
print("\nUnseen Test Set Metrics:")
print(f"Accuracy: {unseen_test_accuracy}")
print(f"Precision: {unseen_test_precision}")
print(f"Recall: {unseen_test_recall}")
print(f"F1 Score: {unseen_test_f1}")