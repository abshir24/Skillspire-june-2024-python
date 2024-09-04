from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fsf1.db'

app.secret_key = 'secret'

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    date_added = db.Column(db.DateTime, server_default = db.func.now()) #auto-generates a timestamp for when the record
    #was added


@app.route('/')

def index():
    all_courses = Course.query.all()

    return render_template("index.html", courses = all_courses)

@app.route('/addcourse', methods = ["GET","POST"])

def addcourse():
    course = Course(name = request.form['course_name'], description = request.form['description'])

    db.session.add(course)

    try:
        db.session.commit()
    except Exception as e:
        print("ERROR: ", e)
        db.session.rollback()

    return redirect('/')

@app.route('/remove/<int:course_id>')

def removecourse(course_id):
    course = Course.query.get(course_id)

    return render_template('deletecourse.html', course = course )


@app.route('/delete/<int:course_id>')

def delete(course_id):
    course = Course.query.get(course_id)

    db.session.delete(course)

    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
        app.run(debug = True, port = 3000)