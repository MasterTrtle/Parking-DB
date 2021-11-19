-- on on récupère l'ensemble des reservation d'une place  (idPlace, idParking, debut, fin seront placés en paramètre)
SELECT r.debut, r.fin FROM Reservation r JOIN place p ON r.numero_place=p.numero AND  r.parking_place = p.id_parking WHERE p.id_parking = idParking AND p.numero = idPlace;

--récuperer l'ensemble des places d'un type précis dans un parking cible
SELECT p.idplace FROM Place a JOIN parking b ON a.id_parkiNG = b.id_parking AND p.type_vehicule ="cible";

-- on effectue une réservation (debut, fin, idvehicule, client, idParking,zone, idPlace seront passés en paramètre)
INSERT into Reservation values (debut, fin, idvehicule, client, idParking, zone, idPlace);

-- récupérer l'ensemble des véhicules d'un client
SELECT v.immat v.type_vehicule FROM Vehicule v JOIN Client c ON v.propietaire = c.id_client;

--selectioner un parking en fonction de son nom
SELECT * FROM PARKING WHERE nom = "cible";

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
