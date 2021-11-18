Compte(#login: string, mail:string, mdp:string, employe => Employe, abonne=> Abonne) avec mdp, employe, abonne NOT NULL and Mail, Employe, abonne UNIQUE  

Employé(#num_secu:int)

Client(#id_client:int) //classe mère de Abonne et Occasionel
//héritage par référence
Abonne(#id_client => Client, points_fidelite : int, nom:string, prenom:string, date_naiss:Date) avec nom, prenom, date_naiss NOT NULL avec date_naiss < currentdate    
Occasionel (#id_client => Client)

Vehicule(#immat:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, proprietaire=>Client) avec type_vehicule, proprietaire NOT NULL

Reservation(#id_reservation:int, debut:Date, fin:Date, vehicule=>Vehicule, client=>Client, placenum=>Place.numero, placepark=>Place.parking) avec debut, fin, vehicule, client, placenum, placepark NOT NULL and debut<fin  

Place(#parking=>Parking, #numero:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple},type_place:enum:{couvert,plein_air}) avec type_vehicule, type_place NOT NULL   

Parking(#id_parking:int, #zone=>Zone nom:string, adresse:string) avec (nom,adresse) KEY

Zone(#nom:string, tarif_ticket:int, tarif_abonnement:int) avec tarif_ticket, tarif_abonnement NOT NULL  

Paiement(#id_transaction:int, montant:int, type_caisse:enum:{Guichet, Automate, Internet}, client => Client) avec montant, type_caisse, client NOT NULL    
//Paiement classe mère de Abonnement et Tickets, héritage par référence
Abonnement(#id_transaction:int, id_carte:int, debut:Date, fin:Date, abonne=>Abonne, zone=>Zone) avec debut, fin, abonne, zone NOT NULL et id_carte KEY avec debut < fin 
Ticket(#id_transaction:int, id_ticket:int, type_vehicule:enum:{deux_roues,camion,vehicule_simple}, debut:DateTime, fin:DateTime, parking.zone=>Parking.zone, parking.id=>Parking.id_parking) avec type_vehicule, debut, parking.zone, parking.id NOT NULL et id_ticket KEY avec debut < fin 
  
Contraintes de cardinalité minimale :
(les not null ont déjà été mis plus haut)

- Projection (Client, id_client) =  Projection (Paiement, client)
- Projection (Abonne, id_client) =  Projection (Abonnement, abonne)
- Projection (Reservation, vehicule) =  Projection (Vehicule, immat)
- Projection (Client, id_client) =  Projection (Vehicule, proprietaire)
- Projection (Abonnement, zone) =  Projection (Zone, nom)
- Projection (Reservation, place.num) =  Projection (Place, numero) et Projection (Reservation, place.park) =  Projection (Place, parking)
- Projection (Ticket, parking.id) = Projection (Parking, id_parking) et Projection (Ticket, parking.zone) = Projection (Parking, zone)

Contrainte des héritages par références :

- INTERSECTION (PROJECTION(Abonnement,id_transaction), PROJECTION(Ticket,id_transaction)) = {}
- INTERSECTION (PROJECTION(Abonne,id_client), PROJECTION(Occasionnel,id_client)) = {}

