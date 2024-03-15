from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import os

import functions

app = Flask(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
SUBJECTS = ["Mathematics", "English", "Physics", "Chemistry", "Geography", "History", "Home Science"]
# ACTUAL_SUBJECTS = ["Mathematics", "English", "Kiswahili",
#                    {"name": "sciences", "its_subjects": ["Biology", "Chemistry", "Physics"]},
#                    {"name": "humanities", "its_subjects": ["Geography", "History", "CRE"]},
#                    {"name": "electives", "its_subjects": ["Computer", "Homescience"]}
#                    ]
ACTUAL_SUBJECTS = ["Mathematics", "English", "Kiswahili",
                   ["Biology", "Chemistry", "Physics"],
                   ["Geography", "History", "CRE"],
                   ["Computer", "Homescience"]
                   ]

compulsories = []
optionals = []
all_subjects_list = []

for subject in ACTUAL_SUBJECTS:
    if type(subject) == str:
        compulsories.append(subject)
        all_subjects_list.append(subject)
    else:
        optionals.append(subject)

for sub_list in optionals:
    for subject in sub_list:
        all_subjects_list.append(subject)



current_year = 0

@app.route("/")
def index():
    global current_year
    if current_year == 0:
        return render_template("index.html", year=current_year, compulsories=compulsories, optionals=optionals)
    elif current_year < 5:
        return render_template("index.html",
                            year=current_year,
                            subjects=session["subjects"],
                            grades=GRADES
                            )
    else:
        return render_template("index.html", year=current_year)

@app.route("/record", methods=["GET", "POST"])
def record():
    if request.method == "POST":
        global current_year
        if current_year == 0:
            uploaded_file = request.files["transcript"]
            file_extension = functions.getExtension(uploaded_file.filename)
            if "extensions" in session:
                session.pop("extensions")
            session["extensions"] = file_extension
            uploads_dir = os.path.join(script_dir, 'uploads')
            for filename in os.listdir(uploads_dir):
                file_path = os.path.join(uploads_dir, filename)
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Couldn't delete {filename} {e}")
            uploaded_file.save("uploads/transcript" + session["extensions"])
            current_year = 5
        elif current_year < 5:
            year_string = "Year " + str(current_year)
            if year_string in session:
                session.pop(year_string)
            session[year_string] = {}
            for subject in session["subjects"]:
                for grade in request.form.getlist(subject):
                    if grade not in GRADES:
                        return render_template("error.html", message="Not a valid grade.")
                session[year_string][subject] = request.form.getlist(subject)
        if current_year < 5:
            current_year += 1
            return redirect("/")
        return render_template("record.html",
                               filepath=('uploads/transcript' + session["extensions"])
                               )
    else:
        return render_template("error.html", message="Unexpected end of sequence")

app.run(debug = True)


