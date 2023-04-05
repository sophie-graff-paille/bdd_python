import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sophie",
    database = "laplateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiants")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()