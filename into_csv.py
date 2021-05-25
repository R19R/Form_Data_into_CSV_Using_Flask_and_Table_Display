from types import MethodType
from flask import Flask, redirect, render_template, request, session, flash, json, jsonify
import csv, pandas
from werkzeug.utils import html


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        return render_template("newpage.html")
    else:
        return redirect(home()) 


@app.route("/inputs", methods=['GET', "POST"])
def input():
    if request.method == "POST":
        # new = request.form
        name = request.form['name']
        comment = request.form['comments']
        fieldnames = ['name', 'comment']
        with open("inputsFile.csv", 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"name":name, 'comment':comment})
        return redirect('/outputs')


@app.route("/outputs", methods=["GET"])
def output():
        filename = 'inputsFile.csv'
        data = pandas.read_csv(filename)
        data.to_html("output.html")
        html_file = data.to_html()
        return html_file



if __name__ == "__main__":
    app.run(debug=True)