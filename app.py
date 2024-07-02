from flask import Flask, render_template
from interface import project_view, sprint_view, iteration_view, log_view


app = Flask(
    __name__, 
    template_folder='/app/interface/templates',
    static_folder='/app/interface/static')

app.register_blueprint(project_view)
app.register_blueprint(sprint_view)
app.register_blueprint(iteration_view)
app.register_blueprint(log_view)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)