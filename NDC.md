# Note de Clarification

Pour les associations d'héritage : anticiper en quelques mots le types de transformation en relationnel qui sera privilégié
Indiquer les utilisateurs de la BD avec leurs rôles
Indiquer quelques requêtes types qu'on voudra faire dans la BD (celles indiqués sur le sujet et d'autres)

un abonnement est lié àunz eone: on peut avoir autant d'abonnements que de zones


les occasionnels n'achètent que des tickets, on n'a pas plus d'infos que leur carte bleu

## _Parking :_ 
Se compose d'un nom (unique et non null), d'une adresse (unique et non null) et d'un nombre de place limite (non null)

- correspond à une zone (qui elle même correspond à un prix)
- si on veut se garer, on doit prendre un ticket 

## _Place:_
Se compose d'un numéro (unique et non null), est adaptée à un type de véhicule, est d'un certain type (couverte ou plein air)
- appartient à un parking
- peut être réservée ou non

## _Zone:_
Se compose d'un nom (centre ville,  zone industrielle, zone d'activités commerciales...)(non null), d'un prix ticket à l'heure ( non null), d'un prix abonnement mensuel pour une certaine zone (non null)
- peut être composée de parkings 

## _Tickets :_   
Se compose d'un id (unique et non null), varie en fonction du type de véhicules(non null), est lié à une date de début (non null) et une date de fin (quand l'utilisateur s'apprête à payer)(non null)
- peuvent être payés au guichet ou à l'automate
- varie en fonction du parking (car pas le même prix)
- sont créés que si il reste de la place dans le parking

## _Paiements :_
Se compose d'un id de transaction (unique et non null), d'un montant (non null)
- peut se faire par Guichet ou par automate si on utilise tickets
- permet également de faire le paiement d'un abonnement

## _Caisse :_
Se compose d'un id (unique et non null), d'un type de caisse (guichet, automate)
- classe association entre paiements et tickets

## _Abonné_ :
Se compose d'un prenom ( non null), d'un nom (not null) d'une date de naissance (not null) 
- il est associé à un compte
- possède une ou plusieurs voitures
- possède autant d'abonnements qu'il le souhaite, sachant qu'il s'agit dun abonnement par zone 
L'utilisateur occasionnel n'a pas besoin d'une classe puisqu'on n'a aucune info sur lui

## _Compte_ :   
Se compose d'un id (unique non null), d'un mot de passe (not null) d'une adresse mail (not null), d'un compteur de points de fidélités
Points_fidélité permet l'instauration d'un système de fidelité comme demandé dans le sujet. Chaque utilisateur qu'il soit abonné ou non profite du système de fidélité.  
- il est associé à un utilisateur 

## Véhicule 
Se compose d'une immatriculation (unique not null), d'un type (not null)     
Il est nécessaire de connaitre le type du véhicule pour lui attribuer une place adaptée dans le parking.
  
## Abonnement : 

ID (obligatoire) : clé 

Date_debut (obligatoire)

Date_fin (obligatoire) permet de determiner la date de fin d’abonnement et de l’exploiter dans l’application


## Carte :

ID (obligatoire) : clé

## Compte :

ID (obligatoire) : clé

Le compte est l’association des classes abonnements, carte et abonné qui permet de lier les 3 informations dans une seule table pour simplifier les requêtes de l’application

## Caisse :

ID (obligatoire) : clé

Type_Caisse (obligatoire) : Répond à la demande du sujet de connaitre le type de caisse sur lequel les utilisateurs payent et d’obtenir des statistiques

Ticket : ID (obligatoire) : clé

Date_début : permet de définir le prix de parking dans l’application

## Paiement :
ID_transaction (obligatoire) : clé

Prix : défini par l’application, permet de sortir des statistiques.

La classe paiement est l’association des classes Carte, caisse et ticket et permet de suivre tous les paiements réalisés en caisse, que ce soit pour les abonnés ou les non-abonnés.

