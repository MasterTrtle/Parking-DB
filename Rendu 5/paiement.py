from datetime import datetime,timedelta

def calculer_montant(cur,zone,ticket,id): #zone + booleen
    if ticket:
        cur.execute("SELECT tarif_ticket FROM Zone where nom='%s'"%zone)
        tarif=cur.fetchone()
        cur.execute("SELECT debut,fin FROM Ticket where id_ticket='%s'"%id)
        date=cur.fetchone()
        debut=date[0]
        fin=date[1]
        FMT='%Y-%M-%D %H:%M:%S'
        delta=datetime.strptime(debut,FMT) - datetime.strptime(fin,FMT)
        return int(delta/3600000000)*int(tarif)
    else:
        cur.execute("SELECT tarif_abonnement FROM Zone where nom='%s'"%zone)
        tarif=cur.fetchone()
        return tarif

def ajouter_paiement(montant,type_caisse,client,cur,conn):
    cur.execute("INSERT INTO paiement values (Default,'%s','%s','%s')"%(montant,type_caisse,client))
    conn.commit()
    cur.execute("SELECT id_transaction FROM paiement where client='%s'"%client)
    return cur.fetchall()[-1]

def afficher_paiements(login,cur):
    cur.execute("SELECT abonne from compte where login='%s'"%login)
    client = cur.fetchone()
    cur.execute("SELECT id_transaction,montant,type_caisse from paiement where client='%s'"%client)
    raw = cur.fetchone()
    if raw is None:print("Vous n'avez pas encore fait de paiement");return
    print("ID | MONTANT | TYPE DE CAISSE")
    while raw:
        print(str(raw[0])+" | "+str(raw[1])+" | "+raw[2])
        raw = cur.fetchone()