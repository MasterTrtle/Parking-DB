#fonction pour consulter son solde de fidélité
def Solde_Fidelite(cur, login):  #entrer l'id de l'utilisateur courant en paramètre
    sql = "SELECT Abonne.points_fidelite FROM Abonne, Compte WHERE Compte.login = '%s' and Compte.abonne = id_client;"%(login)
    cur.execute(sql)
    print(" \n Votre solde de fidélité est \n ")
    raw = cur.fetchone()
    print (str(raw[0]))



#voir le nombre d'abonnements par zone
def Nombre_Abonnements_Zone(cur):
    sql  = "SELECT zone, Count(id_carte) FROM Abonnement GROUP BY zone;"
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("\n Dans la zone :")
        print (str(raw[0]))
        print (" Nombre d'abonnements :" )
        print (str(raw[1]))
        raw = cur.fetchone()


#voir le nombre de parkings par zone
def Nombre_Parkings_Zone(cur):
    sql = "SELECT zone, Count(id_parking) FROM Parking GROUP BY zone;"
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("\n Dans la zone :")
        print (str(raw[0]))
        print (" Nombre de parkings :" )
        print (str(raw[1]))
        raw = cur.fetchone()

#Nombre de Places sur un parking donné pour un type de véhicule
def NbPlaces_Parking_Vehicule(cur):
    parking= int(input("Entrez 1 pour Mairie, 2 pour Chateau, 3 pour Usine, 4 pour Centrale, 5 pour Magasin, 6 pour Capitole "))  #id du parking associé est mise
    choixt=input("Entrez 1 pour vehicule simple, 2 pour camion, 3 pour deux roues ")
    if choixt=='1' :
        typeDuvehicule= 'vehicule simple'
    elif choixt=='2' :
        typeDuvehicule= 'camion'
    elif choixt=='3' :
        typeDuvehicule= 'deux roues'
    elif choixt :
        return

    sql  = "SELECT Count(*) FROM Place  WHERE id_parking = '%s' and type_vehicule = '%s';"%(parking, typeDuvehicule)
    cur.execute(sql)
    raw = cur.fetchone()
    print("\n Nombre de places disponible dans ce parking pour tel type de véhicules :")
    print (str(raw[0]))
    nb=str(raw[0])
    raw = cur.fetchone()

# Voir nb de paiement pour chaque type
def Nombre_Paiements(cur):
    sql  = "SELECT Count (type_caisse), type_caisse FROM Paiement GROUP BY type_caisse;"
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("\n Il y a ", str(raw[0]), "paiements avec", str(raw[1]))
        raw = cur.fetchone()

# Voir le nombre de clients abonnés et occasionnels
def Nombre_declients(cur):
    sql  = "SELECT Count (Abonne.id_client), Count (Occasionnel.id_client) FROM Abonne, Occasionnel;"
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("\n Il y a ", str(raw[0]), "abonnés qui utilisent ce service et ", str(raw[1]), "occasionnels")
        raw = cur.fetchone()
