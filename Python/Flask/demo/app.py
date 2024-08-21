from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')

def root():
    return render_template("form.html")

@app.route('/formdata', methods = ['GET','POST'])

def formdata():
    session['username'] = request.form['username']
    session['password'] = request.form['password']

    print(session)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 3000)