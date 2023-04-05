import mysql.connector

conn = mysql.connector.connect( # connexion à la base de données
    host = "localhost", # adresse du serveur
    user = "root", # nom d'utilisateur
    password = "sophie", # mot de passe
    database = "soentreprise" # nom de la base de données
)

cursor = conn.cursor() # création d'un curseur

# création des tables et insertion des données :

# cursor.execute("CREATE TABLE employes (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(150) NOT NULL, prenom VARCHAR(150) NOT NULL, salaire INT NOT NULL, id_service INT NOT NULL)")
# cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('Graff', 'Sophie', 3500, 4), ('Graff', 'Aurélie', 4800, 2), ('Irving', 'John', 5000, 1), ('Rossellini', 'Isabella', 1800, 3)")

cursor.execute("SELECT * FROM employes WHERE salaire > 3000")

# cursor.execute("CREATE TABLE services (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(150) NOT NULL)")
# cursor.execute("INSERT INTO services (nom) VALUES ('Comptabilité'), ('Informatique'), ('Ressources Humaines'), ('Direction')")

class Crud:
    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    # bien appeler la bonne table dans la requête SQL avec USE <nom de la table> avant de faire la requête

    def Create(self):
        cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", (self.nom, self.prenom, self.salaire, self.id_service)) # %s = paramètre fictif à remplacer par les valeurs des variables
        conn.commit()

    def Read(self):
        cursor.execute("SELECT * FROM employes")
        resultat = cursor.fetchall()
        for i in resultat:
            print(i)

    def Update(self):
        cursor.execute("UPDATE employes SET salaire = 5000 WHERE id = 1")
        conn.commit()

    def Delete(self):
        cursor.execute("DELETE FROM employes WHERE id = 1")
        conn.commit()

resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()