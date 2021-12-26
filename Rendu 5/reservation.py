import abonnement
import menu
from generation import input_date
from datetime import datetime


def est_Reserve(cur, idPlace, idParking, debut, fin):
    # on on récupère l'ensemble des reservations(leur date) d'une place cible dans un parking'
    sql = f"SELECT debut, fin FROM Reservation WHERE numero_place = {idPlace} AND  parking_place = {idParking}"
    cur.execute(sql)
    reservation = cur.fetchone()
    if reservation is None:
        return True
    flag = False
    while reservation:
        if not (reservation[1] <= debut or fin <= reservation[0]):
            flag = True
            break
        reservation = cur.fetchone()
    return flag

def vehicule_disponible(cur, inmat, debut, fin):  # renvoie bool qui indique dispo d un vehicule
    sql = f"select r.debut, r.fin from reservation r where vehicule = '{inmat}';"
    cur.execute(sql)
    flag = True
    raw = cur.fetchone()
    while raw:
        if (not (raw[1] <= debut or fin <= raw[0])):
            flag = False
            break
        raw = cur.fetchone
    return flag


def selectionnerVehicule(cur, debut, fin, client):
    sql = f"SELECT v.immat, v.type_vehicule FROM Vehicule v  where v.proprietaire = {client};"
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
    if vehicule_disponible(cur, vehicule[0], debut, fin):
        return vehicule
    else:
        print(
            f"le vehicule {vehicule} n'est pas disponible, \n entrez [1] pour choisir un autre véhicule, \n entrez une autre touche pour quitter le menu de reservation")
        choix = input()
        if choix == 1:
            selectionnerVehicule(cur, debut, fin, client)
        else:
            menu.menu_client(cur, client)


def selectionnerParking(cur):
    sql = "SELECT * FROM parking"
    cur.execute(sql)
    parking = cur.fetchone()
    i = 0
    while parking:
        adresse = parking[3]
        nom = parking[2]
        print(f"pour réserver une place dans le parking {nom} d'adresse {adresse}, entrez [{i}]")
        i += 1
        parking = cur.fetchone()
    choix = input()
    sql = "SELECT id_parking, zone FROM parking"
    cur.execute(sql)
    parking = cur.fetchone()
    i = 0

    while i < int(choix):
        i += 1
        parking = cur.fetchone()
    return parking


def reserver_place_cible(cur, debut, fin, inmat, client, idParking, idPlace):
    sql = f"INSERT into Reservation values (Default,'{debut}','{fin}','{inmat}','{client}','{idParking}',{idPlace})"
    cur.execute(sql)


def check_abonnement_valide(cur, client, zone, debut, fin):
    debut = datetime.strptime(debut, "%Y-%m-%d")
    debut = debut.date()
    fin = datetime.strptime(fin, "%Y-%m-%d")
    fin = fin.date()

    sql = f"SELECT a.zone, a.debut, a.fin FROM abonnement a WHERE a.abonne='{client}';"
    cur.execute(sql)
    flag = False
    x = cur.fetchone()
    while x:
        if x[0] == zone:
            if (x[1] <= debut) & (fin <= x[2]):
                flag = True
                break
        x = cur.fetchone()
    return flag


def reserver_place_abo(cur, client, debut, fin, inmat, idParking, typevehicule, typePlace):
    print('vous etes abonne a cette zone, la reservation est gratuite')

    sql = f"SELECT numero FROM Place WHERE id_parking={idParking} AND type_vehicule ='{typevehicule}' AND type_place ='{typePlace}';"
    cur.execute(sql)
    id_place = cur.fetchone()
    if id_place is None:
        print("Réservation impossible, il n'y a pas de place disponible")
        return
    while id_place and (not est_Reserve(cur, id_place[0], idParking, debut, fin)):
        id_place = cur.fetchone()
    reserver_place_cible(cur, debut, fin, inmat, client, idParking, id_place[0])


def reserver_place(cur, client,conn):
    type_caisse = 'internet'
    debut = input_date("entrez debut")
    fin = input_date("entrez fin")

    vehicule = selectionnerVehicule(cur, debut, fin, client)
    inmat = vehicule[0]
    typevehicule = vehicule[1]

    type_place = ['couverte', 'plein air couverte', 'plein air']
    print("Choississez le type de place")
    print("[0] - Place couverte")
    print("[1] - Place plein air couverte")
    print("[2] - plein air")
    choix_place = int(input())
    type_place = type_place[choix_place]

    parking = selectionnerParking(cur)
    idParking = parking[0]
    zone = parking[1]

    if check_abonnement_valide(cur, client, zone, debut, fin):
        reserver_place_abo(cur, client, debut, fin, inmat, idParking, typevehicule, type_place)
    else:
        print("vous n'etes pas abonne a cette zone pour la période cible")
        loop = True
        choix = 0
        while loop:
            print("Que voulez-vous faire?")
            print("[1] - Acheter un abonnement pour cette zone")
            print("[2] - Ne rien faire")
            choix = input("Entrez votre choix : ")
            if choix == "1":
                abonnement.acheter_abonnement(cur, client, zone, type_caisse)
                if check_abonnement_valide(cur, client, zone, debut, fin):
                    reserver_place_abo(cur, client, debut, fin, inmat, idParking, typevehicule, type_place)
                    loop = False
                else:
                    print("le nouveau abonnement n'est toujours pas valide")
            elif choix == "2":
                loop = False
                menu.menu_client(cur, client)
    return menu.menu_client(cur, client)


def sortie_parking(cur):
    print("\n--- Signaler une sortie de véhicule---")
    
    #Indiquer la plaque du véhicule sortant
    try :
        immat=str(input("Entrez la plaque d'immatriculation du véhicule sortant : "))
    except ValueError :
        print("Valeur entrée incorrecte")
        immat=str(input("Entrez la plaque d'immatriculation du véhicule sortant : "))
        
    now = datetime.now()
    sql= "UPDATE Reservation SET fin='%s' WHERE vehicule='%s' AND fin IS NULL;"%(now,immat)
    cur.execute(sql)
    if cur.rowcount==0:
        sql= "UPDATE Ticket SET fin='%s' WHERE immat='%s' AND fin IS NULL;"%(now,immat)
        cur.execute(sql)
        if cur.rowcount==0:
            print("/!\ La requête a échoué. Veuillez vérifier que la plaque est correcte.")
            return
    print('* Modification effectuée !')
    return
    