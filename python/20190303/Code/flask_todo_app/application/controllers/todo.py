from flask import Blueprint, redirect, url_for, render_template, request
from application.forms import *
import application.models as Models
from flask_login import login_required, current_user

index_bp = Blueprint('index', __name__, url_prefix='/')
todo_bp = Blueprint('todo', __name__, url_prefix='/todo')


@index_bp.route('/')
def home():
    return redirect(url_for('todo.index'))

@todo_bp.route('/')
def index():
    form = TodoForm()
    if form.validate_on_submit():
        return redirect(url_for('todo.new_todolist'))
    return render_template('index.html', form=form)

@todo_bp.route('/todolists', methods=['GET', 'POST'])
@login_required
def todolist_overview():
    form = TodoListForm()
    if form.validate_on_submit():
        return redirect(url_for('todo.add_todolist'))
    return render_template('overview.html', form=form)


@todo_bp.route('/todolist/<id>', methods=['GET', 'POST'])
def todolist(id):
    todolist = Models.TodoList.objects(id=id).first()
    form = TodoForm()
    if form.validate_on_submit():
      # 值得注意的是mongo和关系数据库不一样，不能根据字段进行关联,所有对于reference field要存入对象类型
        todo = Models.Todo(description=form.todo.data, 
        todolist=todolist, creator=current_user.id).save()
        todolist.update(push__todos=todo)
        return redirect(url_for('todo.todolist', id=id))
    return render_template('todolist.html', todolist=todolist, form=form)

@todo_bp.route('/todolist/new', methods=['POST'])
@login_required
def new_todolist():
    form = TodoForm(todo=request.form.get('todo'))
    if form.validate():
        todolist = Models.TodoList(title='Untitled', creator=current_user.id).save()
        current_user.update(push__todolists=todolist)
        todo = Models.Todo(description=form.todo.data, todolist=todolist).save()
        todolist.update(push__todos=todo)
        return redirect(url_for('todo.todolist', id=todolist.id))
    return redirect(url_for('todo.index'))

@todo_bp.route('/todolist/add', methods=['POST'])
@login_required
def add_todolist():
    form = TodoListForm(todo=request.form.get('title'))
    if form.validate():
        todolist = Models.TodoList(title=form.title.data, 
        creator=current_user.id).save()
        current_user.update(push__todolists=todolist)
        return redirect(url_for('todo.todolist', id=todolist.id))
    return redirect(url_for('todo.index'))

