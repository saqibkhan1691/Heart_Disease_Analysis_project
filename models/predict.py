import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bundle = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
model = bundle["model"]
threshold = bundle["threshold"]

feature_names = joblib.load(os.path.join(BASE_DIR, "feature_names.pkl"))
feature_means = joblib.load(os.path.join(BASE_DIR, "feature_means.pkl"))


def categorize_risk(prob):
    if prob < 0.20:
        return "Low", "green"
    elif prob < 0.40:
        return "Medium", "orange"
    else:
        return "High", "red"


def prepare_input(user_input):
    data = {}

    for f in feature_names:
        if f in user_input:
            data[f] = float(user_input[f])
        else:
            data[f] = feature_means[f]

    return pd.DataFrame([data])


def predict_risk(user_input):

    df = prepare_input(user_input)

    prob = model.predict_proba(df)[0][1]

    category, color = categorize_risk(prob)

    return {
        "probability": round(prob * 100, 2),
        "category": category,
        "color": color
    }

def simulate_improvement(user_input):

    suggestions = []

    base_df = prepare_input(user_input)
    base_prob = model.predict_proba(base_df)[0][1]

    improved_input = user_input.copy()
    improved_prob = base_prob

    for feature in user_input:

        original_value = user_input[feature]

        # Binary feature
        if original_value == 1:

            improved_input[feature] = 0

            df = prepare_input(improved_input)
            new_prob = model.predict_proba(df)[0][1]

            reduction = base_prob - new_prob

            if reduction > 0:

                suggestions.append(
                    f"Reducing {feature} may lower risk by {round(reduction*100,2)}%"
                )

                improved_prob = new_prob

            improved_input[feature] = original_value

    return {
        "improved_probability": round(improved_prob * 100, 2),
        "suggestions": suggestions
    }