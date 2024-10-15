from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import  validates
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

#Association Table for many to many relationship between users and groups
user_groups = db.Table('user_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ("-posts.user", "-groups.users")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    posts = db.relationship("Post", back_populates="user")
    groups = db.relationship("Group", secondary=user_groups, back_populates="users")
    # comments = db.relationship("Comment", back_populates="user")

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email or "." not in email:
            raise ValueError("Email must contain both '@' and '.' to be valid")
        return email


class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    serializer_rules = ("-user",)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="posts")
    # comments = db.relationship("Comment", back_populates="post")

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    serializer_rules = ("-users.groups", "-users.posts")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    users = db.relationship("User", secondary=user_groups, back_populates="groups")


# class Comment(db.Model):
#     __tablename__ = "comments"

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))

#     post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

#     post = db.relationship("User", back_populates="comments")
#     user = db.relationship("Post", back_populates="comments")