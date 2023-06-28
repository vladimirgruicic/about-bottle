from bottle import Bottle, run, template, static_file
from models import User

app = Bottle()

@app.route('/')
def index():
    return template('views/index.tpl')

@app.route('/about')
def about():
    return template('about')

@app.route('/contact')
def contact():
    return template('contact')

@app.route('/zlatan')
def zlatan():
    return template('views/zlatan.tpl')

@app.route('/api/data')
def api_data():
    data = {'name': 'John', 'Age': 5,
            'name': 'Zlatan', 'Age': 41,
            'name': 'John', 'Age': 25,
            'name': 'Zlatan', 'Age': 41,
            'name': 'John', 'Age': 5,
            }
    return data

@app.route('/hello/<name>')
def hello_name(name):
    name = "Vladimir"
    return template('views/hello_template', name=name)

# Route for the dropdown page
@app.route('/dropdown')
def dropdown():
    return template('dropdown_template')

# Route for serving static files
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, reloader=True)