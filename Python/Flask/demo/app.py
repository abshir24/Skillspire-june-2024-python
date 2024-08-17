from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<number>')

def root(number):
   
    return render_template("index.html", number = number)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)

