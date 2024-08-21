from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')
 
def root():
    return render_template("form.html")
 
@app.route('/formdata', methods = ['GET','POST'])
 
def formdata():
    username = request.form['username']
    password = request.form['password']
 
    return render_template("index.html", username=username, password=password)
 
if __name__ == "__main__":
    app.run(debug = True, port = 3000)