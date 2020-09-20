# from flask_sqlalchemy import SQLAlchemy
#
# db = None
#
# def init(app):
#     db = SQLAlchemy(app)
#
#
# def add_user(name, email):
#     admin = User(username=name, email=email)
#     db.session.add(admin)
#     db.session.commit()
#
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username