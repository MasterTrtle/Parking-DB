-- on on récupère l'ensemble des reservation (idPlace, idParking, debut, fin seront placés en paramètre)
SELECT r.debut, r.fin FROM Reservation r, place p ON r.numero_place=p.numero AND  r.parking_place = p.id_parking WHERE p.id_parking = idParking AND p.numero = idPlace

-- on effectue une réservation (debut, fin, idvehicule, client, idParking,zone, idPlace seront passés en paramètre)
INSERT into Reservation values (debut, fin, idvehicule, client, idParking, zone, idPlace);

-- consulter son solde de fidélité (idabonne sera passé en paramètre)
SELECT points_fidelite FROM Abonne WHERE id_client = idabonne;

--voir le nombre d'abonnements par zone
SELECT zone, Count(id_carte) FROM Abonnement GROUP BY zone;

--voir le nombre de parkings par zone
SELECT zone, Count(id_parking) FROM Parking GROUP BY zone;


-- récupérer toute les zones
SELECT * FROM Zone ORDER BY nom;

-- mettre à jour le tarif abonnements d'une zone (nouveau_tarif_A et nom_zone_choisie seront passés en paramètre)
UPDATE Zone SET tarif_abonnement= nouveau_tarif_A WHERE nom=nom_zone_choisie;

-- mettre à jour le tarif tickets d'une zone (nouveau_tarif_T et nom_zone_choisie seront passés en paramètre)
UPDATE Zone SET tarif_ticket=nouveau_tarif_T WHERE nom=nom_zone_choisie;

-- mettre à jour les tarif tickets et abonnements d'une zone (nouveau_tarif_T, nouveau_tarif_A et nom_zone_choisie seront passés en paramètre)
UPDATE Zone SET tarif_abonnement=nouveau_tarif_A, tarif_ticket=nouveau_tarif_T WHERE nom=nom_zone_choisie;
