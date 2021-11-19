from datetime import datetime
import connect



def est_Reserve(idPlace, idParking, debut, fin):
    #on on récupère l'ensemble des reservation
    sql = "SELECT r.debut, r.fin FROM Reservation r, place p ON r.numero_place=p.numero AND  r.parking_place = p.id_parking WHERE p.id_parking = %d AND p.numero = %d "%idParking,idPlace 
    #a voir si on trie pour optimiser
    conn = connect.get_connection()
    allReservation = conn.cursor()
    allReservation.execute(sql)
    reservation = allReservation.fetchone()
    flag = False

    while reservation:
        if (not (reservation[1]<=debut or fin<= reservation[0])):
            flag = True
            break
        reservation = allReservation.fetchone()

    return flag;



def reserverPlace(debut, fin, idvehicule, client, idParking,zone, idPlace):

    if est_Reserve(idPlace, idParking,debut,fin):
        print("reservation impossible, la place est déjà réservée")
    else:
        debut = debut.strftime('%Y-%m-%d %H:%M:%S')
        fin = fin.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT into Reservation values ('%s','%s','%s','%s','%s','%s','%s')", (debut, fin, idvehicule, client, idParking,zone, idPlace)
        conn = connect.get_connection()
        cur = conn.cursor()
        cur.execute(sql)



def nombreTotalPlaceDispo(date):
