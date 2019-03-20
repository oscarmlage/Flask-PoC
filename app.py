from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'stuff.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Create models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def __repr__(self):
        return "{}: {}".format(self.id, self.__str__())


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    available = db.Column(db.Boolean)

    def __str__(self):
        return self.name


admin = Admin(app, name='flask-poc', template_mode='bootstrap3')

# Add administrative views here
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Pet, db.session))

if __name__ == '__main__':

    db.drop_all()
    db.create_all()
    app.run()
