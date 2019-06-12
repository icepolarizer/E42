#!/usr/bin/env python
# Socket Communication Inspired from https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

clients = {} #id-room(socket)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        print(clients)
        socketio.sleep(10)
        count += 1
        # socketio.emit('my_response',
        #               {'data': 'Server generated event', 'count': count},
        #               namespace='/test')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('login', namespace='/test')
def login(message):
    global clients
    clients[message['id']] = request.sid
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('join', namespace='/test')
def join(message):
    global clients
    join_room(clients[message['room']])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('qkd',
         {'data': 'In rooms ' + ', '.join(rooms()),
          'laser': message['laser'],
          'count': session['receive_count']
          }, room=clients[message['room']])


@socketio.on('usr_msg', namespace='/test')
def usr_msg(message):
    session['receive_count'] = session.get('receive_count', 0) + 1

    emit('usr_msg',
         {'sender': message['sender'], 'data': message['data'], 'count': session['receive_count']},
         room=clients[message['recv']])


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1

    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)