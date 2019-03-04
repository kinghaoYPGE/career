from application.extensions import db
from datetime import datetime

__all__ = ['TodoList', 'Todo']


class Todo(db.Document):
    description = db.StringField()
    created_at = db.DateTimeField(default=datetime.now())
    finished_at = db.DateTimeField(default=None)
    is_finished = db.BooleanField(default=False)
    creator = db.ReferenceField('User')
    todolist = db.ReferenceField('TodoList')

    @property
    def id(self):
        return str(self._id)

    @property
    def status(self):
        return 'finished' if self.is_finished else 'open'

    def finished(self):
        self.is_finished = True
        self.finished_at = datetime.now()
        self.save()

    def reopen(self):
        self.is_finished = False
        self.finished_at = None
        self.save()

    def remove(self):
        self.delete()

    def to_dict(self):
        return {
            'description': self.description,
            'creator': self.creator.username,
            'create_at': self.created_at,
            'finished_at': self.finished_at,
            'status': self.status
        }

class TodoList(db.Document):
    title = db.StringField()
    created_at = db.DateTimeField(default=datetime.now())
    creator = db.ReferenceField('User')
    todos = db.ListField(default=[])
    
    @property
    def id(self):
        return str(self._id)

    @property
    def todo_count(self):
        return len(self.todos)

    @property
    def finished_count(self):
        return len(list(filter(lambda x: x.is_finished, self.todos)))

    @property
    def open_count(self):
        return len(list(filter(lambda x: not x.is_finished, self.todos)))

    def to_dict(self):
        return {
            'title': self.title,
            'create_at': self.created_at,
            'creator': self.creator.username,
            'todo_count': self.todo_count,
            'finished_count': self.finished_count,
            'open_count': self.open_count
        }
