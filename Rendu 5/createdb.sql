DROP TABLE IF EXISTS client CASCADE;
DROP TABLE IF EXISTS vehicule CASCADE;
DROP TABLE IF EXISTS paiement CASCADE;
DROP TABLE IF EXISTS zone CASCADE;
DROP TABLE IF EXISTS parking CASCADE;
DROP TABLE IF EXISTS place CASCADE;
DROP TABLE IF EXISTS reservation CASCADE;
DROP TABLE IF EXISTS employe CASCADE;
DROP TABLE IF EXISTS occasionnel CASCADE;
DROP TABLE IF EXISTS abonne CASCADE;
DROP TABLE IF EXISTS compte CASCADE;
DROP TABLE IF EXISTS abonnement CASCADE;
DROP TABLE IF EXISTS ticket CASCADE;

DROP TYPE IF EXISTS type_vehicule;
DROP TYPE IF EXISTS type_place;
DROP TYPE IF EXISTS type_caisse;

CREATE TYPE type_vehicule AS ENUM ('deux roues', 'camion', 'vehicule simple');
CREATE TYPE type_place AS ENUM ('couverte', 'plein air couverte', 'plein air');
CREATE TYPE type_caisse AS ENUM ('guichet', 'automate', 'internet');

CREATE TABLE Client(
    id_client serial primary key
);

CREATE TABLE Vehicule(
    immat varchar(40) primary key,
    type_vehicule type_vehicule not null,
    proprietaire int not null,
    foreign key (proprietaire) references Client(id_client) on delete cascade
);

CREATE TABLE Paiement(
    id_transaction serial primary key,
    montant int not null,
    type_caisse type_caisse not null,
    client int not null,
    foreign key (client) references Client(id_client) on delete cascade
);

CREATE TABLE Zone(
    nom varchar(40) primary key,
    tarif_ticket int not null,
    tarif_abonnement int not null
);

CREATE TABLE Parking(
    id_parking serial primary key,
    zone varchar(40),
    nom varchar(40) unique not null,
    adresse varchar(100) unique not null,
    foreign key (zone) references zone(nom) on delete cascade
);

CREATE TABLE Place(
    id_parking int,
    numero int,
    type_vehicule type_vehicule not null,
    type_place type_place not null,
    primary key (id_parking,numero),
    foreign key (id_parking) references parking(id_parking) on delete cascade
);

CREATE TABLE Reservation(
    id_reservation serial primary key,
    debut date not null,
    fin date not null,
    vehicule varchar(40) not null,
    client int not null,
    parking_place int not null,
    numero_place int not null,
    foreign key (vehicule) references vehicule(immat) on delete cascade,
    foreign key (client) references client(id_client) on delete cascade,
    foreign key (parking_place,numero_place) references place(id_parking,numero) on delete cascade,


    check (date_part('day', fin::timestamp)-date_part('day',debut::timestamp)>0 OR date_part('hour',fin::timestamp) - date_part('hour',debut::timestamp)>0)
); -- check (DATEDIFF(day or hour, debut, fin) > 0) si pas Mysql
   -- client = vehicule.client
   -- date ne se chevauchent pas
   -- vehicule.type = place.type
   -- => A faire dans l'applicatif car necessite des subqueries

CREATE TABLE Employe(
    id_employe serial primary key,
    num_secu int unique not null
);

CREATE TABLE Occasionnel(
    id_client int primary key,
    foreign key (id_client) references client(id_client) on delete cascade
);

CREATE TABLE Abonne(
    id_client int primary key,
    points_fidelite int not null,
    nom varchar(40) not null,
    prenom varchar(40) not null,
    date_naiss date not null,
    foreign key (id_client) references client(id_client) on delete cascade,
    check ((date_part('year', NOW()::timestamp )-date_part('year', date_naiss::timestamp ))>=18)
    );

CREATE TABLE Compte(
    login varchar(40) primary key,
    mail varchar(50) unique,
    mdp varchar(40) not null,
    employe int unique,
    abonne int unique,
    foreign key (employe) references employe(id_employe) on delete cascade,
    foreign key (abonne) references abonne(id_client) on delete cascade,
    check ((employe IS NOT NULL and abonne is NULL) or (abonne is not null and employe is null))
);

CREATE TABLE Abonnement(
    id_transaction int primary key,
    id_carte serial unique not null,
    debut date not null,
    fin date not null,
    abonne int not null,
    zone varchar(40) not null,
    foreign key (id_transaction) references paiement(id_transaction) on delete cascade,
    foreign key (abonne) references abonne(id_client) on delete cascade,
    foreign key (zone) references zone(nom) on delete cascade
  ); -- check (DATEDIFF(month, debut, fin) > 0) si pas Mysql

CREATE TABLE Ticket(
    id_transaction int primary key,
    id_ticket serial,
    id_place int not null,
    type_vehicule type_vehicule not null,
    type_place type_place not null,
    debut date not null,
    fin date,
    id_parking int not null,
    foreign key (id_transaction) references paiement(id_transaction) on delete cascade,
    foreign key (id_parking) references parking(id_parking) on delete cascade,

    check (date_part('day', fin::timestamp) - date_part('day',debut::timestamp)>0 OR date_part('hour',fin::timestamp) - date_part('hour',debut::timestamp)>0)
    ); -- check (DATEDIFF(day or hour, debut, fin) > 0) si pas Mysql
