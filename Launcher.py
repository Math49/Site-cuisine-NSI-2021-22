from flask import *

import sqlite3

bb = sqlite3.connect("Recettes.db")

c = bb.cursor()



app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template("Home.html")

@app.route('/Entree/')
def entree():
    return render_template("Entree.html")


@app.route('/', methods=['POST'])
def text_box():
    for a in c.execute("SELECT * FROM Recette"):
        return render_template("Home.html", message = a)



if __name__ == '__main__':
    app.run()