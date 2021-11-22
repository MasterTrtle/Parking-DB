#!/usr/bin/env python3
import psycopg2


def get_connection():
    return psycopg2.connect("host=localhost dbname=# user=# password=#")



