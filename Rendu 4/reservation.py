from abonnement import acheter_abonnement

def est_Reserve(cur, idPlace, idParking, debut, fin, typevehicule):
    # on on récupère l'ensemble des reservations
    sql = "SELECT r.debut, r.fin FROM Reservation r, place p ON r.numero_place=p.numero AND  r.parking_place = " \
          "p.id_parking WHERE p.id_parking = %d AND p.numero = %d AND p.type_vehicule =%s " % idParking, idPlace, \
          typevehicule
    # a voir si on trie pour optimiser
    cur.execute(sql)
    reservation = cur.fetchone()
    flag = False
    while reservation:
        if (not (reservation[1] <= debut or fin <= reservation[0])):
            flag = True
            break
        reservation = cur.fetchone()
    return flag;

def selectionnerVehicule(cur):
    sql = "SELECT v.immat, v.type_vehicule FROM Vehicule v JOIN Client c ON v.propriétaire = c.id_client;"
    cur.execute(sql)
    vehicule = cur.fetchone()
    i = 0
    while vehicule:
        print("pour réserver une place pour le véhicule de matricule", vehicule[0], "entrez", i)
        i += 1
        vehicule = cur.fetchone()
    choix = input()
    cur.execute(sql)
    vehicule = cur.fetchone()
    i = 0
    while i < int(choix):
        i += 1
        vehicule = cur.fetchone()
    return vehicule


def selectionnerParking(cur):
    nom_parking = input("entrez le nom du parking ou vous souhaiter réserver une place")
    sql = """SELECT id_parking, zone FROM PARKING WHERE nom ='%s'""" % nom_parking

    cur.execute(sql)
    return cur.fetchone()


def reserver_place_cible(cur, debut, fin, idvehicule, client, idParking, zone, idPlace):
    if est_Reserve(idPlace, idParking, debut, fin):
        print("reservation impossible, la place est déjà réservée")
    else:
        sql = "INSERT into Reservation values ('%s','%s','%s','%s','%s','%s','%s')", (
            debut, fin, idvehicule, client, idParking, zone, idPlace)
        cur.execute(sql)


def check_abonnement_valide(cur, client, zone, debut, fin):
    sql = "SELECT a.zone, a.debut, a.fin FROM abonnement a WHERE a.abonne='%s';"%client
    flag = False
    x = cur.fetchone()
    while x:
        if x == zone[0]:
            if zone[1] <= debut & fin <= zone[2]:
                flag = True
                break
        zone = cur.fetchone()
    return flag


def reserver_place(cur, client):
    vehicule = selectionnerVehicule(cur)
    idvehicule = vehicule[0]
    typevehicule = vehicule[1]
    debut = input("entrez debut")
    fin = input("entrez fin")
    parking = selectionnerParking(cur)
    idParking = parking[0]
    zone = parking[1]
    if check_abonnement_valide:
        print('vous etes abonne a cette zone, la reservation est gratuite')
        sql = "SELECT a.numero FROM Place a JOIN parking b ON a.id_parking = b.id_parking AND a.type_vehicule =%s;" % typevehicule
        cur.execute(sql)
        idPlace = cur.fetchone()
        while not est_Reserve(cur, idPlace, idParking, debut, fin, typevehicule):
            idPlace = cur.fetchone()
        reserver_place_cible(cur, debut, fin, idvehicule, client, idParking, zone, idPlace)
    else:
        print("vous n'etes pas abonne a cette zone")
        loop = 'true'
        while (loop == 'true'):
            print("Que voulez-vous faire?")
            print("[1] - Acheter un abonnement pour cette zone")
            print("[2] - Ne rien faire")
            choix = input("Entrez votre choix : ")
        if choix=="2":
            return
        elif choix=="1":
            acheter_abonnement(cur,client,zone)
