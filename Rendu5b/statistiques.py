#fonction pour consulter son solde de fidélité
def Solde_Fidelite(cur, login):  #entrer l'id de l'utilisateur courant en paramètre
    sql = "SELECT Abonne.points_fidelite FROM Abonne, Compte WHERE Compte.login = '%s' and Compte.abonne = id_client;"%(login)
    cur.execute(sql)
    print(" \n Votre solde de fidélité est \n ")
    raw = cur.fetchone()
    print (str(raw[0]))



#voir le nombre d'abonnements par zone
def Nombre_Abonnements_Zone(cur):
    sql_zone = "SELECT zone, Count(id_carte) FROM Abonnement GROUP BY zone;"
    cur.execute(sql_zone)
    raw = cur.fetchone()
    while raw:
        print("\n Dans la zone :")
        print (str(raw[0]))
        print (" Nombre d'abonnements :" )
        print (str(raw[1]))
        raw = cur.fetchone()


#voir le nombre de parkings par zone
def Nombre_Parkings_Zone(cur):
    sql_zone = "SELECT zone, Count(id_parking) FROM Parking GROUP BY zone;"
    cur.execute(sql_zone)
    raw = cur.fetchone()
    while raw:
        print("\n Dans la zone :")
        print (str(raw[0]))
        print (" Nombre de parkings :" )
        print (str(raw[1]))
        raw = cur.fetchone()
