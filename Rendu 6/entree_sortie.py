from datetime import datetime
from affichage_input import input_id_parking,input_type_place,input_type_vehicule
from paiement import calculer_montant,ajouter_paiement,afficher_paiements
import reservation

#######################################
#------ Abonné dans ce parking? -----
#######################################
def is_abonne_zone(cur,immat,id_parking):
    sql="SELECT zone FROM parking WHERE id_parking='%s';"%(id_parking)
    cur.execute(sql)
    zone=cur.fetchone()[0]
    sql="SELECT v.proprietaire FROM Vehicule v INNER JOIN Abonnement a ON v.proprietaire=a.abonne WHERE v.immat='%s' AND a.zone='%s';"%(immat,zone)
    cur.execute(sql)
    if cur.rowcount>0:
        print("Le vehicule est celui d'un abonné!")
        return cur.fetchone()[0]
    else : 
        print("Le vehicule est celui d'un occasionnel!")
        return -1
    
#######################################
#-------- Place réservée ? --------
#######################################
def est_reservee(cur,id_parking,id_place):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #On cherche la place dans la table des Réservations
    #Si on la trouve avec une fin nulle alors elle est réservée
    #Si on la trouve avec une fin après now alors elle est en cours ou réservée dans le futur
    sql = "SELECT * FROM Reservation WHERE numero_place = '%s'\
            AND parking_place ='%s'\
            AND (fin IS NULL OR fin >= '%s');"%(id_place,id_parking,now)
    cur.execute(sql)
    #Si on a un résultat alors la place est réservée
    if cur.rowcount>0:
        print("On a un résultat dans les réservations : place déjà réservée")
        return True
    #Si on a aucun résultat alors elle n'est pas reservee
    #On doit quand même vérifier qu'elle n'est pas utilisée par un occasionnel
    #On effectue le même check dans la table Ticket
    else: 
        sql = "SELECT * FROM Ticket WHERE id_place ='%s' AND id_parking = '%s' AND (fin IS NULL OR fin>='%s')"%(id_place,id_parking,now)
        cur.execute(sql)
        #Si on a un résultat alors la place est réservée
        if cur.rowcount>0:
            print("On a un résultat dans les tickets : place déjà réservée")
            return True  
        else :   
            return False

#######################################
#-------- Trouver place libre --------
#######################################
def trouver_place_libre(cur,id_parking, type_vehicule, type_place):
    sql = f"SELECT numero FROM Place WHERE id_parking={id_parking} AND type_vehicule ='{type_vehicule}' AND type_place ='{type_place}';"
    cur.execute(sql)
    id_place = cur.fetchone()
    if id_place[0] is None:
        print("Entrée impossible, il n'y a pas de place disponible!\n")
        return False
    while id_place and est_reservee(cur, id_parking, id_place[0]):
        id_place = cur.fetchone()
    return id_place[0]
    

#######################################
#----------- Entrée Parking -----------
#######################################

def entree_parking(cur,conn):
    print("\n--- Signaler une entrée de véhicule---")
    
    type_place=input_type_place()
    immat=input("Entrez la plaque d'immatriculation du véhicule entrant : ")
    type_vehicule=input_type_vehicule()
    cur.execute("SELECT * FROM Vehicule where immat='%s'"%immat)
    if cur.fetchone() is None:
        cur.execute("INSERT into Client values (Default) RETURNING id_client")
        conn.commit()
        client=cur.fetchone()[0]
        cur.execute("INSERT into occasionnel values ('%s')"%client)
        conn.commit()
        cur.execute("INSERT into vehicule values('%s','%s','%s')"%(immat,type_vehicule,client))
        conn.commit()
    else:
        cur.execute("SELECT proprietaire from vehicule where immat='%s'"%immat)
        client=cur.fetchone()[0]
    id_parking=input_id_parking(cur)
    id_client=is_abonne_zone(cur,immat,id_parking)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    id_place=trouver_place_libre(cur, id_parking, type_vehicule, type_place)
    cur.execute("SELECT zone FROM Parking WHERE id_parking='%s';"%(id_parking))
    zone=cur.fetchone()[0]
    if id_place==False:
        return
    else :
        if(not reservation.check_abonnement_valide(cur,client,zone)):
            #Le client est un occasionnel, on lui génère un ticket 
            sql= "insert into Ticket values (NULL,DEFAULT,'%s','%s','%s','%s',NULL);"%(id_parking,id_place,immat,now)
            cur.execute(sql)
            conn.commit()
            print("Ticket créé! Le véhicule peut entrer!")
        else:
            #Si le client est un abonné dans cette zone alors on lui créé une réservation avec fin nulle
            print(id_client)
            sql= "insert into Reservation values (DEFAULT,'%s',NULL,'%s','%s','%s','%s');"%(now,immat,id_client,id_parking,id_place)
            cur.execute(sql)
            conn.commit()
            print("Réservation créée! Le véhicule peut entrer!")
            
        

    
    return

#######################################
#----------- Sortie Parking -----------
#######################################

def sortie_parking(cur,conn):
    print("\n--- Signaler une sortie de véhicule---")
    
    immat=input("Entrez la plaque d'immatriculation du véhicule sortant : ")
    #On va essayer de trouver une réservation ou un ticket en cours pour le véhicule
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sql = "SELECT * FROM Reservation WHERE vehicule = '%s' AND fin IS NULL;"%(immat)
    cur.execute(sql)
    #Si on a un résultat alors le vehicule a une réservée
    if cur.rowcount>0:
        print("On a un résultat dans les réservations!")
        sql= "UPDATE Reservation SET fin='%s' WHERE vehicule='%s' AND fin IS NULL;"%(now,immat)
        cur.execute(sql)
        conn.commit()
        if cur.rowcount>0:
            print("Réservation mise à jour, le véhicule peut sortir!")
            return
    #Si on a aucun résultat alors il n'a pas de reservation
    #On effectue le même check dans la table Ticket
    else: 
        sql = "SELECT * FROM Ticket WHERE immat ='%s' AND fin IS NULL"%(immat)
        cur.execute(sql)
        #Si on a un résultat alors le vehicule est un occasionel
        if cur.rowcount>0:
            row=cur.fetchone()
            id_ticket=row[1]
            id_parking=row[2]
            print("On a un résultat dans les tickets : le vehicule sort")
            sql="SELECT zone FROM Parking WHERE id_parking='%s';"%(id_parking)
            cur.execute(sql)
            zone=cur.fetchone()[0]
            cur.execute("UPDATE Ticket SET fin='%s' WHERE immat='%s' AND fin IS NULL;" % (now, immat))
            conn.commit()
            montant = calculer_montant(cur,zone,True,id_ticket)
            print("Prix à payer :")
            print(montant)
            print("Voulez vous continuer ?\n[1] - OUI\n[2] - NON\n")
            choix = int(input())
            if choix == 1:
                cur.execute("Select proprietaire from vehicule where immat='%s'"%immat)
                client = cur.fetchone()[0]
                id_paiement = ajouter_paiement(montant, 'guichet', client, cur, conn)
                sql = "UPDATE Ticket SET id_transaction='%s' WHERE immat='%s' AND fin IS NULL;" % (id_paiement,immat)
                cur.execute(sql)
                conn.commit()
                print("Paiement effectué, retour au menu\n")
            else:
                print("Paiement annulé, retour au menu\n")
            return
        else:
            print("/!\ La requête a échoué. Veuillez vérifier que la plaque est correcte.")
            return
    return

