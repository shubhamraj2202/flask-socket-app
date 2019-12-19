from flask import Flask, render_template
from flask_socketio import SocketIO
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.debug = True
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('index.html')

def message_received(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(received_json_data ,methods=['GET', 'POST']): # received_json_data is used when calling post
	r = random.choice(range(0,100000))
	print('Received event: ' + str(r))
	socketio.emit('Response : ', r, callback=message_received)
	
if __name__ == '__main__':
    socketio.run(app)