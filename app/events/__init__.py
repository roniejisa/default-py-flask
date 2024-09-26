from .user_events import handle_user_event

def register_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        emit('message', {'data': 'Connected'})
    
    @socketio.on('user_event')
    def handle_event(data):
        handle_user_event(data)
