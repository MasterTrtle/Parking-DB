from faker import Faker
import datetime
import psycopg2
import random
from random_username.generate import generate_username
import abonnement


def input_date(message):
    print(message)
    a = int(input("annee ?"))
    m = int(input("mois ?"))
    j = int(input("jour ?"))
    x = datetime.datetime(a, m, j)
    x = x.strftime("%Y-%m-%d")
    return x


def rand_type_vehicule():
    type_vehicule = ['deux roues', 'camion', 'vehicule simple']
    return type_vehicule[random.randint(0, 2)]


def rand_type_place():
    type_place = ['couverte', 'plein air couverte', 'plein air']
    return type_place[random.randint(0, 2)]


def rand_type_caisse():
    type_caisse = ['guichet', 'automate', 'internet']
    return type_caisse[random.randint(0, 2)]


def rand_zone():
    zones = ["Centre-ville", "Industrielle", "Commerciale", "Historique", "Quartier Affaire"]
    return zones[random.randint(0, 4)]


def rand_parking(cur):
    sql = "select id_parking from parking;"
    cur.execute(sql)
    p = cur.fetchall()
    return random.choice(p)[0]


def nouveau_paiement(cur, montant, type_caisse, client):
    sql = f"insert into Paiement values (Default, '{montant}', '{type_caisse}', '{client}') RETURNING id_transaction;"
    cur.execute(sql)
    return cur.fetchone()[0]


def get_zone(cur, parking):
    sql = f"Select zone from parking where id_parking = '{parking}';"
    cur.execute(sql)
    return cur.fetchone()[0]


def get_prix_parking(cur, cible, parking):  # cible = tarif_ticket || tarif_abonnement
    sql = f"select {cible} from zone where nom = '{get_zone(cur, parking)}';"
    cur.execute(sql)
    return cur.fetchone()[0]


def get_prix_zone(cur, cible, zone):  # # cible = tarif_ticket || tarif_abonnement
    sql = f"select {cible} from zone where nom = '{zone}';"
    cur.execute(sql)
    return cur.fetchone()[0]


def select_place(cur, id_parking, type_place, type_vehicule):
    sql = f"select numero from place where id_parking = {id_parking} AND type_place = '{type_place}' AND type_vehicule = '{type_vehicule}'"
    cur.execute(sql)
    place = cur.fetchone()
    if place is None:
        return place
    else:
        # faut checker reservation
        return place[0]


def create_ticket(cur, id_client, type_vehicule, type_place, id_parking, type_caisse):
    id_place = select_place(cur, id_parking, type_place, type_vehicule)
    if id_place is None:
        print(f"impossible de reserver une place {type_place} pour un {type_vehicule} dans le parking {id_parking}")
    else:
        prix = get_prix_parking(cur, 'tarif_ticket', id_parking)
        id_paiement = nouveau_paiement(cur, prix, type_caisse, id_client)
        todays_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        sql = f"Insert into ticket(id_transaction,id_ticket,id_place,type_vehicule,type_place,debut,id_parking) values({id_paiement},DEFAULT,{id_place},'{type_vehicule}','{type_place}','{todays_date}',{id_parking});"
        cur.execute(sql)


def generate_ticket(cur):
    sql = "select id_client from Occasionnel"
    cur.execute(sql)
    liste_occasionel = cur.fetchall()
    for client in liste_occasionel:
        id_client = client[0]
        id_parking = rand_parking(cur)
        create_ticket(cur, id_client, rand_type_vehicule(), rand_type_place(), id_parking, rand_type_caisse())


def create_abonne(cur, nom, prenom, naissance):
    sql = "INSERT into Client(id_client) values (DEFAULT) RETURNING id_client;"
    cur.execute(sql)
    id = cur.fetchone()[0]
    sql = f"INSERT into Abonne values ('{id}','0','{nom}','{prenom}','{naissance}');"
    cur.execute(sql)
    create_account_random(cur, 'client', id)


def insert_random_occasionel(cur, nombre):
    for _ in range(nombre):
        sql = "INSERT into Client(id_client) values (DEFAULT) RETURNING id_client;"
        cur.execute(sql)
        id = cur.fetchone()[0]
        sql = f"Insert into Occasionnel values ('{id}')"
        cur.execute(sql)


def create_compte_client(cur, login, mail, mdp, id_abonne):
    sql = f"INSERT INTO compte(login,mail,mdp,abonne) values ('{login}','{mail}','{mdp}','{id_abonne}');"
    cur.execute(sql)


def create_compte_employe(cur, login, mail, mdp, id_employe):
    sql = f"INSERT INTO compte(login,mail,mdp,employe) values ('{login}','{mail}','{mdp}','{id_employe}');"
    cur.execute(sql)


def create_account_random(cur, cible, id):
    fake = Faker()
    login = generate_username()[0]
    mail = fake.email()
    # sql = ""#verifier unicité mail
    mdp = fake.password(10)
    if cible == "employe":
        create_compte_employe(cur, login, mail, mdp, id)
    else:
        create_compte_client(cur, login, mail, mdp, id)


def create_zone(cur):
    for nom in {"Centre-ville", "Industrielle", "Commerciale", "Historique", "Quartier Affaire"}:
        prix_ticket = random.randint(2, 10)
        prix_abo = random.randint(10, 20)
        sql = f"insert into zone values('{nom}', '{prix_ticket}', '{prix_abo}')"
        cur.execute(sql)


def create_parking(cur, zone, nom, adresse):
    sql = f"insert into parking values(default,'{zone}','{nom}','{adresse}');"
    cur.execute(sql)


def generate_parking(cur, nombre):
    fake = Faker()
    for _ in range(nombre):
        adresse = fake.address()
        nom = fake.name()  # pas trouvé mieux
        create_parking(cur, rand_zone(), nom, adresse)


def creer_place(cur, parking, num, type_place, type_vehicule):
    sql = f"INSERT into PLACE values ('{parking}','{num}','{type_vehicule}','{type_place}')"
    cur.execute(sql)


def generate_places(cur, nombre):
    sql = "SELECT id_parking FROM PARKING;"
    cur.execute(sql)
    liste_parking = cur.fetchall()
    for i in liste_parking:
        for y in range(random.randrange(nombre)):
            creer_place(cur, i[0], y, rand_type_place(), rand_type_vehicule())


def insert_random_abo(cur, nombre):
    fake = Faker()
    for _ in range(nombre):
        nom = fake.last_name()
        prenom = fake.first_name()
        debut = datetime.date(datetime.datetime.now().year - 80, 1, 1)
        fin = datetime.date(datetime.datetime.now().year - 18, 8, 15)  # etre majeur
        naissance = fake.date_between_dates(debut, fin)
        create_abonne(cur, nom, prenom, naissance)


def create_employe(cur, numSecu):
    sql = f"INSERT into employe values (DEFAULT, '{numSecu}') RETURNING id_employe;"
    cur.execute(sql)
    id = cur.fetchone()[0]
    create_account_random(cur, 'employe', id)


def convertion_occa_abo(cur,conn, id):
    # creer un compte
    loop = True
    while loop:
        login = input("Quel login voulez-vous ? ")
        sql = "select login from compte"
        cur.execute(sql)
        raw = cur.fetchone()
        login_valide = 1
        while raw:
            if raw[0] == login:
                login_valide = 0
            raw = cur.fetchone()
        if login_valide:
            password = input("Saisissez votre mot de passe : ")
            mail = input("Quelle est votre adresse mail ? ")
            nom = input('Quel est votre nom')
            prenom = input('Quel est votre prenom')
            naissance = input_date('Quel est votre date de naissance')

            sql= f"delete from occasionnel where id_client = {id}"
            cur.execute(sql)
            sql = f"INSERT into Abonne values ('{id}','0','{nom}','{prenom}','{naissance}');"
            cur.execute(sql)
            create_compte_client(cur, login, mail, password, id)
            conn.commit()
            print("Compte créé")
            loop = False
        else:
            print("login deja utilisé, choississez en un autre")




def insert_random_employe(cur, nombre):
    for _ in range(nombre):
        numSecu = random.getrandbits(20)
        create_employe(cur, numSecu)


def generate_vehicule(cur, client):
    fake = Faker()
    for _ in range(random.randint(0, 5)):
        inmat = str(fake.license_plate())
        sql = f"insert into vehicule values('{inmat}','{rand_type_vehicule()}',{client});"
        cur.execute(sql)


def generate_vehicule_all_clients(cur):
    sql = "select id_client from Client;"
    cur.execute(sql)
    raw = cur.fetchall()
    for client in raw:
        generate_vehicule(cur, client[0])


def remplir_bdd(cur, conn):
    create_zone(cur)
    generate_parking(cur, 5)
    generate_places(cur, 100)
    insert_random_abo(cur, 5)
    insert_random_occasionel(cur, 5)
    insert_random_employe(cur, 1)
    generate_vehicule_all_clients(cur)
    # generate_ticket(cur)

    abonnement.create_abonnement(cur, '2020-01-01', '2020-03-01', 1, 'Industrielle', 'internet')
    abonnement.create_abonnement(cur, '2020-01-01', '2020-03-01', 1, 'Commerciale', 'internet')
    abonnement.create_abonnement(cur, '2020-01-01', '2020-03-01', 1, 'Quartier Affaire', 'internet')
    abonnement.create_abonnement(cur, '2020-01-01', '2020-03-01', 1, 'Centre-ville', 'internet')
    abonnement.create_abonnement(cur, '2019-01-01', '2019-03-01', 1, 'Industrielle', 'internet')
    abonnement.create_abonnement(cur, '2020-01-01', '2020-03-01', 1, 'Historique', 'internet')
    abonnement.create_abonnement(cur, '2021-01-01', '2021-03-01', 1, 'Historique', 'internet')

    conn.commit()
