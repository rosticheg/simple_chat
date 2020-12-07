import logging
from flask import render_template, flash, redirect, url_for, request
from app import app
from logging.handlers import RotatingFileHandler
from flask_socketio import SocketIO


socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
