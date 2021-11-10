Compte(#mail:string mdp:string, pt_fidelite:int) avec mdp NOT NULL  

Abonne(#id_user:int, nom:string, prenom:string,date_naiss:Date, compte=>Compte) avec nom, prenom, date_naiss, compte NOT NULL    

Vehicule(#immat:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, modele:string, proprietaire=>Abonne) avec type_vehicule NOT NULL

Reservation(#id_reservation:int, debut:Date, fin:Date, vehicule=>Vehicule, abonne=>Abonne, place=>Place) avec debut, fin, vehicule, abonne, place NOT NULL   

Place(#numero:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple},type_place:enum:{couvert,plein_air}, parking=>Parking) avec parking, type_vehicule, type_place NOT NULL   

Parking(#id_parking:int, nom:string, adresse:string, zone=>Zone) avec zone NOT NULL, nom et adresse clés

Zone(#nom:string, tarif_ticket:int, tarif_abonnement:int) avec tarif_ticket, tarif_abonnement NOT NULL  

Paiement(#id_transction:int, montant:int, abonnement=>Abonnement, ticket=>Ticket) avec montant NOT NULL, (abonnement xor ticket)     

Abonnement(#id_carte:int, debut:Date, fin:Date, abonne=>Abonne, zone=>Zone) avec debut, fin, abonne, zone NOT NULL

Employé(#num_secu:int, #compte=>Compte)    

Caisse(#id_caisse:int, #paiement=>Paiement, #ticket=>Ticket type_caisse:enum:{guichet, automate}) avec type_caisse NOT NULL 

Ticket(#id_ticket:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, debut:DateTime, fin:DateTime, parking=>Parking) avec type_vehicule, debut, parking NOT NULL

Contrainte pour l'héritage par référence  
