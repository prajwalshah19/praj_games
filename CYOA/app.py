from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():

    title = "The Beginning..."

    text = """One day on the way home from school, you decide to take a shortcut through the forest. 
	Walking through the trees and vines, it starts to get dark. Eventually you stumble upon a sign.
	It reads DO NOT ENTER: DANGER AHEAD."""

    img = "/static/page1.jpg"

    choices = [("Enter Forest", "Ignore the sign, go into the forest"), ("RIP", "Turn around")]

    return render_template('template.html' , title = title, text = text, img = img, choices = choices)

@app.route("/Enter Forest")
def page3():

    return render_template('template.html')

@app.route("/RIP")
def page2():

    return render_template('template.html')
