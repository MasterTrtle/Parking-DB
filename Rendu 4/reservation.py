def est_Reserve(cur,idPlace, idParking, debut, fin,typevehicule):
    #on on récupère l'ensemble des reservations
    sql = "SELECT r.debut, r.fin FROM Reservation r, place p ON r.numero_place=p.numero AND  r.parking_place = p.id_parking WHERE p.id_parking = %d AND p.numero = %d AND p.type_vehicule =%s "%idParking,idPlace,typevehicule
    #a voir si on trie pour optimiser
    cur.execute(sql)
    reservation = cur.fetchone()
    flag = False
    while reservation:
        if (not (reservation[1]<=debut or fin<= reservation[0])):
            flag = True
            break
        reservation = cur.fetchone()
    return flag;

def selectionnerVehicule(cur):
    sql = "SELECT v.immat v.type_vehicule FROM Vehicule v JOIN Client c ON v.propietaire = c.id_client;"
    cur.execute(sql)
    vehicule=cur.fetchone()
    i=0
    while vehicule:
        print("pour réserver une place pour le véhicule entrez",i)
        i+=1
        vehicule = cur.fetchone()
    choix = input()
    cur.execute(sql)
    vehicule=cur.fetchone()
    i=0
    while i<choix:
        i+=1
        vehicule = cur.fetchone()
    return vehicule

def selectionnerParking(cur):
    nom_parking =input("entrez le nom du parking ou vous souhaiter réserver une place")
    sql = "SELECT idParking, zone FROM PARKING WHERE nom = %s;"%nom_parking
    cur.execute(sql)
    return cur.fetchone()

def reserver_place_cible(cur,debut, fin, idvehicule, client, idParking,zone, idPlace):
    if est_Reserve(idPlace, idParking,debut,fin):
        print("reservation impossible, la place est déjà réservée")
    else:
        sql = "INSERT into Reservation values ('%s','%s','%s','%s','%s','%s','%s')", (debut, fin, idvehicule, client, idParking,zone, idPlace)
        cur.execute(sql)

def reserver_place(cur,client):
    vehicule = selectionnerVehicule(cur)
    idvehicule = vehicule[0]
    typevehicule = vehicule[1]
    debut = input("entrez debut")
    fin = input("entrez fin")
    debut = debut.strftime('%Y-%m-%d %H:%M:%S')
    fin = fin.strftime('%Y-%m-%d %H:%M:%S')
    parking = selectionnerParking(cur)
    idParking = parking[0]
    zone = parking[1]
    sql ="SELECT p.idplace FROM Place a JOIN parking b ON a.id_parkiNG = b.id_parking AND p.type_vehicule =%s;"%typevehicule
    cur.execute(sql)
    idPlace=cur.fetchone()
    while not est_Reserve(cur,idPlace, idParking, debut, fin,typevehicule):
        idPlace = cur.fetchone()
    reserver_place_cible(cur,debut, fin, idvehicule, client, idParking,zone, idPlace)
