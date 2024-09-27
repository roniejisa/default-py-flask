from flask_socketio import emit

def register_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        emit('message', {'data': 'Connected'})

    @socketio.on('user_created')
    def handle_user_created(data):
        print(f"User created: {data}")  # Xử lý dữ liệu ở backend

    @socketio.on('user_updated')
    def handle_user_updated(data):
        print(f"User updated: {data}")

    @socketio.on('user_deleted')
    def handle_user_deleted(data):
        print(f"User deleted: {data}")