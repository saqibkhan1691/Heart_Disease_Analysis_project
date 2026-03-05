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
    features = joblib.load("models/feature_names.pkl")
    return render_template("get_started.html", features=features)




# ML API ROUTE

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    result = predict_risk(data)
    improved = simulate_improvement(data)

    result["improved_probability"] = improved

    return jsonify(result)


# RUN APP

if __name__ == "__main__":
    app.run(debug=True)