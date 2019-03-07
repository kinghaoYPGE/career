#!/usr/bin/env python
# encoding: utf-8

from app import create_app
from flask_script import Manager
from flask_script.commands import ShowUrls

manager = Manager(create_app)

manager.add_option('-c', '--config', dest='mode', required=False)
manager.add_command('showurls', ShowUrls())

if __name__ == '__main__':
    manager.run()
