from operator import methodcaller
from pickle import NONE
from flask import *
import sqlite3
from django import *

from numpy import require


app = Flask(__name__)
app.debug = True

id = 0
#connection base de donnée
def db_connection():
    conn = NONE
    try:
        conn = sqlite3.connect('Recettes.db')
    except sqlite3.Error as e:
        print(e)
    return conn

#main page
@app.route('/')
def main():
    return render_template("Home.html")

#entrée page
@app.route('/Entree', methods=["GET","POST"])
def entree():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette")
    recettes = cursor.fetchall()
    if request.method == "GET":
        if recettes is not None:
            rect = recettes
            return render_template("Entree.html", recette = rect)

    #button + window page
    if request.method == "POST":
        print("form : ",request.form.get("test"))
        global id 
        id = int(request.form.get("test"))-1
        print(id)
        
        i = recettes[id]

        name = i[2]
        ingr = i[3].split("//")
        instr = i[4].split("//")
        print(ingr)
        print(instr)
        return render_template("window.html", name = name, ingr = ingr, instr = instr)


if __name__ == '__main__':
    app.run()
