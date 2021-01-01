# -*- coding: utf-8 -*- 
# __author__: Adarsh Kalikadien #
import sqlite3
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect('test.db')
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    data = c.fetchall()
    column_names = [description[0] for description in c.description]
    return render_template("home.html", data=data, column_names=column_names)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test1")
def test1():
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect('test.db')
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    data = c.fetchall()
    column_names = [description[0] for description in c.description]
    return render_template("test1.html", data=data, column_names=column_names)


if __name__ == "__main__":
    app.run(debug=True)
