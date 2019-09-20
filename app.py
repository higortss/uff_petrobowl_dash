from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("master_file.html")


@app.route("/QuickGame")
def quickgame():
    if request.method == 'POST':
        if request.form['button'] == 'clicked':
            return render_template("performance.html")


app.run()
