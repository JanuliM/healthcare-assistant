from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        symptom_text = request.form["symptom"].lower()

        # symptom flags
        has_fever = "fever" in symptom_text
        has_headache = "headache" in symptom_text
        has_cough = "cough" in symptom_text
        has_tiredness = "tired" in symptom_text or "fatigue" in symptom_text

        # smarter logic
        if has_fever and has_cough:
            response = "Possible: Flu or viral infection"
        elif has_headache and has_tiredness:
            response = "Possible: Stress or dehydration"
        elif has_cough:
            response = "Possible: Respiratory infection"
        elif has_fever:
            response = "Possible: Infection (monitor temperature)"
        else:
            response = "Symptoms unclear. Please consult a doctor"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)