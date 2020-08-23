from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    date = datetime.datetime.now().strftime("%x")
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", date=date, hour=hour)

@app.route("/about")
def about():
    date = datetime.datetime.now().strftime("%x")
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template("about.html", date=date, hour=hour)

@app.route("/portfolio")
def portfolio():
    date = datetime.datetime.now().strftime("%x")
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template("portfolio.html", date=date, hour=hour)

@app.route("/portfolio/frizerskisalon")
def frizerskisalon():
    return render_template("https://gist.github.com/renatodjurdjevic/1f9e8105d967c0c9cd9fb2fdcb4d3ecf")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("https://gist.github.com/renatodjurdjevic/9c175d448cab9867767574827c09d452")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("https://gist.github.com/renatodjurdjevic/0de667a00532ecb6704b6d8bd2b29309")

if __name__ == "__main__":
    app.run()
