from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def root():
    # information = {
    #     "name": "Abshir",
    #     "food": "veggie bowl",
    #     "vacation": "Mexico"
    # }


    # return render_template("index.html", name = "Abshir", food = "veggie bowl", vacation = "Mexico")

    # return render_template("index.html", userinfo = information )
    
    return render_template("part2.html")


if __name__ == "__main__":
    app.run(debug = True, port = 3000)

