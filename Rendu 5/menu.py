import zone
import reservation

def menu_employe(cur,conn,login):
    print("---Bienvenue dans l'espace employé---")
    choix=0
    loop = True
    while loop:
        print("Que voulez-vous faire?")
        print("[1] - Changer un parking de zone")
        print("[2] - Changer le tarif d'une zone")
        print("[3] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            zone.changer_zone_parking(cur,conn)
        elif choix=='2' :
            zone.changer_tarif_zone(cur,conn)
        elif choix=='3' :
            loop=False
            return
        
def menu_client(cur,conn,login):
    print("\n---Bienvenue dans votre espace client---")
    choix=0
    loop = True
    while loop:
        print("Que voulez-vous faire?")
        print("[1] - Reserver une place")
        print("[2] - Consulter|Modifier votre liste de véhicules")
        print("[3] - Consulter|Modifier vos abonnement")
        print("[4] - Consulter|Modifier vos réservations")
        print("[5] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            reservation.reserver_place(cur,login)
        elif choix=='2':
            return
        elif choix=='4' :
            return
        elif choix == '5':
            loop = False
    
