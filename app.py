from bottle import Bottle, run, template, static_file, request
from models import User
import sqlite3

app = Bottle()

@app.route('/', method=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the username and email from the form
        username = request.forms.get('username')
        email = request.forms.get('email')

        # Insert the data into the database
        conn = sqlite3.connect('db/aboutbottle.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))

        conn.commit()
        conn.close()

        # Redirect to the home page with a success message
        return template('home', success_message='Data inserted sucessfully!')
    return template('home')

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