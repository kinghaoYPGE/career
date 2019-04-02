from flask import Flask, render_template
from flask import request, session, url_for, redirect, Response
import redis
from datetime import datetime as dt

app = Flask(__name__)

app.secret_key = 'chatroom'

client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    user = session.get('user', 'anonymous')
    # redis接收到用户请求信息，然后发布到redis
    client.publish('chat_channel1', '[%s] %s: %s' % (dt.now(), user, message))
    return Response(status=204)


def _event_stream():
    pubsub = client.pubsub()
    pubsub.subscribe('chat_channel1')
    for msg in pubsub.listen():
        print(msg)
        yield 'data: %s\n\n' % msg['data']


@app.route('/stream')
def stream():
    return Response(_event_stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 8089)
