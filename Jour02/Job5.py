import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sophie",
    database = "laplateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(superficie) from etage")
resultat = cursor.fetchone()[0]

print("La superficie de La Plateforme est de", resultat, "m2")

cursor.close()
conn.close()