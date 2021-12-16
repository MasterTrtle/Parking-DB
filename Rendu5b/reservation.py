from abonnement import acheter_abonnement
import datetime

def est_Reserve(cur, idPlace, idParking, debut, fin, typevehicule):
    # on on récupère l'ensemble des reservations
    sql = "SELECT r.debut, r.fin FROM Reservation r " \
          "JOIN place p ON r.numero_place=p.numero AND  r.parking_place =p.id_parking " \
          "WHERE p.id_parking = '%s' AND p.numero = '%s' AND p.type_vehicule ='%s'"%(idParking, idPlace, typevehicule)
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

def selectionnerVehicule(cur,client):
    sql = "SELECT v.immat, v.type_vehicule FROM Vehicule v where v.propriétaire = %s;"%client
    cur.execute(sql)
    vehicule = cur.fetchone()
    i = 0
    while vehicule:
        print("pour réserver une place pour le véhicule de matricule", vehicule[0], "entrez", i)
        i += 1
        vehicule = cur.fetchone()
    choix = int(input())
    cur.execute(sql)
    vehicule = cur.fetchone()
    i = 0
    while i < choix:
        i += 1
        vehicule = cur.fetchone()
    return vehicule


def selectionnerParking(cur):
    nom_parking = input("entrez le nom du parking ou vous souhaiter réserver une place")
    sql = "SELECT id_parking, zone FROM PARKING WHERE nom ='%s'" % nom_parking

    cur.execute(sql)
    return cur.fetchone()


def reserver_place_cible(cur, debut, fin, idvehicule, client, idParking, zone, idPlace):
    sql = "INSERT into Reservation values ('%s','%s','%s','%s','%s','%s','%s')"%(debut, fin, idvehicule, client, idParking, zone, idPlace)
    cur.execute(sql)
    print("Reservation réussie")

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


def reserver_place(cur,client,conn):
    cur.execute("select abonne from compte where login='%s';" % client)
    idclient = cur.fetchone()
    vehicule = selectionnerVehicule(cur,idclient[0])
    idvehicule = vehicule[0]
    typevehicule = vehicule[1]
    debut = datetime.date(int(input("Année de Début")),int(input("Mois de début")),int(input("Jour de début")))
    fin = datetime.date(int(input("Année de Fin")),int(input("Mois de Fin")),int(input("Jour de Fin")))
    parking = selectionnerParking(cur)
    idParking = parking[0]
    zone = parking[1]
    if check_abonnement_valide:
        print('vous etes abonne a cette zone, la reservation est gratuite')
        sql = "SELECT numero FROM Place WHERE type_vehicule ='%s' AND id_parking='%s' AND zone_parking='%s';" %(typevehicule,idParking,zone)
        cur.execute(sql)
        idPlace = cur.fetchone()
        if idPlace is None:print("Il n'y a plus de place libre pour ce vehicule dans le parking");return
        else:
            while est_Reserve(cur, idPlace[0], idParking, debut, fin, typevehicule):
                idPlace = cur.fetchone()
                if idPlace is None:print("Il n'y a plus de place libre pour ce vehicule dans le parking");return
            try:
                reserver_place_cible(cur, debut, fin, idvehicule, idclient[0], idParking, zone, idPlace[0])
            except Exception as error:
                print("Erreur :",error);return;
            conn.commit()
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
