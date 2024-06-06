from flask import Flask, render_template
from models import get_data

app = Flask(__name__)

@app.route('/')
def index():
    alumnos = get_data()
    return render_template('index.html', alumnos=alumnos)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
