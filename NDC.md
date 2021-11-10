# Note de Clarification

Pour les associations d'héritage : anticiper en quelques mots le types de transformation en relationnel qui sera privilégié
Indiquer les utilisateurs de la BD avec leurs rôles
Indiquer quelques requêtes types qu'on voudra faire dans la BD (celles indiqués sur le sujet et d'autres)


un abonnement est lié àunz eone: on peut avoir autant d'abonnements que de zones

les occasionnels n'achètent que des tickets, on n'a pas plus d'infos que leur carte bleu

## _Parking :_ 
Se compose d'un nom (unique et non null), d'une adresse (unique et non null) et d'un nombre de place limite (non null)
     est composé de 1 à N places
    correspond à une zone (qui elle même correspond à un prix)
    si on veut se garer, on doit prendre un ticket 

## _Paiements :_
Se compose d'un id de transaction (unique et non null), d'un montant (unique et non null)
    peut se faire par Guichet ou par automate si on utilise tickets, ou par carte abonnement

## _Place:_
Se compose d'un numéro (unique et non null), est adaptée à un type de véhicule, est d'un certain type (couverte ou plein air), peut être réservée ou non 
    appartient à un parking
    

## Utilisateur (classe mère abstraite)
  
Prénom (obligatoire)   
  
Nom(obligatoire)  
   
Date_de_naissance (obligatoire) 
    
**(Prénom, Nom, Date_de_naissance) : clé** 
     
Points_fidélité permet l'instauration d'un système de fidelité comme demandé dans le sujet. Chaque utilisateur qu'il soit abonné ou non profite du système de fidélité.  
  
Un utilisateur est soit un abonné soit un occasionel.

## Abonné (classe fille de Utilisateur)

## Non Abonné (classe fille de Utilisateur)

## Véhicule 
  
Immatriculation (Obligatoire): clé  
  
Type (Obligatoire): Type_Véhicule  
 
Il est nécessaire de connaitre le type du véhicule pour lui attribuer une place adaptée dans le parking.
  
Nom (Obligatoire)

## _Cartes mensuelle:_
id
fin de validité
	
## _Zone:_
Type (centre ville,  zone industrielle, zone d'activités commerciales)
prix du parking lié
Transaction: (classe association entre Utilisateur et
date
id
montant
mode paiement

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

