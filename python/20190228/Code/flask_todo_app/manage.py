from flask_script import Manager

from application import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='mode', required=False)
if __name__ == '__main__':
  manager.run()

