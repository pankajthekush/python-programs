from flask import Flask, escape, request ,render_template , url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '837384683748FSFA7'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique = True,nullable=False)
    email = db.Column(db.String(120), unique = True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False , default='default.jpeg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='auther',lazy=True)

    def __repr__(self):
       return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     title =  db.Column(db.String(100),nullable=False)
     date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
     content =  db.Column(db.Text(20),nullable=False)
     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
     def __repr__(self):
         return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author' : 'pankaj Kumar',
        'title' : 'First post',
        'content' : 'first post content',
        'date_posted' : 'October 14 2019'
    },
        {
        'author' : 'Jane Doe ',
        'title' : 'Second post',
        'content' : 'Second post content',
        'date_posted' : 'October 14 2019'
    }


]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts ,title="New title")

@app.route('/about')
def about():
    return render_template("about.html",title='new new titl')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created {form.username.data}!',"success")
        return redirect(url_for('home'))

    return render_template('register.html',title='Register',form = RegistrationForm())
     

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('Login.html',title='Login',form =  LoginForm())
     


if __name__ == "__main__":
    app.run(debug=True)