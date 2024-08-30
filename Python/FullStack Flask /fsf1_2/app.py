from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fsf1.db'

app.secret_key = 'secret'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    user_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)


@app.route('/')

def index():
    return render_template("index.html")


@app.route('/createuser', methods = ['GET', 'POST'])

def createuser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user_name = request.form['user_name']
    email = request.form['email']
    password = request.form['password']

    user = User(first_name = first_name, last_name = last_name, user_name = user_name, email = email, password = password)

    db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

    return redirect('/displayusers')

@app.route('/displayusers')
def displayusers():
    users = User.query.all() #retrieves all users [<User archie.andrews@email.com>, <User veronica.lodge@email.com>]


    return render_template("users.html", users = users)


@app.route('/login', methods = ['GET','POST'])

def login():
    username = request.form['user_name']
    password = request.form['password']

    user = User.query.filter_by(user_name = username, password = password).first()

    if user == None:
        return "<h1 style='color:red'> This user doesn't exist </h1>"

    return render_template("user.html", user = user)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
        app.run(debug = True, port = 3000)