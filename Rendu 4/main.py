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
        retour = "false"
        while retour == "false":
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
        login = input("Quel login voulez-vous ?")
        # check si le login n'est pas déjà pris
        password = input("Saisissez votre mot de passe")
        mail = input("Quelle est votre adresse mail ?")
        employe = bool(input("Êtes-vous employé ?\n 0-Oui\n 1-Non"))
        if employe:
            secu = int(input("Quel est votre numero de sécurité sociale"))
            print("employe")
            # check si l'employé existe sinon refus
        else:
            client = int(input("Quel est votre identifiant client ?"))
            print("client")
            # check si c'est un abonné
