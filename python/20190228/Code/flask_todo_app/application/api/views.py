from flask import jsonify, request, abort
import application.models as Models
from . import api_bp
import application.models as Models


#===========ajax============
@api_bp.route('/todo/<todo_id>')
def get_todo(todo_id):
    todo = Models.Todo.objects(id=todo_id).first_or_404()
    return jsonify(todo.to_dict())


@api_bp.route('/todo/<todo_id>', methods=['PUT'])
def update_todo_status(todo_id):
    todo = Models.Todo.objects(id=todo_id).first_or_404()
    try:
        if request.json.get('is_finished'):
           todo.finished()
        else:
            todo.reopen()
    except:
        abort(400)
    return jsonify(todo.to_dict())


#===========ajax============



@api_bp.route('/user/<string:username>')
def get_user(username):
    """
    得到用户信息
    :param username:
    :return:
    """
    user = Models.User.objects(username=username).first_or_404()
    return jsonify(user.to_dict())

# todo

