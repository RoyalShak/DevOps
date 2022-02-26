from Utils import SCORES_FILE_NAME
from flask import Flask, render_template


def holyflask():
    app = Flask(__name__)
    TotalScore = open(SCORES_FILE_NAME).read()

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('home.html', score=TotalScore)

    @app.route("/about")
    def about():
        return render_template('about.html', title='About')

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)


holyflask()
