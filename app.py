from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            age = int(request.form.get("age", 0))
            sex = int(request.form.get("sex", 0))
            cp = int(request.form.get("cp", 0))
            trestbps = int(request.form.get("trestbps", 0))
            chol = int(request.form.get("chol", 0))
            fbs = int(request.form.get("fbs", 0))
            restecg = int(request.form.get("restecg", 0))
            thalach = int(request.form.get("thalach", 0))
            exang = int(request.form.get("exang", 0))
            oldpeak = float(request.form.get("oldpeak", 0))
            slope = int(request.form.get("slope", 0))
            ca = int(request.form.get("ca", 0))
            thal = int(request.form.get("thal", 0))

            features = np.array([[
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]])

            prediction = model.predict(features)

            if prediction[0] == 1:
                result = "⚠️ High risk of heart disease"
            else:
                result = "✅ Low risk of heart disease"

        except Exception:
            result = "⚠️ Error: Please enter valid values"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)