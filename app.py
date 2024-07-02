from flask import Flask, render_template
import os


app = Flask(__name__, template_folder='/app/interface/templates')

@app.route('/')
def hello_geek():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False, )