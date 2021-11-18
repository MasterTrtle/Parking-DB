INSERT into Client values ('0');
INSERT into Client values ('1');
INSERT into Client values ('2');

insert into occasionnel values('1');
insert into abonne values('0','0','Dupont','Jacques','2000-03-26');
insert into abonne values('2','25','Dupond','Jacques','1972-01-01');

INSERT into Vehicule values ('111','vehicule simple','0');
INSERT into Vehicule values ('112','camion','1');
INSERT into Vehicule values ('113','deux roues','2');

INSERT into zone values ('Centre-ville','2','15');

INSERT into parking values('1','Centre-ville','Mairie','1 place de la mairie,60200 Compiegne');
INSERT into parking values('2','Centre-ville','Chateau','4 place du chateau 60200 Compiegne');

Insert into place values('1','Centre-ville','1','camion','couverte');
Insert into place values('1','Centre-ville','2','vehicule simple','plein air');
Insert into place values('2','Centre-ville','1','deux roues','couverte');

Insert into Paiement values('1', '6', 'automate','1');
Insert into Paiement values('2', '15', 'internet','2');


insert into Employe values ('1000359');

insert into reservation values ('1','2021-11-15','2021-11-16','111','1','1','Centre-ville','2');

insert into compte values ('arandomlogin','randomail@utc.fr','randompass',NULL,'2');

insert into ticket values ('1','1','camion','2021-11-13','2021-11-14','Centre-ville','1');

insert into abonnement values ('2','1','2021-11-14','2021-11-15','2');
