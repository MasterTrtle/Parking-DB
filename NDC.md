# Note de Clarification

Classes: 

_Parking :_ 
est composé de 1 à N places
correspond à une zone (qui elle même correspond à un prix)

_Mode de paiements (mère):_ (classe association entre parking et utilisateur : change pour chaque parking que l’user a)

_Mode de paiement Occasionels:_ fille 1 (xor avec fille 2)
tickets à l’heure guichet
tickets à l’heure automate

_Mode de paiement Abonnés:_ fille2 (xor avec fille 1)
carte mensuelle renouvelable chaque mois 


_Place:_
plein air ou couvertes
correspond a une véhicule

_Véhicule:_
type deux_roues; camion; véhicule simple
nom
immatriculation

_Utilisateur:_ (classe mère)
a un ou plusieurs véhicules
nom
prenom
âge
nombre de points de fidélité

_Utilisateur occasionnel _ (classe fille de Utilisateur)

_Utilisateur abonné_ (classe fille de Utilisateur):
a une carte
 

_Cartes mensuelle:_
id
fin de validité
	
_Zone:_
Type (centre ville,  zone industrielle, zone d'activités commerciales)
prix du parking lié
Transaction: (classe association entre Utilisateur et
date
id
montant
mode paiement

