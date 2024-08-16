from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def root():
    return render_template("index.html", number = 5)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)

