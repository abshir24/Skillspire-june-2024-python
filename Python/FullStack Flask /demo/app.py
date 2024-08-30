from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.secret_key = 'secret'

db = SQLAlchemy(app)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key = True) #This field gets auto generated
    name = db.Column(db.String(200), nullable = False)
    phone_number = db.Column(db.Integer, nullable = False)
    country = db.Column(db.String(200), nullable = False)

@app.route('/')

def default():
    return render_template("form.html")


@app.route('/addcustomer', methods = ['GET','POST'])

def addcustomer():
    customer = Customer( name = "Customer Name" , phone_number = 5555555555, country = "USA")

    db.session.add(customer)

    try:
        db.session.commit()
    except Exception as e: 
        db.session.rollback()

  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
        app.run(debug = True, port = 3000)