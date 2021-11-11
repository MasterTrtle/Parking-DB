NDC:


# Note de Clarification

## _UtilisateursBDD :_ 
-	Nouvel utilisateur pour se créer un abonnement (et donc un compte)
-	Abonné pour gérer ses abonnements et réserver une place
-	un employé pour consulter des stat et diverses informations 

## _Requêtes types :_
-	consulter les statistiques
-	consulter le nombre de place restantes sur un parking
-	réserver une place
-	changer un parking de zone
-	changer le tarif d’une zone
-	se créer un compte
-	requêtes associées aux users décrites précédemment 
-	consulter son solde de fidélité
-	afficher le nombre de places disponibles dans l’ensemble des parkings
-	…


## _Compte :_ (classe mère)_  

Se compose d'un login (unique not null), d’un mot de passe(not null), et d’une adresse mail (unique not null). 
Un compte correspond soit à un abonné, soit à un employé

## _Employé :_ 
Se compose d’un numéro de sécu social (unique not null)
- il correspond à un unique compte


## _Abonné :_ (classe fille)_  
Se compose d’un nom(not null), d’un prénom(not null), d'une date de naissance (not null), et d’un solde de fidélité qui permettra de lui calculer des avantages.
- il hérite de client par référence
- il possède un compte
- il souscrit à autant d'abonnements qu'il le souhaite, sachant qu'il s'agit d'un abonnement par zone 

## _Occasionnel :_ (classe fille)_  
Héritage complet par référence de la classe client
- si il souscrit à un abonnement il devient un abonné

## _Client :_
Se compose d’un id_client (unique & not null).
Classe mère de occasionnel et abonné
- il peut effectuer des paiements
- il peut effectuer des réservations
- il possède 0 ou plusieurs véhicules



## _Véhicule :_
Se compose d'une immatriculation (unique not null), d'un type (not null): deux roues, camion, véhicule simple.     
Il est nécessaire de connaître le type du véhicule pour lui attribuer une place adaptée dans le parking.
-	Il peut être associé à une réservation
-	Il appartient à un client
  

## _Réservation :_
Se compose d’un id (unique not null), d’une date de début (not null) et d’une date de fin (not null), et d’une fonction permettant de vérifier si la réservation est possible date de fin > Date de début.
Dans notre modélisation, un client peut réserver à l’avance afin d’être sûr qu’une place sera disponible pour lui. C’est gratuit pour celui qui a un abonnement et sinon, le jour de la réservation, l’occasionnel devra régler sur place. En fait cette classe est une assurance d’avoir une place disponible entre le début et la fin de la réservation.

-	Elle est associée au véhicule qui a réservé la place
-	Elle est faite par un client
-	Elle réserve une place en particulier

## _Paiements : (classe mère abstraite)_
Se compose d'un id de transaction (unique et non null), d'un montant (non null), d’un type de caisses (guichet, automate et internet)  et d'une fonction permettant de calculer le montant.
Classe mère de ticket et abonnement.
- Un paiement est effectué par un client

## _Abonnement :_ (classe fille)_  
Se compose d’un id_carte (unique not null), d’une date de début (not null) et d’une date de fin (not null) pour l’abonnement, et d’une fonction permettant de vérifier si l’abonnement est valide 
- hérite par référence de paiements
- Il est souscrit par un abonné
- Il est relié à une zone. Dans notre modélisation, un abonnement est relié à une zone. Il peut donc y avoir autant d’abonnements que de zones
- Il est obtenu via un paiement

## _Tickets :_ (classe fille)_   
Se compose d'un id (unique et non null), varie en fonction du type de véhicules(non null), est lié à une date de début (non null) et une date de fin (quand le client s'apprête à payer)(non null) avec date de fin > Date de début
- varie en fonction du parking (car pas le même prix selon zone du parking), un ticket permet d'accéder à un parking d'une certaine zone
- hérite par référence de paiements
- Est effectué par un occasionnel ou un abonné ne possédant pas d’abonnement valide pour la zone du parking
- sont créés uniquement s’il reste de la place dans le parking


## _Parking :_ 
Se compose d'un id(unique et non null), d'une adresse (unique et non null), d'un nom(unique et non null) et d'une fonction permettant de connaître le nombre de place limite et le nombre de places restantes en fonction du type de véhicule

- correspond à une zone (qui elle même correspond à un prix)
- est composé de places
- si on veut se garer sans être abonné, on doit prendre un ticket 

## _Place:_
Se compose d'un numéro (unique et non null), est adaptée à un type de véhicule (non null), est d'un certain type (couverte ou plein air) (non null), et possède une fonction avant de vérifier si elle est réservée ou non
- appartient à un parking, elle compose le parking 
- peut être réservée ou non

## _Zone:_
Se compose d'un nom (centre ville,  zone industrielle, zone d'activités commerciales...)(unique et non null), d'un prix ticket à l'heure ( non null), d'un prix abonnement mensuel pour une certaine zone (non null)
- peut être composée de parkings
- peut donner lieu à plusieurs abonnements   


