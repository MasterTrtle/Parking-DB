#######################################
#---------- Input et choix  ----------
#######################################
def input_type_place():
    type_place = ['couverte', 'plein air couverte', 'plein air']
    choix=-1
    while (not (choix==0 or choix==1 or choix==2)):
        print("Choississez le type de place")
        print("[0] - Place couverte")
        print("[1] - Place en plein air couverte")
        print("[2] - Place en plein air")
        print("Votre choix : ")
        choix = int(input())
    return type_place[choix]

def input_type_vehicule():
    type_vehicule = ['deux roues', 'camion', 'vehicule simple']
    choix=-1
    while (not (choix==0 or choix==1 or choix==2)):
        print("Choississez le type de vehicule :")
        print("[0] - Deux roues")
        print("[1] - Camion")
        print("[2] - Véhicule simple")
        print("Votre choix : ")
        choix = int(input())
    return type_vehicule[choix]

def input_id_parking(cur):
    choix=-1   
    nb_parking=afficher_parkings(cur)
    print(nb_parking)
    while (choix<0 or choix>nb_parking):
        print("Votre choix : ")
        choix = int(input())
    return choix

def input_id_carte():
    loop=True
    print("Si l'utilisateur a une carte d'abonné veuillez entrer l'ID de la carte : (-1 sinon)")
    while loop==True :
        try :
            print("Votre choix : ")
            id_carte=int(input("Entrez la plaque d'immatriculation du véhicule sortant : "))
            loop=False
        except ValueError :
            print("Valeur entrée incorrecte, l'ID est un nombre")
            continue

    return id_carte
        

#######################################
#------------ Affichages  ------------
#######################################

#Affiche un tableau avec toutes les zones
def afficher_zones(cur) :
    sql="SELECT * FROM Zone ORDER BY nom;"
    cur.execute(sql)
    print(f"\n{'Zone':15s} {'Ticket':10s} {'Abonnement':10s}")
    row=cur.fetchone()
    while row :
        print(f'{row[0]:15s} {row[1]:<10d} {row[2]:<10d}')
        row=cur.fetchone()

#Affiche un tableau avec tous les parkings
def afficher_parkings(cur) :
    sql="SELECT * FROM Parking ORDER BY zone;"
    cur.execute(sql)
    print(f"\n[{'ID':>3s}] {'Nom':10s} {'Zone':15s} {'Adresse':10s}")
    row=cur.fetchone()
    while row :
        print(f'[{row[0]:>3d}] {row[2]:10s} {row[1]:15s} {row[3]:10s}')
        row=cur.fetchone()     
    return cur.rowcount