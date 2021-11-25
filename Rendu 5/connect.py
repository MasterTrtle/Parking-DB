#!/usr/bin/env python3
import psycopg2


#def get_connection():
 #   return psycopg2.connect("host=localhost dbname=# user=# password=#")

def get_connection():
    HOST = ""
    USER = ""
    PASSWORD = ""
    DATABASE = ""

    return psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

