# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import calculate


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/survey')
def survey():
    return render_template("survey.html")

@app.route('/results', methods =["GET", "POST"])
def results():
    if request.method=="POST":
        my_answer_procrastination=request.form["procrastination"]
        my_answer_support=request.form["support"]
        print(my_answer_support)
        user_answers = {
           "procrastination": my_answer_procrastination,
            "support": my_answer_support
        }
        return render_template('results.html', user_answers=user_answers)

@app.route('/study_plan', methods=["GET", "POST"])
def study_plan():
    if request.method=="POST":
        my_hard_class= request.form['hard_class']
        my_grade= request.form['average']
        my_goal=request.form['goal']
        assignment_type = request.form['assignment_type']
        my_homework = request.form['homework']
        user_academics = {
            "my_hard_class": my_hard_class,
            "my_grade": my_grade,
            "my_goal": my_goal,
            "my_homework": my_homework,
            "my_current_assignment": assignment_type
        }
        study_plan=calculate(user_academics)
        return render_template('study_plan.html', user_academics=user_academics, study_plan=study_plan)