from flask import Flask, render_template
from flask.helpers import url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
