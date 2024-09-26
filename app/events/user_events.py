from flask_socketio import emit

def handle_user_event(data):
    # Xử lý sự kiện từ client
    emit('response_event', {'data': data}, broadcast=True)