# Note de Clarification

## Utilisateurs : 
On identifie trois utilisateurs différents.   
### Nouvel utilisateur
C'est un client qui se connecte pour la première fois sur la plateforme.  
Si c'est un client, étant donné que seuls les abonnés ont un compte, la création de son compte implique la création d'un abonnement.  
Un employé peut également se créer un compte si il n'en possède pas déjà un.
### Abonné
Les abonnés peuvent se connecter sur la plateforme grâce à leur compte (login et mot de passe). Ils peuvent ainsi gérer leurs réservations et leurs abonnements.
### Employé
On considère que les employés de l'entreprise possèdent également un compte. Ils peuvent consulter des statistiques et diverses informations.

## Requêtes types :
-	Consulter les statistiques
-	Consulter le nombre de places restantes sur un parking
-	Réserver une place
-	Changer un parking de zone
-	Changer le tarif d’une zone
-	Se créer un compte
-	Requêtes associées aux users décrites précédemment 
-	Consulter son solde de fidélité
-	Afficher le nombre de places disponibles dans l’ensemble des parkings
-	…


## Compte :

Se compose d'un login (unique not null), d’un prenom (non null), d’un mot de passe(not null), d'un nom (not null) et d’une adresse mail (unique not null).  
C'est une classe mère abstraite car elle ne représente rien de concret.   
C’est la classe mère de employé et abonné, puisqu'ils ont besoin des attributs de Compte.  
On choisira de transformer cet héritage par référence car un héritage par classe mère poserait problème avec les associations et un héritage par les classes filles rendrait les requêtes de connexions plus complexes.

## Employé : 
Se compose d’un numéro de sécurité sociale (unique not null)
- Il hérite du compte par référence 


## Abonné :
Se compose d'une date de naissance (not null), et d’un solde de fidélité (not null) qui permettra de lui calculer des avantages.  
L'utilisateur occasionnel n'a pas besoin d'une classe puisque nous n'avons aucune information sur lui.  

- Il hérite du compte par référence
- Il possède 0 ou plusieurs voitures
- Il souscrit à autant d'abonnements qu'il le souhaite, sachant qu'il s'agit d'un abonnement par zone 
- Il peut effectuer des réservations de places pour ses véhicules


## Véhicule :
Se compose d'une immatriculation (unique not null), d'un type (not null): deux roues, camion, véhicule simple.     
Il est nécessaire de connaitre le type du véhicule pour lui attribuer une place adaptée dans le parking.
-	Il peut être associé à une réservation
-	Il appartient à un abonné
  
## Abonnement :
Se compose d’un id_carte (unique not null), d’une date de début (not null) et d’une date de fin (not null) pour l’abonnement, et d’une fonction permettant de vérifier si l’abonnement est valide 
-	Il est souscrit par un abonné
-	Il est relié à une zone. Dans notre modélisation, un abonnement est relié à une zone. Il peut donc y avoir autant d’abonnements que de zones.
- Il doit être acheté

## Réservation :
Se compose d’un id (unique not null), d’une date de début (not null) et d’une date de fin (not null), et d’une fonction permettant de vérifier si la réservation est possible.  
Dans notre modélisation, un abonné peut réserver à l’avance afin d’être sûr qu’une place sera disponible pour lui alors qu'un occasionnel ne peut prendre une place que lorsqu’il se rend sur le parking pour prendre un ticket.

-	Elle est associée au véhicule qui a réservé la place
-	Elle est faite par un abonné
-	Elle réserve une place en particulier
-   Le type du véhicule lié à la réservation doit correspondre au type de la place concernée
-   Il doit rester assez de place dans le parking
-   Deux réservations ne peuvent pas se chevaucher pour une même place

## Ticket :   
Se compose d'un id (unique et non null), varie en fonction du type de véhicule (non null), est lié à une date de début (non null) et une date de fin (quand l'utilisateur s'apprête à payer)(non null) avec date de fin > date de début
- Peuvent être payés au guichet ou à l'automate
- Varie en fonction du parking (car pas le même prix selon zone du parking), un ticket permet d'accéder à un parking d'une certaine zone
- sont créés seulement s'il reste de la place dans le parking

## Paiement :
Se compose d'un id de transaction (unique et non null), d'un montant (non null) et d'une fonction permettant de calculer le montant.
- Peut se faire par guichet ou par automate si on utilise les tickets
- Permet également de faire le paiement d'un abonnement
- xor: Se fait soit pour un ticket soit pour un abonnement

## Caisse :
Se compose d'un id (unique et non null), d'un type de caisse (guichet, automate)
- classe association entre paiement et ticket


## Parking : 
Se compose d'un id (unique et non null), d'une adresse (unique et non null), d'un nom (unique et non null) et d'une fonction permettant de connaître le nombre de place limite et le nombre de places restantes en fonction du type de véhicule

- Correspond à une zone (qui elle même correspond à un prix)
- Si on veut se garer sans être abonné, on doit prendre un ticket 

## Place:
Se compose d'un numéro (unique et non null), est adaptée à un type de véhicule (non null), est d'un certain type (couverte ou plein air) (non null), et possède une fonction afin de vérifier si elle est réservée ou non
- Appartient à un parking, elle compose le parking 
- Peut être réservée ou non

## Zone:
Se compose d'un nom (centre ville,  zone industrielle, zone d'activités commerciales...)(unique et non null), d'un prix ticket à l'heure (non null), d'un prix abonnement mensuel (non null)
- Peut être composée de parkings
- Peut donner lieu à plusieurs abonnements   

