from pickle import FALSE
from flask import Flask
from flask import render_template
from flask import request
from models import *
import sqlite3

app = Flask(__name__)
app.debug = True 

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def home():
        username = request.form['usernames']
        password = request.form['MDP']
        con = sql.connect("BDCompte.db")
        cur = con.cursor() 
        cur = con.execute("SELECT * FROM Compte")
        compte = cur.fetchall()
        for i in range(len(compte)):
            if username == compte[i][1] and password == compte[i][2]:
                user = compte[i][1]
                return render_template("login.html", username = user)
            else:
                mess = "username or password is invalid"
                return render_template("login.html", mess = mess)

@app.route('/register', methods=['GET', 'POST'])
def Ajout():
        username = request.form['usernames']
        password = request.form['MDP']
        email = request.form['mail']
        con = sql.connect("BDCompte.db")
        cur = con.cursor() 
        cur = con.execute("INSERT INTO Compte (username, MDP, mail) VALUES " + str((username, password, email)))
        con.commit()
        con.close()
        return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
