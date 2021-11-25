def afficher_zones(cur) :
    sql="SELECT * FROM Zone ORDER BY nom;"
    cur.execute(sql)
    print(f"\n{'Zone':15s} {'Ticket':10s} {'Abonnement':10s}")
    row=cur.fetchone()
    while row :
        print(f'{row[0]:15s} {row[1]:<10d} {row[2]:<10d}')
        row=cur.fetchone()

def afficher_parkings(cur) :
    sql="SELECT * FROM Parking ORDER BY zone;"
    cur.execute(sql)
    print(f"\n[{'ID':>3s}] {'Nom':10s} {'Zone':15s} {'Adresse':10s}")
    row=cur.fetchone()
    while row :
        print(f'[{row[0]:>3d}] {row[2]:10s} {row[1]:15s} {row[3]:10s}')
        row=cur.fetchone()        
    
def changer_tarif_zone(cur,conn):
    print("\n--- Modifier le tarif d'une zone---")
    
    #Afficher l'état actuel de la table zone
    afficher_zones(cur)
    
    #Séléctionner la zone à modifier
    zone=input("Entrez le nom de la zone que vous souhaitez mettre à jour : ")
    
    #Séléctionner les champs à modifier
    choix=0
    while (choix!=1 and choix!=2 and choix!=3 and choix!=4):
        print("Voulez vous modifier le tarif abonnement, ticket ou les deux?")
        print("[1] - Changer le tarif abonnement")
        print("[2] - Changer le tarif ticket")
        print("[3] - Changer les deux")
        print("[4] - Retour")
        
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            tarif_abo=input("Entrez la nouvelle valeur du tarif abonnement :")
            sql= "UPDATE Zone SET tarif_abonnement='%s' WHERE nom='%s';"%(tarif_abo,zone)
            cur.execute(sql)
            conn.commit()
            return
        
        elif choix=='2' :
            tarif_ticket=input("Entrez la nouvelle valeur du tarif ticket :")
            sql= "UPDATE Zone SET tarif_ticket='%s' WHERE nom='%s';"%(tarif_ticket,zone)
            cur.execute(sql)
            conn.commit()
            return
        
        elif choix=='3' :
            tarif_abo=input("Entrez la nouvelle valeur du tarif abonnement :")
            tarif_ticket=input("Entrez la nouvelle valeur du tarif ticket :")
            sql= "UPDATE Zone SET tarif_abonnement='%s',tarif_ticket='%s' WHERE nom='%s';"%(tarif_abo,tarif_ticket,zone)
            cur.execute(sql)
            conn.commit()
            return
        
        elif choix=='4' :
            return
    
def changer_zone_parking(cur,conn):
    print("\n--- Modifier la zone d'un parking---")
    
    #Afficher l'état actuel de la table parking
    afficher_parkings(cur)
    
    #Afficher l'état actuel de la table zone
    afficher_zones(cur)
    
    #Séléctionner le parking à modifier
    parking=input("Entrez l'ID du parking que vous souhaitez mettre à jour : ")
    #Séléctionner la nouvelle zone
    zone=input("Entrez le nom de la zone dans laquelle vous souhaitez transférer le parking : ")
    sql= "UPDATE Parking SET zone='%s' WHERE nom='%s';"%(zone,parking)
    cur.execute(sql)
    conn.commit()
    return
    
    