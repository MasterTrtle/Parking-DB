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


# Nombre de places prises par des abonnements pour un parking et un type de véhicule donné
def Nombre_Places_Abonnements(cur):
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
    #voir comment savoir cb d'abonnés sont sur un parking


# Nombre de places prises par des occasionnels pour un parking et un type de véhicule donné
def Nombre_Places_Occasionnels(cur):
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
    #voir comment savoir cb d'abonnés sont sur un parking
