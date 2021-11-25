import datetime
import generation


def acheter_abonnement(cur,client,zone):
    sql = "select tarif_abonnement from zone where zone ='%s'"%zone
    cur.execute
    montant=cur.fetchone
    transaction =generation.nouvelle_transaction(cur,montant,"internet",client) #type caisse a changer

    #gérer l'entrée de la date
    choix=0
    while (choix!=3):
        print("Quand voulez vous faire commencer votre abonnement?")
        print("[1] - maintenant")
        print("[2] - autre")
        print("[3] - annuler")
        choix=input()
    if choix == 3:
        return
    else:
        duree = int(input("combien de mois ?"))
        if choix == 1:
            debut = datetime().now # attention format date
            fin = debut + duree # a refaire
        else:
            debut = input("entrez la date de début")
            fin= debut + duree # a refaire
        sql = "INSERT into Abonnement values ('%s', DEFAULT,'%s', '%s', '%s');" % (transaction, debut, fin, client)
        cur.execute(sql)