from flask import Flask, render_template, request, redirect,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fsf5.db'

app.secret_key = 'secret'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    date_added = db.Column(db.DateTime, server_default = db.func.now())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    post = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False)
    date_added = db.Column(db.DateTime, server_default = db.func.now())


@app.route('/')

def index():
    return render_template("index.html")


@app.route('/register', methods = ['GET', 'POST'])

def register():
    user = User(username = request.form['username'], email=request.form['email'], password = request.form['password'])

    db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        print("ERROR: ", e)
        db.session.rollback() 

    user = User.query.filter_by(email = request.form['email']).first()

    session['username'] = user.username

    return redirect('/newsfeed')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = User.query.filter_by(email = request.form['email'], password = request.form['password']).first()

    if user == None:
        
        return "<h1 style='color:red'> Invalid username or password </h1>"

    session['username'] = user.username

    return redirect('/newsfeed')

@app.route('/addpost', methods = ['GET', 'POST'])

def addpost():
    post = Post(title= request.form['title'], post = request.form['post'], username = session['username'])

    db.session.add(post)

    try:
        db.session.commit()
    except Exception as e:
        print("ERROR: ", e)
        db.session.rollback() 

    return redirect('/newsfeed')


@app.route('/newsfeed')

def newsfeed():
    posts = Post.query.all()

    return render_template("newsfeed.html", posts= posts)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
        app.run(debug = True, port = 3000)