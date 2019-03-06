from application.extensions import db
from datetime import datetime

__all__ = ['TodoList', 'Todo']


class Todo(db.Document):
    desc = db.StringField()
    create_at = db.DateTimeField(default=datetime.now())
    finished_at = db.DateTimeField(default=None)  # todo的完成时间
    is_finished = db.BooleanField(default=False)  # todo状态:1. finished, 2. open
    creator = db.ReferenceField('User')
    todolist = db.ReferenceField('TodoList')

    @property
    def id(self):
        return str(self._id)

    @property
    def status(self):
        return 'finished' if self.is_finished else 'open'

    def finished(self):
        self.finished_at = datetime.now()
        self.is_finished = True
        self.save()

    def reopen(self):
        self.finished_at = None
        self.is_finished = False
        self.save()

    def to_dict(self):
        return {
            'description': self.desc,
            'creator': self.creator.username,
            'create_at': self.create_at,
            'finished_at': self.finished_at,
            'status': self.status
        }


class TodoList(db.Document):
    title = db.StringField()
    create_at = db.DateTimeField(default=datetime.now())
    creator = db.ReferenceField('User')
    todos = db.ListField()

    @property
    def id(self):
        return str(self._id)

    @property
    def todo_count(self):
        return len(self.todos)

    @property
    def finished_count(self):
        return len(list(
            filter(lambda x: x.is_finished, self.todos)
        ))

    @property
    def open_count(self):
        return self.todo_count - self.finished_count

    def to_dict(self):
        return {
            'title': self.title,
            'creator': self.creator.username,
            'create_at': self.create_at,
            'todo_count': self.todo_count,
            'finished_count': self.finished_count,
            'open_count': self.open_count
        }


