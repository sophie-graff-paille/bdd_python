import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sophie",
    database = "laplateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT nom, capacite from salles")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()