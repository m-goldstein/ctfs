import os
from flask import Flask, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("hi")
    #with open('main.py') as j:
    #    source = j.read()
    #    return render_template('index.html', source=source)

@app.route('/', methods=['IMAGINARY'])
def imaginary():
    return render_template_string(f"{os.getenv('FLAG')}")

@app.route('/notflag')
def nottheflag():
  return render_template_string("the flag isn't here lol")

if(__name__ == '__main__'):
      app.run('0.0.0.0', 8080)
