from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "healthcare-assistant-secret-key"

# Load trained ML model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            def required_number(field_name, caster):
                value = request.form.get(field_name)
                if value is None or str(value).strip() == "":
                    raise ValueError(f"Missing field: {field_name}")
                return caster(value)

            age = required_number("age", int)
            sex = required_number("sex", int)
            cp = required_number("cp", int)
            trestbps = required_number("trestbps", int)
            chol = required_number("chol", int)
            fbs = required_number("fbs", int)
            restecg = required_number("restecg", int)
            thalach = required_number("thalach", int)
            exang = required_number("exang", int)
            oldpeak = required_number("oldpeak", float)
            slope = required_number("slope", int)
            ca = required_number("ca", int)
            thal = required_number("thal", int)

            features = np.array([[
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]])

            prediction = model.predict(features)

            if prediction[0] == 1:
                session["result"] = "⚠️ High risk of heart disease"
            else:
                session["result"] = "✅ Low risk of heart disease"

        except Exception:
            session["result"] = "⚠️ Error: Please enter valid values"

        return redirect(url_for("home"))

    result = session.pop("result", None)
    prediction_made = result is not None

    return render_template("index.html", result=result, prediction_made=prediction_made)

if __name__ == "__main__":
    app.run(debug=True)