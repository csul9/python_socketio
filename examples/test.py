import socketio
import eventlet


sio = socketio.Server(async_mode='eventlet')
app = socketio.Middleware(sio)
import eventlet
eventlet.wsgi.server(eventlet.listen(('', 8000)), app)