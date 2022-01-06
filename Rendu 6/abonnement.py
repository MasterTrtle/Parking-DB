import generation
import menu
import paiement
from datetime import datetime, date



def duree_mois(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    diff = int(abs((d1 - d2).days // 30.5))
    return diff


def check_occasionel_abonne(cur, client):  # renvoie True si le client est un occasionel
    sql = f"select id_client from occasionnel WHERE id_client in ({client});"
    cur.execute(sql)
    flag = cur.fetchone()
    flag = not (flag is None)
    return flag


def transition_occasionel_abonne(cur, client):
    sql = f"delete from occasionnel where id_client ={client}"
    cur.execute(sql)
    creer_compte_abonne(cur, client)  # voir dans le main, a faire une fonction


def get_points(cur, abonne):
    sql = f"select points_fidelite from abonne where id_client={abonne}"
    cur.execute(sql)
    return cur.fetchone()[0]


def update_points(cur, abonne, point):
    point += get_points(cur, abonne)
    sql = f"update abonne set points_fidelite = {point} where id_client ={abonne};"
    cur.execute(sql)


def create_abonnement(cur, debut, fin, client, zone,id_paiement):
    if check_occasionel_abonne(cur, client):
        transition_occasionel_abonne(cur, client)
    sql = f"insert into abonnement values({id_paiement}, Default, '{debut}', '{fin}',{client},'{zone}');"
    cur.execute(sql)


def acheter_abonnement(cur, client, zone, type_caisse,conn):
    if check_occasionel_abonne(cur, client):
        print("Vous n'avez pas de compte abonné, necessaire pour acheter un abonnement")
        print("Voulez vous vous creer un compte ?")
        flag = True
        while flag:
            print("[1] - Creer compte un abonnement pour cette zone")
            print("[2] - Ne rien faire")
            choix = int(input())
            if choix == 1:
                generation.convertion_occa_abo(cur, conn, client)
                debut = generation.input_date("entrez date debut")
                fin = generation.input_date('entrez date fin')
                create_abonnement(cur, debut, fin, client, zone, type_caisse)
                update_points(cur, client, generation.get_prix_zone(cur, 'tarif_abonnement', zone))
            elif choix == 2:
                flag = False
                menu.menu_client(cur, client)
    else:
        debut = datetime.today()
        fin = date(debut.year,debut.month+1,debut.day)
        montant=paiement.calculer_montant(cur,zone,False,0)
        print("Cela va vous couter : %s\n Voulez vous continuer ?\n[1] - OUI\n[2] - NON\n"%montant)
        choix=int(input())
        if choix==1:
            id_paiement=paiement.ajouter_paiement(montant,'internet',client,cur,conn)
            create_abonnement(cur, debut, fin, client, zone,id_paiement)
            update_points(cur, client, generation.get_prix_zone(cur, 'tarif_abonnement', zone))
        else:
            print("Paiement annulé, retour au menu\n")