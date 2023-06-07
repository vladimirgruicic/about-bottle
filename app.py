from bottle import Bottle, run, template, static_file

app = Bottle()

@app.route('/')
def index():
    return """
        Hello my man DevOps! Howdy!!!
        This is our road to success with Python'
        """
@app.route('/about')
def about():
    return """
        This is About page. It is not fany as the one on About You or some others, but it is a start.
    """
@app.route('/zlatan')
def zlatan():
    return """
        This is tribute to Zlatan Emperor Of Football Ibrahimovic. I saw his farewell on Milan stadium and it was beautuful.
    """
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
    return template('hello_template', name=name)

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, reloader=True)