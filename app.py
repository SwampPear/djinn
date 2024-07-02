from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def hello_geek():
    return render_template('interface/templates/index.html')


if __name__ == "__main__":
    print(os.getcwd())
    #app.run(debug=False)