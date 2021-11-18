import connect

if __name__ == '__main__':
    conn = connect.get_connection()
    cur = conn.cursor()
    #sql = "select * from vehicule;"
    #cur.execute(sql)
    #raw = cur.fetchone()
    #while raw:
    #    print(raw[0])
    #    raw = cur.fetchone()
