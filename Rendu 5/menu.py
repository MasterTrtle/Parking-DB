import zone
import reservation
import statistiques
import entree_sortie


def menu_employe(cur,conn,login):
    print("---Bienvenue dans l'espace employé---")
    choix=0
    loop='true'
    while (loop=='true'):
        print("Que voulez-vous faire?")
        print("[1] - Changer un parking de zone")
        print("[2] - Changer le tarif d'une zone")
        print("[3] - Voir le nombre d'abonnements par zone")
        print("[4] - Voir le nombre de parkings par zone")
        print("[5] - Nombre de Places sur un parking donné pour un type de véhicule")
        print("[6] - Voir nb de paiement pour chaque type")
        print("[7] - Voir le nombre de clients abonnés et occasionnels")
        print("[8] - Signaler l'entrée d'un véhicule")
        print("[9] - Signaler la sortie d'un véhicule")
        print("[10] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            loop='false'
            zone.changer_zone_parking(cur,conn)
            loop='true'
        elif choix=='2' :
            loop='false'
            zone.changer_tarif_zone(cur,conn)
            loop='true'
        elif choix=='3' :
            loop='false'
            statistiques.Nombre_Abonnements_Zone(cur)
            loop='true'
        elif choix=='4' :
            loop='false'
            statistiques.Nombre_Parkings_Zone(cur)
            loop='true'
        elif choix=='5' :
            loop='false'
            statistiques.NbPlaces_Parking_Vehicule(cur)
            loop='true'
        elif choix=='6' :
            loop='false'
            statistiques.Nombre_Paiements(cur)
            loop='true'
        elif choix=='7' :
            loop='false'
            statistiques.Nombre_declients(cur)
            loop='true'
        elif choix=='8' :
            loop='false'
            entree_sortie.entree_parking(cur)
            loop='true'
        elif choix=='9' :
            loop='false'
            entree_sortie.sortie_parking(cur)
            loop='true'
        elif choix=='10' :   
            return

def menu_client(cur,conn,id,login):
    print("\n---Bienvenue dans votre espace client---")
    choix=0
    loop='true'
    while (loop=='true'):
        print("Que voulez-vous faire?")
        print("[1] - Reserver une place ")
        print("[2] - Consulter son solde de fidélité")
        print("[3] - ")
        print("[4] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            loop = 'false'
            reservation.reserver_place(cur,id,conn, login)
            loop='true'
        elif choix=='2' :
            loop='false'
            statistiques.Solde_Fidelite(cur, login)
            loop='true'
        elif choix=='3' :
            loop='false'
            #fonction
            loop='true'
        elif choix=='4' :
            return
