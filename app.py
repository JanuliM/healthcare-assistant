from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        symptom_text = request.form["symptom"].lower()
        possible_causes = []

        if "fever" in symptom_text:
            possible_causes.append("Viral infection or flu")
        if "headache" in symptom_text:
            possible_causes.append("Stress, dehydration, or fatigue")
        if "cough" in symptom_text:
            possible_causes.append("Cold or respiratory infection")

        if possible_causes:
            response = "Possible: " + " | ".join(possible_causes)
        else:
            response = "Please consult a doctor for proper diagnosis"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)