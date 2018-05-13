from flask import Flask, render_template
import os

from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"


@app.route('/home')
def homepage():
    users = [
        {
            'name' : 'ice',
        },
        {
            'name' : 'ic3'
        },
        {
            'name' : 'Ic3Sandy'
        }
    ]
    return render_template('home.html', title='Home', users=users)
    

if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)

