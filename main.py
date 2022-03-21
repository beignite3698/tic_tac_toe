from urllib import request
from flask import Flask ,render_template,request
app = Flask(__name__)
@app.route('/')
def tik():
    return render_template('index.html')

@app.route('/data')
def data():
    data=request.args.get('q')
    return processing(data)

def processing(data):
    