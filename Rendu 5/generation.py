from faker import Faker
import datetime
import psycopg2
import random
from random_username.generate import generate_username

def rand_parking(cur):
    sql = "select id_parking from parking;"
    cur.execute(sql)
    p = cur.fetchall()
    return random.choice(p)[0]

def nouveau_paiement(cur,montant,type_caisse,client):
    sql = "insert into Paiement values (Default, '%s', '%s', '%s') RETURNING id_transaction;"%(montant,type_caisse,client)
    cur.execute(sql)
    return cur.fetchone()[0]

def get_zone(cur,parking):
    sql = "Select zone from parking where id_parking = '%s';"%parking
    cur.execute(sql)
    return cur.fetchone()[0]

def get_prix(cur,cible, parking): # cible = tarif_ticket || tarif_abonnement
    sql = "select %s from zone where nom = '%s';"%(cible,get_zone(cur,parking))
    cur.execute(sql)
    return cur.fetchone()[0]

def select_place(cur,id_parking, type_place,type_vehicule):
    sql = f"select numero from place where id_parking = {id_parking} AND type_place = '{type_place}' AND type_vehicule = '{type_vehicule}'"
    cur.execute(sql)
    place = cur.fetchone()
    if place == None:
        return place
    else:
        #faut checker reservation
        return place[0]


def create_ticket(cur,id_client,type_vehicule,type_place,id_parking,type_caisse):
    id_place = select_place(cur,id_parking, type_place,type_vehicule)
    if id_place == None:
        print(f"impossible de reserver une place {type_place} pour un {type_vehicule} dans le parking {id_parking}")
    else:
        prix = get_prix(cur, 'tarif_ticket', id_parking)
        id_paiement = nouveau_paiement(cur, prix, type_caisse, id_client)
        todays_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        sql =f"Insert into ticket(id_transaction,id_ticket,id_place,type_vehicule,type_place,debut,id_parking) values({id_paiement},DEFAULT,{id_place},'{type_vehicule}','{type_place}','{todays_date}',{id_parking});"
        cur.execute(sql)

def generate_ticket(cur):
    type_vehicule = ['deux roues', 'camion', 'vehicule simple']
    type_caisse = ['guichet', 'automate', 'internet']
    type_place = ['couverte', 'plein air couverte', 'plein air']
    sql = "select id_client from Occasionnel"
    cur.execute(sql)
    liste_occasionel = cur.fetchall()
    for client in liste_occasionel:
        id_client = client[0]
        id_parking = rand_parking(cur)
        create_ticket(cur,id_client,type_vehicule[random.randint(0,2)],type_place[random.randint(0,2)],id_parking,type_caisse[random.randint(0,2)])


def create_abo(cur, nom, prenom, naissance):
    sql = "INSERT into Client(id_client) values (DEFAULT) RETURNING id_client;"
    cur.execute(sql)
    id = cur.fetchone()[0]
    sql = "INSERT into Abonne values ('%s','0','%s','%s','%s');" % (id, nom, prenom, naissance)
    cur.execute(sql)
    create_account_random(cur,'client',id)


def insert_random_occasionel(cur,nombre):
    for i in range(nombre):
        sql = "INSERT into Client(id_client) values (DEFAULT) RETURNING id_client;"
        cur.execute(sql)
        id = cur.fetchone()[0]
        sql = "Insert into Occasionnel values ('%s')"%id
        cur.execute(sql)

def create_account_random(cur,cible, id):
    fake = Faker()
    login =generate_username()[0]
    mail = fake.email()
    #sql = ""#verifier unicité mail
    mdp = fake.password(10)
    if cible =="employe":
        sql = "INSERT INTO compte(login,mail,mdp,employe) values ('%s','%s','%s','%s');"%(login,mail,mdp,id)
    else:
        sql = "INSERT INTO compte(login,mail,mdp,abonne) values ('%s','%s','%s','%s');" % (login, mail, mdp, id)
    cur.execute(sql)

def create_zone(cur):
    for nom in {"Centre-ville", "Industrielle", "Commerciale", "Historique","Quartier Affaire"}:
        prix_ticket=random.randint(2,10)
        prix_abo=random.randint(10,20)
        sql = "insert into zone values('%s', '%s', '%s')"%(nom, prix_ticket, prix_abo)
        cur.execute(sql)

def create_parking(cur,zone,nom,adresse):

    sql="insert into parking values(default,'%s','%s','%s');"%(zone,nom,adresse)
    cur.execute(sql)

def generate_parking(cur,nombre):
    fake = Faker()
    for i in range(nombre):
        zones=["Centre-ville", "Industrielle", "Commerciale", "Historique", "Quartier Affaire"]
        zone=zones[random.randint(0,4)]
        adresse=fake.address()
        nom=fake.name() #pas trouvé mieux
        create_parking(cur, zone, nom, adresse)

def creer_place(cur,parking,num,type_place,type_vehicule):
    sql = "INSERT into PLACE values ('%s','%s','%s','%s')"%(parking,num,type_vehicule,type_place)
    cur.execute(sql)

def generate_places(cur,nombre):
    type_place =['couverte', 'plein air couverte', 'plein air']
    type_vehicule=['deux roues', 'camion', 'vehicule simple']
    sql = "SELECT id_parking FROM PARKING;"
    cur.execute(sql)
    liste_parking=cur.fetchall()
    for i in liste_parking:
        for y in range(random.randrange(nombre)):
            creer_place(cur,i[0],y,type_place[random.randint(0,2)],type_vehicule[random.randint(0,2)])

def insert_random_abo(cur, nombre):
    fake = Faker()
    for i in range(nombre):
        nom = fake.last_name()
        prenom = fake.first_name()
        debut = datetime.date(datetime.datetime.now().year - 80, 1, 1)
        fin = datetime.date(datetime.datetime.now().year - 18, 8, 15)  # etre majeur
        naissance = fake.date_between_dates(debut, fin)
        create_abo(cur, nom, prenom, naissance)

def create_employe(cur,numSecu):
    sql = "INSERT into employe values (DEFAULT, '%s') RETURNING id_employe;"%numSecu
    cur.execute(sql)
    id = cur.fetchone()[0]
    create_account_random(cur,'employe',id)

def insert_random_employe(cur,nombre):
    fake = Faker()
    for i in range(nombre):
        numSecu=random.getrandbits(20)
        create_employe(cur,numSecu)

def generate_vehicule(cur,client):
    fake = Faker()
    for i in range(random.randint(0,5)):
        inmat=str(fake.license_plate())
        type_vehicule = ['deux roues', 'camion', 'vehicule simple'][random.randint(0,2)]
        sql = "insert into vehicule values('%s','%s',%s);"%(inmat,type_vehicule,client)
        cur.execute(sql)


def generate_vehicule_all_clients(cur):
    sql= "select id_client from Client;"
    cur.execute(sql)
    raw=cur.fetchall()
    for client in raw:
        generate_vehicule(cur, client[0])

def remplir_bdd(cur):
    create_zone(cur)
    generate_parking(cur, 10)
    generate_places(cur,20)
    insert_random_abo(cur,10)
    insert_random_occasionel(cur,20)
    insert_random_employe(cur,5)
    generate_vehicule_all_clients(cur)
    generate_ticket(cur)
