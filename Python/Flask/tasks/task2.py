from flask import Flask

app = Flask(__name__)


@app.route('/home')

def home():
    return "<h1> Paws Rescue Center 🐾 </h1>"

@app.route('/about')

def about():
    return "<h1>About Us:</h1>" + '''

    <p> We are a non-profit organization working as an animal rescue. We aim to help you connect with the 
    purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission 
    is to promote the ideology "adopt, don't hop"! </p>

    '''

if __name__ == "__main__":
    app.run(debug = True, port = 3000)