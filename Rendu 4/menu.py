import zone
import reservation

def menu_employe(cur,conn,login):
    print("---Bienvenue dans l'espace employé---")
    choix=0
    loop='true'
    while (loop=='true'):
        print("Que voulez-vous faire?")
        print("[1] - Changer un parking de zone")
        print("[2] - Changer le tarif d'une zone")
        print("[3] - Terminer")
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
            return
        
def menu_client(cur,conn,login):
    print("\n---Bienvenue dans votre espace client---")
    choix=0
    loop='true'
    while (loop=='true'):
        print("Que voulez-vous faire?")
        print("[1] - Reserver une place ")
        print("[2] - ")
        print("[3] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            loop='false'
            reservation.reserver_place(cur,login)
            loop='true'
        elif choix=='2' :
            loop='false'
            #fonction
            loop='true'
        elif choix=='3' :
            return
    
