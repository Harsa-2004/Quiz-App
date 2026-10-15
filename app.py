from flask import Flask, render_template, request
from database import create_table, get_questions
from generate_quiz import generate_questions

app = Flask(__name__)

create_table()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        topic = request.form["topic"]

        generate_questions(topic)

        questions = get_questions()

        return render_template("quiz.html", questions=questions)

    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    questions = get_questions()

    score = 0

    for q in questions:

        qid = str(q[0])

        correct = q[6]

        user_answer = request.form.get(qid)

        if user_answer == correct:
            score += 1

    return render_template("result.html", score=score, total=len(questions))


if __name__ == "__main__":
    app.run(debug=True)