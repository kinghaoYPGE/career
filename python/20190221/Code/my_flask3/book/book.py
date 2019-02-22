from flask import Blueprint, render_template, redirect, url_for, request, flash

# 创建一个蓝图对象
book_bp = Blueprint('book', __name__, template_folder='../templates')
books = ['Java', 'Python', 'Javascript']

@book_bp.route('/')
def index():
  return '<h1>Welcome to Book!</h1>'

@book_bp.route('/book', methods=['GET', 'POST'])
def add_book():
  if request.method == 'POST':
    title = request.form['title']
    books.append(title)
    flash('add successfully!')
    return redirect(url_for('book.add_book'))
  return render_template('book.html', books=books)


@book_bp.route('/book/<name>')
def get_book_info(name):
  book = None
  if name not in books:
    book = []
  else:
    book[name]
  return render_template('book.html', books=book)
