from pickle import NONE
from flask import *
import sqlite3



app = Flask(__name__)
app.debug = True

id = 0
commentaire = []

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

@app.route('/Connection')
def connection():
    return render_template("Connect.html")

#entrée page
@app.route('/Entree', methods=["GET","POST"])
def entree():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Entree'")
    recettes = cursor.fetchall()
    print(recettes)
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Entree.html", recette = rect)
        if len(recettes) == 0:
            message = "Aucune recettes"
            print(message)
            return render_template("Entree.html", message = message)

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

#plat page
@app.route('/Plat', methods=["GET","POST"])
def plat():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Plat'")
    com = conn.cursor()
    com = conn.execute("SELECT * FROM Comment")
    comment = com.fetchall()
    recettes = cursor.fetchall()
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Plat.html", recette = rect)
        if len(recettes) == 0:
            message = "Aucune recettes"
            print(message)
            return render_template("Plat.html", message = message)

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

        for a in comment:
            if a[3] == id+1:
                commentaire.append(a)
        
        return render_template("window.html", name = name, ingr = ingr, instr = instr, comment = commentaire)

#dessert page
@app.route('/Dessert', methods=["GET","POST"])
def dessert():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Dessert'")
    recettes = cursor.fetchall()
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Dessert.html", recette = rect)
        if len(recettes) == 0:
            message = "Aucune recettes"
            print(message)
            return render_template("Dessert.html", message = message)

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

#divert page
@app.route('/Divers', methods=["GET","POST"])
def divers():
    global id
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Divers'")
    recettes = cursor.fetchall()
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Divers.html", recette = rect)
        if len(recettes) == 0:
            message = "Aucune recettes"
            print(message)
            return render_template("Divers.html", message = message)
        

    #button + window page
    if request.method == "POST":
        print("form : ",request.form.get("test"))
        id = int(request.form.get("test"))-1
        print(id)
        
        i = recettes[id]

        name = i[2]
        ingr = i[3].split("//")
        instr = i[4].split("//")
        print(ingr)
        print(instr)
        return render_template("window.html", name = name, ingr = ingr, instr = instr)
    
@app.route('/comment', methods=["POST"])
def comment():
    global id
    print("comment")
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        text = request.form['text']
        a = id+1
        conn = db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Comment (pseudo,text,id_recette) VALUES " + str((pseudo, text,a)) )
        conn.commit()
        conn.close()

        return render_template("Home.html")



if __name__ == '__main__':
    app.run()
