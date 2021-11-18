#fonction pour consulter son solde de fidélité
def Solde_Fidelite(cur, idabonne):  #entrer l'id de l'utilisateur courant en paramètre
    sql = "SELECT points_fidelite FROM Abonne WHERE id_client = idabonne;"
    cur.execute(sql)
    print(" Votre solde de fidélité est ")
    raw = cur.fetchone()
    print (str(raw[0]))


#voir le nombre d'abonnements par zone
def Nombre_Abonnements_Zone(cur):
    sql_zone = "SELECT zone, Count(id_carte) FROM Abonnement GROUP BY zone;"
    cur.execute(sql_zone)
    raw = cur.fetchone()
    while raw:
        print("Dans la zone" + str(raw[0]) + ", il y a " + raw[1] + " abonnements")
        raw = cur.fetchone()


#voir le nombre de parkings par zone
def Nombre_Parkings_Zone(cur):
    sql_zone = "SELECT zone, Count(id_parking) FROM Parking GROUP BY zone;"
    cur.execute(sql_zone)
    raw = cur.fetchone()
    while raw:
        print("Dans la zone" + str(raw[0]) + ", il y a " + raw[1] + " parkings")
        raw = cur.fetchone()
