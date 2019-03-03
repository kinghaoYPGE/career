from flask import jsonify, request, abort, url_for
from . import api_bp
import application.models as Models
from werkzeug.security import generate_password_hash
from application.decorators import permission_control

#=========ajax=========#
@api_bp.route('/todo/<todo_id>')
def get_todo(todo_id):
  todo = Models.Todo.objects(id=todo_id).first()
  if not todo:
    abort(404)
  return jsonify(todo.to_dict())

@api_bp.route('/todo/<todo_id>', methods=['PUT'])
def update_todo_status(todo_id):
  todo = Models.Todo.objects(id=todo_id).first()
  if not todo:
    abort(404)
  try:
    if request.json.get('is_finished'):
      todo.finished()
    else:
      todo.reopen()
  except:
    abort(400)
  print(todo.to_dict())
  return jsonify(todo.to_dict())

@api_bp.route('/todolist/<todolist_id>', methods=['PUT'])
@permission_control(Models.Permission.DELETE)
def change_todolist_title(todolist_id):
  todolist = Models.TodoList.objects(id=todolist_id).first()
  if not todolist:
    abort(404)
  try:
    todolist.update(title=request.json.get('title'))
  except:
    abort(400)
  return jsonify(todolist.to_dict())

#=========ajax=========#



@api_bp.route('/user/<string:username>')
def get_user(username):
  user = Models.User.objects(username=username).first()
  return jsonify(user.to_dict())

@api_bp.route('/user', methods=['POST'])
def add_user():
  try:
    user = Models.User(
      username=request.json.get('username'),
      email=request.json.get('email'),
      password=generate_password_hash(request.json.get('password'))
    ).save()
  except:
    abort(400)
  return jsonify(user.to_dict()), 201  # 新建成功

  @api_bp.route('/user/<string:username>/todolists')
  def get_user_todolists(username):
    user = Models.User.objects(username=username).first()
    todolists = user.todolists
    return jsonify({
      'todolists': [todolist.to_dict() for todolist in user.todolists]
    })

  @api_bp.route('/user/<string:username>/todolist/<todolist_id>')
  def get_user_todolist(username, todolist_id):
    user = Models.User.objects(username=username).first()
    todolist = Models.TodoList.objects(id=todolist_id).first()
    if not user or username != todolist.creator.username:
      abort(404)
    return jsonify(todolist.to_dict())

@api_bp.route('/user/<string:username>/todolist', methods=['POST'])
def add_user_todolist(username):
  return 


@api_bp.route('/todolists')
def get_todolists():
  return

@api_bp.route('/todolist/<todolist_id>')
def get_todolist(todolist_id):
  return

@api_bp.route('/todolist', methods=['POST'])
def add_todolist():
  return

@api_bp.route('/todolist/<todolist_id>/todos')
def get_todolist_todos(todolist_id):
  return

@api_bp.route('/user/<string:username>/todolist/<todolist_id>/todos')
def get_user_todolist_todos(username, todolist_id):
  return

@api_bp.route('/user<string:username>/todolist/<todolist_id>', methods=['POST'])
def add_user_todolist_todo(username, todolist_id):
  return

@api_bp.route('/todolist/<todolist_id>', methods=['POST'])
def add_todolist_todo(todolist_id):
  return

@api_bp.route('/user/<string:username>')
def delete_user(username):
  return

@api_bp.route('/todolist/<todolist_id>')
def delete_todolist(todolist_id):
  return

@api_bp.route('/todo/<todo_id>')
def delete_todo(todo_id):
  return
