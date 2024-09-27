from ..extensions import socketio  # Đảm bảo bạn đã import socketio

def publish_event(event_type, data):
    # Phát sự kiện với key cụ thể
    socketio.emit(event_type, data)  # Đảm bảo dùng socketio ở đây