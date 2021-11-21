#!/usr/bin/env python3
import psycopg2


#def get_connection():
 #   return psycopg2.connect("host=localhost dbname=# user=# password=#")

def get_connection():
    HOST = "tuxa.sme.utc"
    USER = "nf18a060"
    PASSWORD = "hLXrO3No"
    DATABASE = "dbnf18a060"

    return psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

