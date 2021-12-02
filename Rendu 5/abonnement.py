import generation
from menu import menu_client


def check_occasionel_abonne(cur, client):  # renvoie True si le client est un occasionel
    sql = f"select id_client from occasionnel WHERE id_client in ({client});"
    cur.execute(sql)
    flag = cur.fetchone()
    flag = not (flag is None)
    return flag


def transition_occasionel_abonne(cur, client):
    return


def get_points(cur, abonne):
    sql = f"select points_fidelite from abonne where id_client={abonne}"
    cur.execute(sql)
    return cur.fetchone()[0]


def update_points(cur, abonne, point):
    point += get_points(cur, abonne)
    sql = f"update abonne set points_fidelite = {point} where id_client ={abonne};"
    cur.execute(sql)


def create_abonnement(cur, debut, fin, client, zone, type_caisse):
    duree = duree_mois(debut, fin)
    prix = generation.get_prix_zone(cur, 'tarif_abonnement', zone) * duree
    id_paiement = generation.nouveau_paiement(cur, prix, type_caisse, client)
    if check_occasionel_abonne(cur, client):
        creer_compte_abonne(cur, client)  # voir dans le main, a faire une fonction
    sql = f"insert into abonnement values({id_paiement}, Default, '{debut}', '{fin}',{client},'{zone}');"
    cur.execute(sql)


def acheter_abonnement(cur, client, zone, type_caisse):
    if check_occasionel_abonne(cur, client):
        print("Vous n'avez pas de compte abonner, necessaire pour acheter un abonnement")
        print("Voulez vous vous creer un compte ?")
        flag = True
        while flag:
            print("[1] - Creer compte un abonnement pour cette zone")
            print("[2] - Ne rien faire")
            choix = int(input())
            if choix == 1:
                # cf code du main pour creation compte
                debut = input("entrez date debut")
                fin = input('entrez date fin')
                create_abonnement(cur, debut, fin, client, zone, type_caisse)
                update_points(cur, client, generation.get_prix_zone(cur, 'tarif_abonnement', zone))
            elif choix == 2:
                flag = False
                menu_client(cur, client)
    else:
        debut = generation.input_date("entrez date debut")
        fin = generation.input_date('entrez date fin')
        create_abonnement(cur, debut, fin, client, zone, type_caisse)
        update_points(cur, client, generation.get_prix_zone(cur, 'tarif_abonnement', zone))
