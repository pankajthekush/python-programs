from flask import Flask, escape, request ,render_template , url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '837384683748FSFA7'

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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form = form)
     

@app.route('/login')
def register():
    form = LoginForm()
    return render_template('Login.html',title='Login',form = form)
     


if __name__ == "__main__":
    app.run(debug=True)