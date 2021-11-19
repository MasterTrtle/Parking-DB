import connect

if __name__ == '__main__':
    conn = connect.get_connection()
    cur = conn.cursor()
    # sql = "select * from vehicule;"
    # cur.execute(sql)
    # raw = cur.fetchone()
    # while raw:
    #    print(raw[0])
    #    raw = cur.fetchone()
    print("Bienvenue chez Auto-loc, votre location auto-instantanée")
    print("Que voulez-vous faire ?")
    print("   1. Se connecter")
    print("   2. Se créer un compte")
    choix1 = int(input())
    if choix1 == 1:
        # connexion
        loop = "true"
        while loop == "true":
            login = input("Quel est votre login ?")
            sql = "select login from compte"
            cur.execute(sql)
            raw = cur.fetchone()
            login_valide = 0
            while raw:
                if raw[0] == login:
                    login_valide = 1
                raw = cur.fetchone()
            if login_valide:
                password = input("Quel est votre mot de passe ?")
                sql = "select mdp,employe from compte where login='%s'" % login
                cur.execute(sql)
                raw = cur.fetchone()
                if raw[0] == password:
                    if raw[1]:
                        employe = 1
                        print("employe")
                    else:
                        employe = 0
                        print("client")
                else:
                    print("Mauvais mot de passe\nVeuillez vous reconnecter")
                    # retour menu
            else:
                print("Login inconnu\nVeuillez vous reconnecter")

    else:
        #creer un compte
        loop = "true"
        while loop == "true":
            login = input("Quel login voulez-vous ?")
            sql = "select login from compte"
            cur.execute(sql)
            raw = cur.fetchone()
            login_valide = 1
            while raw:
                if raw[0] == login:
                    login_valide = 0
                raw = cur.fetchone()
            if login_valide:
                password = input("Saisissez votre mot de passe")
                mail = input("Quelle est votre adresse mail ?")
                employe = int(input("Êtes-vous employé ?\n 0-Oui\n 1-Non"))
                if employe == 0:
                    #employe
                    secu = int(input("Quel est votre numero de sécurité sociale"))
                    sql = "select * from employe"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    employe = 0
                    while raw:
                        if int(raw[0]) == secu:
                            employe = 1
                        raw = cur.fetchone()
                    if employe == 1:
                        sql = "insert into Compte values('%s','%s','%s','%s',NULL)" % (login, mail, password, secu)
                        cur.execute(sql)
                        cur.commit()
                        print("Compte créé")
                        loop = "false"
                    else:
                        print("Le numero ne correspond pas à un employé\nMerci de rééssayer")
                else:
                    #client
                    num = int(input("Quel est votre identifiant client ?"))
                    sql = "select * from client"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    client = 0
                    while raw:
                        if int(raw[0]) == num:
                            client = 1
                        raw = cur.fetchone()
                    if client:
                        sql = "insert into Compte values('%s','%s','%s', NULL,'%s')" % (login, mail, password, num)
                        cur.execute(sql)
                        # cur.commit() -- C KC
                        print("Compte créé")
                        loop = "false"
                    else:
                        print("Le numero ne correspond pas à un client\nMerci de rééssayer")
            else:
                print("Login déjà utilisé\nMerci de ressaisir un nouveau login")
