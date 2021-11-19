INSERT into Client values ('0');
INSERT into Client values ('1');
INSERT into Client values ('2');

insert into occasionnel values('1');
insert into abonne values('0','0','Dupont','Jacques','2000-03-26');
insert into abonne values('1','13','Veil','Simone','1955-09-30');
insert into abonne values('2','25','Dupond','Jacques','1972-01-28');
insert into abonne values('3','15','Navre','Charlotte','1999-08-01');
insert into abonne values('4','8','Poutire','Alice','1965-04-15');
insert into abonne values('5','4','Janvier','Elise','1988-09-10');
insert into abonne values('6','0','Vian','Boris','1967-07-07');
insert into abonne values('7','30','Holmes','Sherlock','1994-10-18');
insert into abonne values('8','17','Vivet','Lucie','1985-02-05');

INSERT into Vehicule values ('111','vehicule simple','0');
INSERT into Vehicule values ('112','camion','8');
INSERT into Vehicule values ('113','deux roues','2');
INSERT into Vehicule values ('245','vehicule simple','1');
INSERT into Vehicule values ('321','camion','5');
INSERT into Vehicule values ('118','deux roues','6');
INSERT into Vehicule values ('451','vehicule simple','3');
INSERT into Vehicule values ('852','camion','4');
INSERT into Vehicule values ('902','deux roues','7');

INSERT into zone values ('Centre-ville','2','15');
INSERT into zone values ('Industriel','1','5');
INSERT into zone values ('Commercial','5','20');

INSERT into parking values('1','Centre-ville','Mairie','1 place de la mairie,60200 Compiegne');
INSERT into parking values('2','Centre-ville','Chateau','4 place du chateau, 60200 Compiegne');
INSERT into parking values('3','Industriel','Usine','12 avenue du général Leclerc,60200 Compiegne');
INSERT into parking values('4','Industriel','Centrale','1 Square du 8 mai 1945, 60200 Compiegne');
INSERT into parking values('5','Commercial','Magasin','12 boulevard vivian,60200 Compiegne');
INSERT into parking values('6','Commercial','Capitole','135 rue des Bateliers, 60200 Compiegne');

Insert into place values('1','Centre-ville','1','camion','couverte');
--faut modifier les valeurs ci dessous en fonction des parkings, pas eu le temps
--Insert into place values('1','Centre-ville','2','vehicule simple','plein air');
--Insert into place values('1','Centre-ville','1','camion','couverte');
--Insert into place values('2','Centre-ville','2','vehicule simple','plein air');
--Insert into place values('2','Centre-ville','2','vehicule simple','plein air');
--Insert into place values('2','Centre-ville','1','deux roues','couverte');
--Insert into place values('2','Centre-ville','1','deux roues','couverte');
--Insert into place values('3','Centre-ville','1','deux roues','couverte');
--Insert into place values('3','Centre-ville','1','deux roues','couverte');
--Insert into place values('3','Centre-ville','1','deux roues','couverte');

Insert into Paiement values('1', '6', 'automate','1');
Insert into Paiement values('2', '15', 'internet','2');


insert into Employe values ('1000359');

insert into reservation values ('1','2021-11-15','2021-11-16','111','1','1','Centre-ville','2');

insert into compte values ('arandomlogin','randomail@utc.fr','randompass',NULL,'2');

insert into ticket values ('1','1','camion','2021-11-13','2021-11-14','Centre-ville','1');

insert into abonnement values ('2','1','2021-11-14','2021-11-15','2');
