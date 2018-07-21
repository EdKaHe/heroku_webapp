# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:52:48 2018

@author: edizh
"""

from flask import Flask, render_template

#give the Flask class the name of the script
#if script executed __name__="__main__"
#if included __name__="script"
app=Flask(__name__)

#output of home function is mapped to the url
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)