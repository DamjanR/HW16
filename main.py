from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template("prva-stran.html")

@app.route("/bogle")
def bogle():
    return render_template("bogle.html")

@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

if __name__ == '__main__':
    app.run()
