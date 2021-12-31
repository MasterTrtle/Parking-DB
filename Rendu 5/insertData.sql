INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);
INSERT into Client values (DEFAULT);

insert into occasionnel values('10');
insert into occasionnel values('11');

insert into abonne values('1','13','Veil','Simone','1955-09-30');
insert into abonne values('2','25','Dupond','Jacques','1972-01-28');
insert into abonne values('3','15','Navre','Charlotte','1999-08-01');
insert into abonne values('4','8','Poutire','Alice','1965-04-15');
insert into abonne values('5','4','Janvier','Elise','1988-09-10');
insert into abonne values('6','0','Vian','Boris','1967-07-07');
insert into abonne values('7','30','Holmes','Sherlock','1994-10-18');
insert into abonne values('8','17','Vivet','Lucie','1985-02-05');
insert into abonne values('9','0','Biaux','Florestan','2000-03-26');

INSERT into Vehicule values ('11tger2','camion','8');
INSERT into Vehicule values ('54d113','deux roues','2');
INSERT into Vehicule values ('24fs5','vehicule simple','1');
INSERT into Vehicule values ('32qger1','camion','5');
INSERT into Vehicule values ('1qgr18','deux roues','6');
INSERT into Vehicule values ('4eg51','vehicule simple','3');
INSERT into Vehicule values ('8eg52','camion','4');
INSERT into Vehicule values ('90rgop2','deux roues','7');
INSERT into Vehicule values ('1gre19','vehicule simple','11');
INSERT into Vehicule values ('415ger5','deux roues','10');

INSERT into zone values ('Centre-ville','2','15');
INSERT into zone values ('Industriel','1','5');
INSERT into zone values ('Commercial','6','20');

INSERT into parking values(DEFAULT,'Centre-ville','Mairie','1 place de la mairie,60200 Compiegne');
INSERT into parking values(DEFAULT,'Centre-ville','Chateau','4 place du chateau, 60200 Compiegne');
INSERT into parking values(DEFAULT,'Industriel','Usine','12 avenue du général Leclerc,60200 Compiegne');
INSERT into parking values(DEFAULT,'Industriel','Centrale','1 Square du 8 mai 1945, 60200 Compiegne');
INSERT into parking values(DEFAULT,'Commercial','Magasin','12 boulevard vivian,60200 Compiegne');
INSERT into parking values(DEFAULT,'Commercial','Capitole','135 rue des Bateliers, 60200 Compiegne');

Insert into place values('1','1','camion','couverte');
Insert into place values('1','2','vehicule simple','plein air');
Insert into place values('1','3','camion','couverte');
Insert into place values('2','1','vehicule simple','plein air');
Insert into place values('2','2','vehicule simple','plein air');
Insert into place values('2','3','deux roues','couverte');
Insert into place values('2','4','vehicule simple','couverte');
Insert into place values('3','1','vehicule simple','plein air');
Insert into place values('3','2','vehicule simple','couverte');
Insert into place values('3','3','deux roues','couverte');
Insert into place values('4','1','vehicule simple','couverte');
Insert into place values('4','2','vehicule simple','plein air');
Insert into place values('4','3','vehicule simple','couverte');
Insert into place values('4','4','camion','couverte');
Insert into place values('4','5','deux roues','couverte');
Insert into place values('5','1','vehicule simple','plein air');
Insert into place values('5','2','vehicule simple','couverte');
Insert into place values('6','1','vehicule simple','plein air');
Insert into place values('6','2','camion','couverte');
Insert into place values('6','3','deux roues','plein air');

Insert into Paiement values(DEFAULT, '2', 'automate','1');
Insert into Paiement values(DEFAULT, '1', 'automate','4');
Insert into Paiement values(DEFAULT, '5', 'internet','5');
Insert into Paiement values(DEFAULT, '6', 'automate','8');
Insert into Paiement values(DEFAULT, '20', 'internet','6');
Insert into Paiement values(DEFAULT, '12', 'automate','7');

insert into employe values (DEFAULT,'1000359');
insert into employe values (DEFAULT,'2548720');
insert into employe values (DEFAULT,'7145986');
insert into employe values (DEFAULT,'2403210');
insert into employe values (DEFAULT,'7102503');

insert into reservation values (DEFAULT,'2021-11-15','2021-11-16','11tger2','8','1','2');
insert into reservation values (DEFAULT,'2021-11-25',NULL,'11tger2','8','1','2');

insert into compte values ('a', 'randomail@utc.fr', 'b', NULL, '2');
insert into compte values ('employe','randomail@societe.fr','e','1',NULL);

insert into Ticket values ('1',DEFAULT,'1','2','11tger2','2021-11-13','2021-11-14');
insert into Ticket values ('3',DEFAULT,'2','1','54d113','2021-11-13','2021-11-14');
insert into Ticket values ('5',DEFAULT,'4','1','8eg52','2021-11-13','2021-11-14');
insert into Ticket values (NULL,DEFAULT,'4','1','1gre19','2021-11-30',NULL);

insert into abonnement values ('2',DEFAULT,'2021-11-26','2021-11-25','1','Industriel');
insert into abonnement values ('4',DEFAULT,'2023-10-08','2025-10-08','2','Centre-ville');
insert into abonnement values ('6',DEFAULT,'2021-11-30','2021-12-30','3','Commercial');