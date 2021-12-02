def est_Reserve(cur, idPlace, idParking, debut, fin, typevehicule):
    # on on récupère l'ensemble des reservations(leur date) d'une place cible dans un parking'
    sql = f"SELECT r.debut, r.fin FROM Reservation r, place p ON r.numero_place=p.numero AND  r.parking_place = p.id_parking WHERE p.id_parking = {idParking} AND p.numero = {idPlace} AND p.type_vehicule ={typevehicule} "
    cur.execute(sql)
    reservation = cur.fetchone()
    flag = False
    while reservation:
        if (not (reservation[1] <= debut or fin <= reservation[0])):
            flag = True
            break
        reservation = cur.fetchone()
    return flag

def select_place(cur, id_parking, type_place, type_vehicule):
    sql = f"select numero from place where id_parking = {id_parking} AND type_place = '{type_place}' AND type_vehicule = '{type_vehicule}'"
    cur.execute(sql)
    place = cur.fetchall()
    print(place)
    if place == []:
        return place
    else:
        # faut checker reservation
        return place



def vehicule_disponible(cur, inmat, debut, fin): #renvoie bool qui indique dispo d un vehicule
    sql = "select r.debut, r.fin from reservation r where vehicule = {inmat};"
    cur.execute(sql)
    flag = true
    raw = cur.fetchone()
    while raw:
        if (not (reservation[1] <= debut or fin <= reservation[0])):
            flag = false
            break
        raw = cur.fetchone
    return flag

def selectionnerVehicule(cur,debut,fin):
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
    if vehicule_disponible(cur, inmat, debut, fin):
        return vehicule
    else:
        print(f"le vehicule {vehicule} n'est pas disponible, \n entrez [1] pour choisir un autre véhicule, \n entrez une autre touche pour quitter le menu de reservation")
        choix = input()
        if choix == 1:
            selectionnerVehicule(cur, debut, fin)
        else:
            menu_client(cur, conn, login)





def selectionnerParking(cur):
    nom_parking = input("entrez le nom du parking ou vous souhaiter réserver une place")
    sql = f"SELECT id_parking, zone FROM PARKING WHERE nom ='{nom_parking}'"
    cur.execute(sql)
    return cur.fetchone()


def reserver_place_cible(cur, debut, fin, inmat, client, idParking, idPlace):
    if est_Reserve(idPlace, idParking, debut, fin):
        print("reservation impossible, la place est déjà réservée")
    else:
        sql = f"INSERT into Reservation values (Default,'{debut}','{fin}','{inmat}','{client}','{idParking}','{idPlace}')"
        cur.execute(sql)


def check_abonnement_valide(cur, client, zone, debut, fin):
    sql = f"SELECT a.zone, a.debut, a.fin FROM abonnement a WHERE a.abonne='{client}';"
    cur.execute(sql)
    flag = False
    x = cur.fetchone()
    while x:
        if x == zone[0]:
            if zone[1] <= debut & fin <= zone[2]:
                flag = True
                break
        zone = cur.fetchone()
    return flag


def reserver_place_abo(cur, client,debut,fin,inmat,idParking):
    print('vous etes abonne a cette zone, la reservation est gratuite')

    sql = f"SELECT a.numero FROM Place a JOIN parking b ON a.id_parking = b.id_parking AND a.type_vehicule ={typevehicule};"
    cur.execute(sql)
    idPlace = cur.fetchone()
    while not est_Reserve(cur, idPlace, idParking, debut, fin, typevehicule):
        idPlace = cur.fetchone()
    reserver_place_cible(cur, debut, fin, inmat, client, idParking, idPlace)





def reserver_place(cur, client):
    type_caisse = 'internet'
    debut = input("entrez debut")
    fin = input("entrez fin")
    vehicule = selectionnerVehicule(cur,debut,fin)
    inmat = vehicule[0]
    typevehicule = vehicule[1]
    parking = selectionnerParking(cur)
    idParking = parking[0]
    zone = parking[1]
    if check_abonnement_valide:
        reserver_place_abo(cur, client,debut,fin,inmat,idParking)
    else:
        print("vous n'etes pas abonne a cette zone pour la période cible")
        loop = True
        choix=0
        while loop:
            print("Que voulez-vous faire?")
            print("[1] - Acheter un abonnement pour cette zone")
            print("[2] - Ne rien faire")
            choix = input("Entrez votre choix : ")
            if choix == "1":
                acheter_abonnement(cur, client, zone,type_caisse)
            elif choix == "2":
                loop = False
                menu_client(cur, conn, login)
