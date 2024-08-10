from flask import Flask

app = Flask(__name__)

@app.route('/')

def root():
    return "<h1> 0 </h1>"

@app.route('/one')

def routeOne():
    return "<h1> 1 </h1>"
    
@app.route('/three')

def routeTwo():
    return "3"

if __name__ == "__main__":
    app.run(debug = True, port = 3000)

