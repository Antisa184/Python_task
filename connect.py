import psycopg2
from config import config

def connect(sheet):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
    # check if table exists
        cur.execute("""SELECT EXISTS(SELECT 1 FROM information_schema.tables 
              WHERE table_catalog='postgres' AND 
                    table_schema='public' AND 
                    table_name='foreo');""")
        if not cur.fetchone()[0]:
        # create a table
            cur.execute("""CREATE TABLE foreo (
                store_no VARCHAR(255) UNIQUE PRIMARY KEY,
                store VARCHAR(255) NOT NULL,
                ty_units INTEGER,
                ly_units INTEGER,
                tw_sales NUMERIC,
                lw_sales NUMERIC,
                lw_var NUMERIC,
                ly_sales NUMERIC,
                ly_var NUMERIC,
                ytd_sales NUMERIC,
                lytd_sales NUMERIC,
                lytd_var NUMERIC
                )"""
            )
    # load rows
        for i in range(len(sheet.index)-1):
            row=sheet.iloc[i]
            print(row[0])
            sql = """ INSERT INTO foreo (store_no, store, ty_units, ly_units, tw_sales, lw_sales, lw_var, ly_sales, ly_var, ytd_sales, lytd_sales, lytd_var) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            data=(str(row[0]), str(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]))
            cur.execute(sql,data)
            #id = cur.fetchone()[0]
            print(data)
            conn.commit()
	# close the communication with the PostgreSQL
        cur.close()

    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')