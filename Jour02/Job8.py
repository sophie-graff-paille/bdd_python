import mysql.connector

conn = mysql.connector.connect( # connexion à la base de données
    host = "localhost", # adresse du serveur
    user = "root", # nom d'utilisateur
    password = "sophie", # mot de passe
    database = "zoo" # nom de la base de données
)

cursor = conn.cursor() # création d'un curseur

# création des tables et insertion des données :

# cursor.execute("CREATE TABLE animal (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(150) NOT NULL, race VARCHAR(150) NOT NULL, id_type_cage INT NOT NULL, date_naissance DATE NOT NULL, pays_origine VARCHAR(150) NOT NULL)")
# cursor.execute("INSERT INTO animal (nom, race, id_type_cage, date_naissance, pays_origine) VALUES ('Clarence', 'Lion', 1, '2015-07-31', 'Afrique du Sud'), ('Kaa', 'Python', 2, '2020-11-04', 'Brésil'), ('Baghera', 'Panthère noire', 1, '2012-01-31', 'Indonésie'), ('Taz', 'Diable', 3, '2022-04-18', 'Tasmanie')")

# cursor.execute("CREATE TABLE cage (id INT PRIMARY KEY AUTO_INCREMENT, superficie INT NOT NULL, capacité INT)")
# cursor.execute("INSERT INTO cage (superficie, capacité) VALUES (100, 1), (50, 1), (30, 1)")
# conn.commit()

class Crudanimal:
    def __init__(self, nom, race, id_type_cage, date_naissance, pays_origine):
        self.nom = nom
        self.race = race
        self.id_type_cage = id_type_cage
        self.date_naissance = date_naissance
        self.pays_origine = pays_origine

    # bien appeler la bonne table dans la requête SQL avec USE <nom de la table> avant de faire la requête

    def Create(self):
        cursor.execute("INSERT INTO animal (nom, race, id_type_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)", (self.nom, self.race, self.id_type_cage, self.date_naissance, self.pays_origine)) # %s = paramètre fictif à remplacer par les valeurs des variables
        conn.commit()

    def Read(self):
        cursor.execute("SELECT * FROM animal")
        resultat = cursor.fetchall()
        for i in resultat:
            print(i)

    def Update(self):
        cursor.execute("UPDATE animal SET id_type_cage = 1 WHERE id = 1")
        conn.commit()

    def Delete(self):
        cursor.execute("DELETE FROM animal WHERE id = 1")
        conn.commit()

class Crudcage:
    def __init__(self, superficie, capacité):
        self.superficie = superficie
        self.capacité = capacité

    # bien appeler la bonne table dans la requête SQL avec USE <nom de la table> avant de faire la requête

    def Create(self):
        cursor.execute("INSERT INTO cage (superficie, capacité) VALUES (%s, %s)", (self.superficie, self.capacité)) # %s = paramètre fictif à remplacer par les valeurs des variables
        conn.commit()

    def Read(self):
        cursor.execute("SELECT * FROM cage")
        resultat = cursor.fetchall()
        for i in resultat:
            print(i)

    def Update(self):
        cursor.execute("UPDATE cage SET superficie = 100 WHERE id = 1")
        conn.commit()

    def Delete(self):
        cursor.execute("DELETE FROM cage WHERE id = 1")
        conn.commit()

cursor.execute("SELECT * FROM animal WHERE id_type_cage != 0")
resultat = cursor.fetchall()
print(resultat)
cursor.close()

cursor = conn.cursor()

cursor.execute("SELECT SUM(superficie) FROM cage")
resultat = cursor.fetchall()[0][0]
print("La superficie totale des cages est de", resultat, "m2")

cursor.close()
conn.close()