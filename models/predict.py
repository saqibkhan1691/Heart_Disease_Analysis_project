# import os
# import joblib
# import pandas as pd
# import numpy as np

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
# bundle = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
# model = bundle["model"]
# threshold = bundle["threshold"]
# feature_names = joblib.load(os.path.join(BASE_DIR, "feature_names.pkl"))
# feature_means = joblib.load(os.path.join(BASE_DIR, "feature_means.pkl"))


# def categorize_risk(probability):
#     if probability < 0.20:
#         return "Low", "green"
#     elif probability < 0.40:
#         return "Medium", "yellow"
#     else:
#         return "High", "red"


# def prepare_input(user_input):
#     # Fill missing features with mean
#     full_input = {}

#     for feature in feature_names:
#         if feature in user_input:
#             full_input[feature] = user_input[feature]
#         else:
#             full_input[feature] = feature_means[feature]

#     return pd.DataFrame([full_input])


# def predict_risk(user_input):

#     input_df = prepare_input(user_input)

#     probability = model.predict_proba(input_df)[0][1]

#     prediction = int(probability >= threshold)

#     category, color = categorize_risk(probability)

#     return {
#         "probability": round(float(probability) * 100, 2),
#         "category": category,
#         "color": color
#     }


# def simulate_improvement(user_input):

#     modified_input = user_input.copy()

#     # Example improvement assumptions
#     if "Smoking" in modified_input:
#         modified_input["Smoking"] = 0

#     if "PhysicalActivity" in modified_input:
#         modified_input["PhysicalActivity"] = 1

#     input_df = prepare_input(modified_input)

#     new_prob = model.predict_proba(input_df)[0][1]

#     return round(float(new_prob) * 100, 2)





import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bundle = joblib.load(os.path.join(BASE_DIR,"model.pkl"))
model = bundle["model"]
threshold = bundle["threshold"]

feature_names = joblib.load(os.path.join(BASE_DIR,"feature_names.pkl"))
feature_means = joblib.load(os.path.join(BASE_DIR,"feature_means.pkl"))


def categorize_risk(prob):

    if prob < 0.20:
        return "Low","green"

    elif prob < 0.40:
        return "Medium","orange"

    else:
        return "High","red"


def prepare_input(user_input):

    data = {}

    for f in feature_names:

        if f in user_input:
            data[f] = float(user_input[f])
        else:
            data[f] = feature_means[f]

    df = pd.DataFrame([data])

    return df


def predict_risk(user_input):

    df = prepare_input(user_input)

    prob = model.predict_proba(df)[0][1]

    category,color = categorize_risk(prob)

    return {
        "probability": round(prob*100,2),
        "category": category,
        "color": color
    }


def simulate_improvement(user_input):

    improved = user_input.copy()

    if "Smoking" in improved:
        improved["Smoking"] = 0

    if "AlcoholDrinking" in improved:
        improved["AlcoholDrinking"] = 0

    if "PhysicalActivity" in improved:
        improved["PhysicalActivity"] = 1

    if "BMI" in improved:
        improved["BMI"] = min(float(improved["BMI"]),25)

    df = prepare_input(improved)

    prob = model.predict_proba(df)[0][1]

    return round(prob*100,2)