from flask import Flask, render_template, request
import joblib
import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

model = joblib.load("foodexp.pkl")

client = Groq()
app = Flask(__name__)

@app.route("/",methods=["get","post"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["get","post"])
def main():
    return(render_template("main.html"))

@app.route("/ethics",methods=["get","post"])
def ethics():
    return(render_template("ethics.html"))

@app.route("/correct",methods=["get","post"])
def correct():
    return(render_template("correct.html"))

@app.route("/wrong",methods=["get","post"])
def wrong():
    return(render_template("wrong.html"))

@app.route("/econ",methods=["get","post"])
def econ():
    return(render_template("econ.html"))

@app.route("/foodexp",methods=["get","post"])
def foodexp():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    return(render_template("foodexp.html",r=r[0][0]))

@app.route("/roe",methods=["get","post"])
def roe():
    
    return(render_template("roe.html"))

@app.route("/generalquestion",methods=["get","post"])
def generalquestion():
    return(render_template("generalquestion.html"))

@app.route("/groq",methods=["get","post"])
def groq():
    return(render_template("groq.html"))

if __name__ == "__main__":
    app.run()