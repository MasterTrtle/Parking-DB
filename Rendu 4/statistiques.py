#fonction pour consulter son solde de fidélité
def printSoldeFidelite(cur, idabonne):
    sql = "SELECT points_fidelite FROM Abonne WHERE id_client = idabonne;"
    cur.execute(sql)
    print(" Votre solde de fidélité est ")
    raw = cur.fetchone()
    print (str(raw[0]))
