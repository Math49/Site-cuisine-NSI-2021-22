from pickle import NONE
from flask import *
import sqlite3



app = Flask(__name__)
app.debug = True

#var global
id = 0
Connection = False
Compte = []

#connection base de donnée
def db_connection():
    conn = NONE
    try:
        conn = sqlite3.connect('Recettes.db')
    except sqlite3.Error as e:
        print(e)
    return conn

#Page Home
@app.route('/')
def main():
    global Compte
    global Connection
    return render_template("Home.html", compte = Compte, connect = Connection)

#Page Connection
@app.route('/Connection')
def connection():
    global Compte
    global Connection
    return render_template("Connect.html", compte = Compte, connection = Connection)


#Page Entrée
@app.route('/Entree', methods=["GET","POST"])
def entree():
    global id 
    global Compte
    global Connection
    commentaire = []
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Entree'")
    com = conn.cursor()
    com = conn.execute("SELECT * FROM Comment")
    comment = com.fetchall()
    recettes = cursor.fetchall()

    #Envoie des recettes
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Entree.html", recette = rect, compte = Compte, connection = Connection)
        if len(recettes) == 0:
            message = "Aucune recettes"
            return render_template("Entree.html", message = message, compte = Compte, connection = Connection)

    #Page Window
    if request.method == "POST":
        id = int(request.form.get("button"))
        
        for i in range(len(recettes)):
            if id == recettes[i][0]:
                a = recettes[i]
                name = a[2]
                ingr = a[3].split("//")
                instr = a[4].split("//")
        
        for a in comment:
            if a[3] == id:
                commentaire.append(a)

        return render_template("window.html", name = name, ingr = ingr, instr = instr, connect = Connection, comment = commentaire, compte = Compte)

#Page Plat
@app.route('/Plat', methods=["GET","POST"])
def plat():
    global id 
    global Compte
    global Connection
    commentaire = []
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Plat'")
    com = conn.cursor()
    com = conn.execute("SELECT * FROM Comment")
    comment = com.fetchall()
    recettes = cursor.fetchall()

    #Envoie des recettes
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Plat.html", recette = rect, compte = Compte, connection = Connection)
        if len(recettes) == 0:
            message = "Aucune recettes"
            return render_template("Plat.html", message = message, compte = Compte, connection = Connection)

    #Page Window
    if request.method == "POST":
        id = int(request.form.get("button"))

        for i in range(len(recettes)):
            if id == recettes[i][0]:
                a = recettes[i]
                name = a[2]
                ingr = a[3].split("//")
                instr = a[4].split("//")

        for a in comment:
            if a[3] == id:
                commentaire.append(a)
        
        return render_template("window.html", name = name, ingr = ingr, instr = instr, connect = Connection, comment = commentaire, compte = Compte)

#Page Dessert
@app.route('/Dessert', methods=["GET","POST"])
def dessert():
    global id 
    global Compte
    global Connection
    commentaire = []
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Dessert'")
    com = conn.cursor()
    com = conn.execute("SELECT * FROM Comment")
    comment = com.fetchall()
    recettes = cursor.fetchall()

    #Envoie des recettes
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Dessert.html", recette = rect, compte = Compte, connection = Connection)
        if len(recettes) == 0:
            message = "Aucune recettes"
            return render_template("Dessert.html", message = message, compte = Compte, connection = Connection)

    #Page Window
    if request.method == "POST":
        id = int(request.form.get("button"))
        
        for i in range(len(recettes)):
            if id == recettes[i][0]:
                a = recettes[i]
                name = a[2]
                ingr = a[3].split("//")
                instr = a[4].split("//")

        for a in comment:
            if a[3] == id:
                commentaire.append(a)

        return render_template("window.html", name = name, ingr = ingr, instr = instr, connect = Connection, comment = commentaire, compte = Compte)

#Page Divers
@app.route('/Divers', methods=["GET","POST"])
def divers():
    global Compte
    global Connection
    global id
    commentaire = []
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Recette WHERE type = 'Divers'")
    com = conn.cursor()
    com = conn.execute("SELECT * FROM Comment")
    comment = com.fetchall()
    recettes = cursor.fetchall()

    #Envoie des recettes
    if request.method == "GET":
        if len(recettes) != 0:
            rect = recettes
            return render_template("Divers.html", recette = rect, compte = Compte, connection = Connection)
        if len(recettes) == 0:
            message = "Aucune recettes"
            return render_template("Divers.html", message = message, compte = Compte, connection = Connection)
        

    #Page Window
    if request.method == "POST":
        id = int(request.form.get("button"))
        
        for i in range(len(recettes)):
            if id == recettes[i][0]:
                a = recettes[i]
                name = a[2]
                ingr = a[3].split("//")
                instr = a[4].split("//")

        for a in comment:
            if a[3] == id:
                commentaire.append(a)

        return render_template("window.html", name = name, ingr = ingr, instr = instr, connect = Connection, comment = commentaire, compte = Compte)

#Intégration du commentaire dans la base de donnée
@app.route('/comment', methods=["POST"])
def comment():
    global id
    global Connection
    global Compte
    if Connection == True:
        if request.method == 'POST':
            pseudo = Compte[1]
            text = request.form['text']
            a = id
            conn = db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO Comment (pseudo,text,id_recette) VALUES " + str((pseudo, text,a)) )
            conn.commit()
            conn.close()
            return render_template("Home.html")

#Système de login
@app.route('/login', methods=["POST"])
def login():
    global Connection
    global Compte
    email = request.form['login_email']
    password = request.form['login_password']
    con = db_connection()
    cur = con.cursor() 
    cur = con.execute("SELECT * FROM Compte")
    compte = cur.fetchall()
    for i in range(len(compte)):
        if email == compte[i][3] and password == compte[i][2]:
            user = compte[i][1]
            Connection = True
            Compte = compte[i]
            mess = "Vous êtes connecté"
            return render_template("Connect.html", username = user, login_mess = mess)
        else:
            mess = "l'email ou le mot de passe ne sont pas valide"
            return render_template("Connect.html", login_mess = mess)

#Système de register
@app.route('/register', methods=["POST"])
def register():
    con = db_connection()
    cur = con.cursor() 
    cur = con.execute("SELECT * FROM Compte")
    compte = cur.fetchall()
    username = request.form['register_username']
    password = request.form['register_password']
    email = request.form['register_email']
    for i in range(len(compte)):
        if email == compte[i][3]:
            mess = "Email déjà utilisé, veuillez utiliser une autre adresse Email"
            return render_template('Connect.html', register_mess = mess)

    cur = con.execute("INSERT INTO Compte (Username, Password, Email) VALUES " + str((username, password, email)))
    con.commit()
    con.close()
    mess = "Compte créé, veuillez vous connecter"
    return render_template('Connect.html', register_mess = mess)


if __name__ == '__main__':
    app.run()
