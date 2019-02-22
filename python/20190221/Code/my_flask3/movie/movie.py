from flask import Blueprint, render_template, redirect, url_for, request, flash

# 创建一个蓝图对象
movie_bp = Blueprint('movie', __name__, template_folder='../templates')
movies = ['m1', 'm2', 'm3']

@movie_bp.route('/')
def index():
  return '<h1>Welcome to Movie!</h1>'

@movie_bp.route('/movie', methods=['GET', 'POST'])
def add_movie():
  if request.method == 'POST':
    title = request.form['title']
    movies.append(title)
    flash('add successfully!')
    return redirect(url_for('movie.add_movie'))
  return render_template('movie.html', movies=movies)


@movie_bp.route('/movie/<name>')
def get_movie_info(name):
  movie = None
  if name not in movies:
    movie = []
  else:
    movie[name]
  return render_template('movie.html', movies=movie)
