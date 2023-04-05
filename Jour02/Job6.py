import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sophie",
    database = "laplateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(capacite) from salles")
resultat = cursor.fetchone()[0]

print("La capacité de toutes les salles est de :", resultat)

cursor.close()
conn.close()