from flask import Flask, render_template
from interface import log_view


app = Flask(
    __name__, 
    template_folder='/app/interface/templates',
    static_folder='/app/interface/static')

app.register_blueprint(log_view)

@app.route('/')
def hello_geek():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False, )