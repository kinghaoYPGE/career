"""
Flask-Bootstrap
Bootstrap:Twitter开源的CSS/HTML前端框架
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from faker import Faker

fake = Faker()

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/book')
def book():
  books = fake.words(5)
  return render_template('index.html', books=books)

@app.route('/movie')
def movie():
  movies = fake.words(5)
  return render_template('index.html', movies=movies)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)