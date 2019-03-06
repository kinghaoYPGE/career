from flask import Blueprint, render_template, redirect, url_for, request
from application.forms import *
import application.models as Models
from flask_login import current_user

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')


@todo_bp.route('/')
def index():
    form = TodoForm()
    if form.validate_on_submit():
        return redirect(url_for('todo.new_todolist'))
    return render_template('index.html', form=form)


@todo_bp.route(('/todolist/new'), methods=['POST'])
def new_todolist():
    form = TodoForm(todo=request.form.get('todo'))
    if form.validate():
        todolist = Models.TodoList(
            title='Untitled',
            creator=current_user.id
        ).save()
        # 将todolist关联到当前用户下
        current_user.update(push__todolists=todolist)
        todo = Models.Todo(
            desc=form.todo.data,
            todolist=todolist.id,
            creator=current_user.id
        ).save()
        # 将todo关联到todolist下
        todolist.update(push__todos=todo)
        return redirect(url_for('todo.todolist', id=todolist.id))
    return redirect(url_for('todo.index'))


@todo_bp.route('/todolists', methods=['GET', 'POST'])
def todolist_overview():
    form = TodoListForm()
    if form.validate_on_submit():
        return redirect(url_for('todo.add_todolist'))
    return render_template('overview.html', form=form)


@todo_bp.route('/todolist/<id>', methods=['GET', 'POST'])
def todolist(id):
    todolist = Models.TodoList.objects(id=id).first_or_404()
    form = TodoForm()
    if form.validate_on_submit():
        todo = Models.Todo(
            desc=form.todo.data,
            todolist=todolist.id,
            creator=current_user.id
        ).save()
        todolist.update(push__todos=todo)
        return redirect(url_for('todo.todolist', id=id))
    return render_template('todolist.html', todolist=todolist, form=form)


@todo_bp.route('/todolist/add', methods=['POST'])
def add_todolist():
    form = TodoListForm(title=request.form.get('title'))
    if form.validate():
        todolist = Models.TodoList(
            title=form.title.data,
            creator=current_user.id
        ).save()
        current_user.update(push__todolists=todolist)
        return redirect(url_for('todo.todolist', id=todolist.id))
    return redirect(url_for('todo.index'))


