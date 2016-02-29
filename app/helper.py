from models import User

def validate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if (user):
        return True
    return False