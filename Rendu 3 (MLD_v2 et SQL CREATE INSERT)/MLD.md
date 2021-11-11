Compte(#login: string, mail:string, mdp:string, employe => Employe, abonne=> Abonne) avec mdp NOT NULL and Mail, Employe, abonne UNIQUE  

Employé(#num_secu:int)

Client(##id_client:int)

Abonne(#id_client => Client, points_fidelite : int, nom:string, prenom:string, date_naiss:Date) avec nom, prenom, date_naiss NOT NULL    
Occasionel (#id_client => Client)

Vehicule(#immat:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, proprietaire=>Client) avec type_vehicule, proprietaire NOT NULL

Reservation(#id_reservation:int, debut:Date, fin:Date, vehicule=>Vehicule, client=>Client, place=>Place) avec debut, fin, vehicule, client, place NOT NULL   

Place(#parking=>Parking, #numero:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple},type_place:enum:{couvert,plein_air}) avec type_vehicule, type_place NOT NULL   

Parking(#id_parking:int, #zone=>Zone nom:string, adresse:string) avec (nom,adresse) KEY

Zone(#nom:string, tarif_ticket:int, tarif_abonnement:int) avec tarif_ticket, tarif_abonnement NOT NULL  

Paiement(#id_transaction:int, montant:int, type_caisse:enum:{Guichet, Automate, Internet}, client => Client) avec montant, type_caisse, client NOT NULL    

Abonnement(#id_transaction:int, id_carte:int, debut:Date, fin:Date, abonne=>Abonne, zone=>Zone) avec debut, fin, abonne, zone NOT NULL et id_carte KEY
Ticket(#id_transaction:int, id_ticket:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, debut:DateTime, fin:DateTime, parking=>Parking) avec type_vehicule, debut, parking NOT NULL et id_ticket KEY
  
