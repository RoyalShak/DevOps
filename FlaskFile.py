from flask import Flask, render_template

app = Flask(_name_)

json_file = "TextFiles/JsonScore.json"


@app.route("/")
@app.route("/home")
def home():
    all_time_scores = open(json_file, "r")
    return all_time_scores.read()
    # return render_template('home.html', post=all_time_scores.read())


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if _name_ == '_main_':
    app.run(debug=True)