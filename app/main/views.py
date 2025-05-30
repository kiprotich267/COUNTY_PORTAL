from flask import Blueprint
from flask_security import login_required, current_user, roles_required

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@login_required
def home():
    return f"Welcome to county portal! {current_user.email}"

@main_bp.route('/about')
@login_required
def about():
    return "This is the about page of the county portal."


@main_bp.route('/dashboard')
@roles_required('super_admin')
def dashboard():
    return"This dashboard is accessible to admins only."



