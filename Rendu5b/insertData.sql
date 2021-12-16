INSERT into Client values ('0');
INSERT into Client values ('1');
INSERT into Client values ('2');
INSERT into Client values ('3');
INSERT into Client values ('4');
INSERT into Client values ('5');
INSERT into Client values ('6');
INSERT into Client values ('7');
INSERT into Client values ('8');
INSERT into Client values ('9');
INSERT into Client values ('10');
INSERT into Client values ('11');
insert into client values ('42');



insert into occasionnel values('9');
insert into occasionnel values('10');
insert into occasionnel values('11');


insert into abonne values('0','0','Dupont','Jacques','2000-03-26');
insert into abonne values('1','13','Veil','Simone','1955-09-30');
insert into abonne values('2','25','Dupond','Jacques','1972-01-28');
insert into abonne values('3','15','Navre','Charlotte','1999-08-01');
insert into abonne values('4','8','Poutire','Alice','1965-04-15');
insert into abonne values('5','4','Janvier','Elise','1988-09-10');
insert into abonne values('6','0','Vian','Boris','1967-07-07');
insert into abonne values('7','30','Holmes','Sherlock','1994-10-18');
insert into abonne values('8','17','Vivet','Lucie','1985-02-05');
insert into abonne values('42','0','Biaux','Florestan','2000-03-26');

INSERT into Vehicule values ('111','vehicule simple','0');
INSERT into Vehicule values ('112','camion','8');
INSERT into Vehicule values ('113','deux roues','2');
INSERT into Vehicule values ('245','vehicule simple','1');
INSERT into Vehicule values ('321','camion','5');
INSERT into Vehicule values ('118','deux roues','6');
INSERT into Vehicule values ('451','vehicule simple','3');
INSERT into Vehicule values ('852','camion','4');
INSERT into Vehicule values ('902','deux roues','7');
INSERT into Vehicule values ('119','vehicule simple','11');
INSERT into Vehicule values ('415','deux roues','10');

INSERT into zone values ('Centre-ville','2','15');
INSERT into zone values ('Industriel','1','5');
INSERT into zone values ('Commercial','6','20');

INSERT into parking values('1','Centre-ville','Mairie','1 place de la mairie,60200 Compiegne');
INSERT into parking values('2','Centre-ville','Chateau','4 place du chateau, 60200 Compiegne');
INSERT into parking values('3','Industriel','Usine','12 avenue du général Leclerc,60200 Compiegne');
INSERT into parking values('4','Industriel','Centrale','1 Square du 8 mai 1945, 60200 Compiegne');
INSERT into parking values('5','Commercial','Magasin','12 boulevard vivian,60200 Compiegne');
INSERT into parking values('6','Commercial','Capitole','135 rue des Bateliers, 60200 Compiegne');

Insert into place values('1','Centre-ville','1','camion','couverte');
Insert into place values('1','Centre-ville','2','vehicule simple','plein air');
Insert into place values('1','Centre-ville','3','camion','couverte');
Insert into place values('2','Centre-ville','1','vehicule simple','plein air');
Insert into place values('2','Centre-ville','2','vehicule simple','plein air');
Insert into place values('2','Centre-ville','3','deux roues','couverte');
Insert into place values('2','Centre-ville','4','vehicule simple','couverte');
Insert into place values('3','Industriel','1','vehicule simple','plein air');
Insert into place values('3','Industriel','2','vehicule simple','couverte');
Insert into place values('3','Industriel','3','deux roues','couverte');
Insert into place values('4','Industriel','1','vehicule simple','couverte');
Insert into place values('4','Industriel','2','vehicule simple','plein air');
Insert into place values('4','Industriel','3','vehicule simple','couverte');
Insert into place values('4','Industriel','4','camion','couverte');
Insert into place values('4','Industriel','5','deux roues','couverte');
Insert into place values('5','Commercial','1','vehicule simple','plein air');
Insert into place values('5','Commercial','2','vehicule simple','couverte');
Insert into place values('6','Commercial','1','vehicule simple','plein air');
Insert into place values('6','Commercial','2','camion','couverte');
Insert into place values('6','Commercial','3','deux roues','plein air');


Insert into Paiement values('1', '2', 'automate','1');
Insert into Paiement values('2', '15', 'internet','0');
Insert into Paiement values('3', '1', 'automate','4');
Insert into Paiement values('4', '5', 'internet','5');
Insert into Paiement values('5', '6', 'automate','8');
Insert into Paiement values('6', '20', 'internet','6');
Insert into Paiement values('7', '2', 'automate','11');
Insert into Paiement values('8', '15', 'internet','9');
Insert into Paiement values('9', '1', 'automate','3');
Insert into Paiement values('10', '20', 'internet','2');
Insert into Paiement values('11', '6', 'automate','10');



insert into employe values ('1000359');
insert into employe values ('2548720');
insert into employe values ('7145986');
insert into employe values ('2403210');
insert into employe values ('7102503');

insert into reservation values ('1','2021-11-15','2021-11-16','111','1','1','Centre-ville','2');


insert into compte values ('arandomlogin','randomail@utc.fr','randompass',NULL,'2');
insert into compte values ('employe','randomail@societe.fr','e','7102503',NULL);

insert into ticket values ('1','1','vehicule simple','2021-11-13','2021-11-14','Centre-ville','1');



insert into abonnement values ('2','310','2021-11-14','2021-11-15','0', 'Centre-ville');
insert into abonnement values ('4','121','2021-10-08','2025-10-08','5', 'Industriel');
insert into abonnement values ('6','420','2021-09-30','2021-12-30','6', 'Centre-ville');
insert into abonnement values ('8','560','2021-07-05','2022-01-05','8', 'Commercial');
insert into abonnement values ('10','789','2021-01-18','2023-01-18','2', 'Industriel');
