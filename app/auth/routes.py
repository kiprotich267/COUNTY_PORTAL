from flask import Blueprint
from flask_security import login_required, current_user
from app.models.user import User

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/profile')
@login_required
def profile():
    "This is the current user information"
    # return {
    #     "id": current_user.id,
    #     "email": current_user.email,
    #     "active": current_user.active,
    # }

    return f"{current_user.email} is logged in and active: {current_user.active}"

@auth_bp.route('/users')
@login_required
def users():
    all_users = User.query.all()
    for user in all_users:
        return f"{user.email} {user.roles}"

@auth_bp.route('/logout')
@login_required
def logout():
    return f"{current_user.email} has logged out."
