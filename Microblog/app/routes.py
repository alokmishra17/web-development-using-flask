from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alok Mishra'}
    return render_template('index.html',title='HOME PAGE',user=user)
