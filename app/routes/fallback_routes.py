from flask import Blueprint
fallback_bp = Blueprint('fallback',__name__)

@fallback_bp.route('/', defaults={'path': ''})
@fallback_bp.route('/<path:path>')
def catch_all(path):
    return render_template('base.html')