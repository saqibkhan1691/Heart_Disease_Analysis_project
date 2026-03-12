import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from xgboost import XGBClassifier


# STEP 1: Load Cleaned Dataset
df = pd.read_csv("data/heart_data_clean_preprocessed.csv")

# STEP 2: Separate Features & Target
X = df.drop(["HeartDisease", "Sex"], axis=1)
y = df["HeartDisease"]

# Save feature names
joblib.dump(X.columns.tolist(), "models/feature_names.pkl")

# Save feature means
joblib.dump(X.mean().to_dict(), "models/feature_means.pkl")

# STEP 3: Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scale_pos_weight = len(y_train[y_train == 0]) / len(y_train[y_train == 1])

# STEP 4: Define Models
models = {
    "Logistic Regression": LogisticRegression(class_weight="balanced", max_iter=1000),
    "Random Forest": RandomForestClassifier(class_weight="balanced", n_estimators=200),
    "XGBoost": XGBClassifier(
        scale_pos_weight=scale_pos_weight,
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        eval_metric="logloss"
    )
}

best_model = None
best_score = 0
best_model_name = ""

# STEP 5: Train & Compare
for name, model in models.items():

    model.fit(X_train, y_train)

    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = model.predict(X_test)

    roc = roc_auc_score(y_test, y_prob)

    print(f"\n{name}")
    print("ROC-AUC:", round(roc, 4))
    print(classification_report(y_test, y_pred))

    if roc > best_score:
        best_score = roc
        best_model = model
        best_model_name = name


print("\nBest Model Selected:", best_model_name)
print("Best ROC-AUC:", round(best_score, 4))


# STEP 6: Calibrate Best Model
calibrated_model = CalibratedClassifierCV(best_model, method='isotonic', cv=5)
calibrated_model.fit(X_train, y_train)

best_model = calibrated_model


# STEP 7: Find Optimal Threshold
y_prob_best = best_model.predict_proba(X_test)[:, 1]

best_threshold = 0
best_f1 = 0

for threshold in np.arange(0.05, 0.5, 0.01):

    preds = (y_prob_best >= threshold).astype(int)
    score = f1_score(y_test, preds)

    if score > best_f1:
        best_f1 = score
        best_threshold = threshold


print("Best Threshold:", round(best_threshold, 3))
print("Best F1 Score:", round(best_f1, 4))



# STEP 8: Save Final Model Bundle
joblib.dump(
    {
        "model": best_model,
        "threshold": best_threshold
    },
    "models/model.pkl"
)

print("\nModel saved successfully!")