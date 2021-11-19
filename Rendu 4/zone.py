import psycopg2
def changer_tarif_zone(cur):
    print("--- Modifier le tarif d'une zone---")
    sql="SELECT * FROM Zone ORDER BY nom;"
    cur.execute(sql)
    print('{0:15s} {1:10s} {2:10s}'.format('Zone','Ticket','Abonnement'))
    row=cur.fetchone()
    while row :
        print('{0:15s} {1:<10d} {2:<10d}'.format(row[0],row[1],row[2]))
        row=cur.fetchone()

    zone=input("Entrez le nom de la zone que vous souhaitez mettre à jour :")
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
            row=cur.execute(sql)
            if
            return
        elif choix=='2' :
            tarif_ticket=input("Entrez la nouvelle valeur du tarif ticket :")
            sql= "UPDATE Zone SET tarif_ticket='%s' WHERE nom='%s';"%(tarif_ticket,zone)
            row=cur.execute(sql)
            return
        elif choix=='3' :
            tarif_abo=input("Entrez la nouvelle valeur du tarif abonnement :")
            tarif_ticket=input("Entrez la nouvelle valeur du tarif ticket :")
            sql= "UPDATE Zone SET tarif_abonnement='%s',tarif_ticket='%s' WHERE nom='%s';"%(tarif_abo,tarif_ticket,zone)
            row=cur.execute(sql)
            return
        elif choix=='4' :
            return
    
def changer_zone_parking(cur):
    print("--- Modifier la zone d'un parking---")
    
def zone_setting(cur):
    choix=0
    while (choix!=1 and choix!=2 and choix!=3):
        print("--- Paramétrage de zones---")
        print("[1] - Changer un parking de zone")
        print("[2] - Changer le tarif d'une zone")
        print("[3] - Terminer")
        choix=input("Entrez votre choix : ")
        if choix=='1' :
            changer_zone_parking(cur)
        elif choix=='2' :
            changer_tarif_zone(cur)
        elif choix=='3' :
            return

if __name__ == "__main__":
    HOST = "tuxa.sme.utc"
    USER = "nf18a060"
    PASSWORD = "hLXrO3No"
    DATABASE = "dbnf18a060"

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

    cur=conn.cursor()
    zone_setting(cur)
    conn.commit()
    conn.close()
    