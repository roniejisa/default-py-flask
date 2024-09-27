import bcrypt
import re

def create_hash(password):
    # Chuyển đổi mật khẩu sang dạng byte
    # password_bytes = password.encode('utf-8')
    # Tạo salt tự động
    salt = bcrypt.gensalt(12)
    # Băm mật khẩu
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def check_hash(password, hashed):
    # Kiểm tra mật khẩu
    # Chuyển đổi từ str sang bytes
    password = password.encode('utf-8')
    hashed = hashed.encode('utf-8')
    return bcrypt.checkpw(password, hashed)

def is_valid_email(email):
    email_regex = re.compile(r'''
        ^[A-Za-z0-9._%+-]+      # Tên người dùng: chữ cái, số, ., _, %, +, -
        @                       # Ký tự @
        [A-Za-z0-9.-]+          # Tên miền: chữ cái, số, ., -
        \.[A-Za-z]{2,}$         # Phần mở rộng: từ 2 ký tự trở lên
    ''', re.VERBOSE)
    
    return bool(email_regex.match(email))

def is_valid_username(username):
    username_regex = re.compile(r'''
        ^                       # Bắt đầu chuỗi
        (?![_\-])(?!.*[_\-]$)   # Không bắt đầu hoặc kết thúc bằng _ hoặc -
        [A-Za-z0-9_\-]{3,30}    # Chứa chữ cái, số, _ hoặc - và độ dài từ 3 đến 30
        $
    ''', re.VERBOSE)
    
    return bool(username_regex.match(username))

def is_valid_phone(phone):
    """
    Kiểm tra xem chuỗi phone có phải là số điện thoại hợp lệ không.
    Hỗ trợ các định dạng như +84 123 456 789, 0123-456-789, (0123) 456-789
    """
    phone_regex = re.compile(r'''
        ^                   # Bắt đầu chuỗi
        (\+?\d{1,3}\s?)?    # Mã quốc gia (tùy chọn), ví dụ: +84
        (\(?\d{2,4}\)?)     # Số điện thoại, có thể có dấu ngoặc đơn
        [\s\-\.]?           # Khoảng trắng, dấu gạch ngang hoặc dấu chấm (tùy chọn)
        \d{3,4}             # Số thứ hai
        [\s\-\.]?           # Khoảng trắng, dấu gạch ngang hoặc dấu chấm (tùy chọn)
        \d{3,4}             # Số cuối cùng
        $                   # Kết thúc chuỗi
    ''', re.VERBOSE)
    
    return bool(phone_regex.match(phone))