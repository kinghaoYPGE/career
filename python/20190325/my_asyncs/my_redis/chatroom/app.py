#!/usr/bin/env python
import datetime
import flask
import redis
from flask import render, session, request, Response, redirect, session
from datetime import datetime as dt

app = flask.Flask(__name__)
app.secret_key = 'asdf'
red = redis.StrictRedis(host='localhost', port=6379, db=6)


def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        print(message)
        yield 'data: %s\n\n' % message['data']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        return redirect('/')
    return render('login.html')


@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    user = session.get('user', 'anonymous')
    red.publish('chat', u'[%s] %s: %s' % (dt.now(), user, message))
    return Response(status=204)


@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")


@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8089, threaded=True)
