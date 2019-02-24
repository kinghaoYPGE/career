from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True)
  email = db.Column(db.String(30), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email
  
  def __repr__(self):
    return '<User: %s>' % self.username
  __str__ = __repr__
@app.route('/adduser')
def add_user():
  # user = User('zhangsan', '1@test.com')
  from faker import Faker
  fake = Faker()
  for i in range(5):
    user = User(fake.name(), fake.email())
    db.session.add(user)
  db.session.commit()
  return '<h3>add user successfully!</h3>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)
