# Note de Clarification

## _UtilisateursBDD :_ 
-	Nouvel utilisateur pour se créer un abonnement (et donc un compte)
-	Abonné pour gérer ses abonnements et réserver
-	Société pour consulter ses stat et diverses informations 

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


## Compte :

Se compose d'un id (unique not null), d’un prenom (non null), d’un mot de passe(not null)  d'un nom (not null), d’une adresse mail (not null) 

C’est la classe mère de employé et abonné

## _Employé_ :
Se compose d’un numéro de sécu social (unique not null)
- il hérite du compte par référence 


## _Abonné_ :
Se compose date de naissance (not null), et d’un solde de fidélité (not null) qui permettra de lui calculer des avantages
- il hérite du compte par référence
- possède une ou plusieurs voitures
- possède autant d'abonnements qu'il le souhaite, sachant qu'il s'agit dun abonnement par zone 
- peut effectuer des réservations
L'utilisateur occasionnel n'a pas besoin d'une classe puisqu'on n'a aucune info sur lui


## _Véhicule :_
Se compose d'une immatriculation (unique not null), d'un type (not null)     
Il est nécessaire de connaitre le type du véhicule pour lui attribuer une place adaptée dans le parking.
-	Il peut être associé à une réservation
-	Il appartient à un user
  
## _Abonnement : _
Se compose d’un id_carte (unique not null), d’une date de début et d’une date de fin pour l’abonnement, et d’une fonction permettant de vérifier si l’abonnement est valide 
-	Il est souscrit par un abonné
-	Il est relié à une zone. Dans notre modélisation, un abonnement est relié à une zone. Il peut donc y avoir autant d’abonnements que de zones

## _Réservation : _
Se compose d’un id (unique not null), d’une date de début et d’une date de fin, et d’une fonction permettant de vérifier si la réservation est possible 
-	Elle est associée au véhicule qui a réservé la place
-	Elle est faite par un abonné
-	Elle réserve une place en particulier

Dans notre modélisation, un abonné peut réserver à l’avance afin d’être sûr qu’une place sera disponible pour lui et un occasionnel ne peut réserver une place que lorsqu’il se rend sur le parking pour prendre un ticket. 


## _Tickets :_   
Se compose d'un id (unique et non null), varie en fonction du type de véhicules(non null), est lié à une date de début (non null) et une date de fin (quand l'utilisateur s'apprête à payer)(non null)
- peuvent être payés au guichet ou à l'automate
- varie en fonction du parking (car pas le même prix)
- sont créés que si il reste de la place dans le parking

## _Paiements :_
Se compose d'un id de transaction (unique et non null), d'un montant (non null)
- peut se faire par Guichet ou par automate si on utilise tickets
- permet également de faire le paiement d'un abonnement
Se fait soit par ticket soit par abonnement

## _Caisse :_
Se compose d'un id (unique et non null), d'un type de caisse (guichet, automate)
- classe association entre paiements et tickets


## _Parking :_ 
Se compose d'un id(unique et non null), d'une adresse (unique et non null) et d'un nombre de place limite (non null), d’une fonction permettant de connaître le nombre de places limites et le nombre de places restantes

- correspond à une zone (qui elle même correspond à un prix)
- si on veut se garer, on doit prendre un ticket 

## _Place:_
Se compose d'un numéro (unique et non null), est adaptée à un type de véhicule, est d'un certain type (couverte ou plein air)
- appartient à un parking
- peut être réservée ou non

## _Zone:_
Se compose d'un nom (centre ville,  zone industrielle, zone d'activités commerciales...)(non null), d'un prix ticket à l'heure ( non null), d'un prix abonnement mensuel pour une certaine zone (non null)
- peut être composée de parkings
- est relié à un abonnement puisque le prix de l’abonnement varie en fonction de la zone  

