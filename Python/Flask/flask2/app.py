from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')

def index():
   return render_template("index.html") 

@app.route('/display-name/<name>')

def display_name(name):
    return render_template("name.html", name = name)

@app.route('/display-food/<food>')

def display_food(food):
    return render_template("food.html", food = food)

@app.route('/display-vacation/<vacation>')

def display_vacation(vacation):
    return render_template("vacation.html", vacation = vacation)

 
if __name__ == "__main__":
    app.run(debug = True, port = 3000)