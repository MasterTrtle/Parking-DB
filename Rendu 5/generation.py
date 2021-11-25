from faker import Faker
import datetime
import psycopg2
import random


def nouvelle_transaction(cur,montant,type_caisse,client):
    sql = "insert into Paiement values (Default ; '%s', %'s', %'s') RETURNING id_transaction;"%(montant,type_caisse,client)
    cur.execute
    return cur.fetchone()[0]

def create_abo(cur, nom, prenom, naissance):
    sql = "INSERT into Client(id_client) values (DEFAULT) RETURNING id_client;"
    cur.execute(sql)
    id = cur.fetchone()[0]
    sql = "INSERT into Abonne values ('%s','0','%s','%s','%s');" % (id, nom, prenom, naissance)
    cur.execute(sql)

def insert_random_occasionel(cur,nombre):
    fake = Faker()
    for i in range(nombre):
        sql = "INSERT into Client(id_client) values (DEFAULT);"
        cur.execute(sql)

def insert_random_ticket(cur,id_transaction,id_client,type_vehicule):
    sql ="Insert into ticket values('%s',DEFAULT,'%s','%s','%s' );"%(id_transaction,type_vehicule,debut,fin,zone_parking,id_parking)
    return

def create_zone(cur):
    for nom in {"Centre-ville", "Industrielle", "Commerciale", "Historique","Quartier Affaire"}:
        prix_ticket=random.randint(2,10)
        prix_abo=random.randint(10,20)
        sql = "insert into zone values('%s', '%s', '%s')"%(nom, prix_ticket, prix_abo)
        cur.execute(sql)

def create_parking(cur,zone,nom,adresse):
    sql="insert into parking values(default,'%s','%s','%s');"%(zone,nom,adresse)
    cur.execute

def generate_parking(cur,nombre):
    fake = Faker()
    for i in range(nombre):
        zones=["Centre-ville", "Industrielle", "Commerciale", "Historique", "Quartier Affaire"]
        zone=zones[random.randint(0,4)]
        adresse=fake.address()
        nom=fake.name() #pas trouvé mieux
        create_parking(cur, zone, nom, adresse)

def insert_random_abo(cur, nombre):
    fake = Faker()
    for i in range(nombre):
        nom = fake.last_name()
        prenom = fake.first_name()
        debut = datetime.date(datetime.datetime.now().year - 80, 1, 1)
        fin = datetime.date(datetime.datetime.now().year - 18, 8, 15)  # etre majeur
        naissance = fake.date_between_dates(debut, fin)
        create_abo(cur, nom, prenom, naissance)

def generate_vehicule(cur,client):
    fake = Faker()
    for i in range(random.randint(0,10)):
        inmat=str(fake.license_plate())
        type_vehicule = ['deux roues', 'camion', 'vehicule simple'][random.randint(0,2)]
        sql = "insert into vehicule values('%s','%s',%s);"%(inmat,type_vehicule,client)
        cur.execute(sql)


def generate_vehicule_all_clients(cur):
    sql= "select * from Client"
    cur.execute(sql)
    raw=cur.fetchone()
    while raw:
        generate_vehicule(cur, raw[0])
        try:
            raw = cur.fetchone()
        except:
            break

def generate_all_account(cur):
    return


def remplir_bdd(cur):
    create_zone(cur)
    generate_parking(cur, 15)
    insert_random_abo(cur,20)
    insert_random_occasionel(cur,20)
    generate_vehicule_all_clients(cur)
