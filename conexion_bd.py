import psycopg2
DSN = "dbname=prueba user=postgres password=123456"

def connectionBd():
    conn = psycopg2.connect(DSN)
    cursor = conn.cursor()
    return cursor
    #query = "SELECT * FROM persona;"
    #cur.execute(query)
    #for persona in cur.fetchall():
    #    print(persona)
    #cur.close()
    #con.close()

#if __name__== "__main__":
#   leer_datos();