from operator import methodcaller
from pickle import NONE
from flask import *
import sqlite3

from numpy import require


app = Flask(__name__)
app.debug = True

def db_connection():
    conn = NONE
    try:
        conn = sqlite3.connect('Recettes.db')
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route('/')
def main():
    return render_template("Home.html")

@app.route('/Entree/', methods=["GET"])
def entree():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM Recette")
        recettes = [
            dict(id_recette=row[0], type=row[1], name=row[2], ingredient=row[3], instruction=row[4])
            for row in cursor.fetchall()
        ]
        if recettes is not None:
            a = recettes
            print(a)
    return render_template("Entree.html", message = a)


if __name__ == '__main__':
    app.run()