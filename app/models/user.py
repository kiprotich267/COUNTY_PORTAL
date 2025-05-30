from app.extensions import db
from flask_security import UserMixin, RoleMixin
import uuid


# many-to-many relationship table for roles and users
# this is an association table for the many-to-many relationship
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                          db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

#   This is basic identity fields that comes with Flask-Security
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


    # Account status fields
    active = db.Column(db.Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())

    #flask-security required field for tokens, session, password management
    fs_uniquifier = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
# tracking fields
# TODO :

# relationships
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<User {self.email}>'

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
