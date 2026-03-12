import sys
import os

from models.predict import predict_risk, simulate_improvement

from flask import request, jsonify

from flask import Flask, render_template

import joblib

app = Flask(__name__)

# PAGE ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get_started")
def get_started():

    binary_features = [
        "Smoking",
        "AlcoholDrinking",
        "Stroke",
        "DiffWalking",
        "Diabetic",
        "PhysicalActivity",
        "Asthma",
        "KidneyDisease",
        "SkinCancer",
        "Race_Asian",
        "Race_Black",
        "Race_Hispanic",
        "Race_Other",
        "Race_White"
    ]

    numeric_features = [
        "BMI",
        "PhysicalHealth",
        "MentalHealth",
        "AgeCategory",
        "GenHealth",
        "SleepTime"
    ]

    return render_template(
        "get_started.html",
        binary_features=binary_features,
        numeric_features=numeric_features
    )


# ML API ROUTE

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    result = predict_risk(data)

    improvement = simulate_improvement(data)

    result["improved_probability"] = improvement["improved_probability"]
    result["suggestions"] = improvement["suggestions"]

    return jsonify(result)


# RUN APP

if __name__ == "__main__":
    app.run(debug=True)