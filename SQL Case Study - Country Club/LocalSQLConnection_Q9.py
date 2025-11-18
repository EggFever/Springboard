import sqlite3
from sqlite3 import Error

 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
        SELECT 
            facility_name,
            member_name,
            cost
        FROM (
            SELECT 
                b.bookid,
                f.name AS facility_name,
                m.firstname || ' ' || m.surname AS member_name,
                CASE 
                    WHEN b.memid = 0 THEN b.slots * f.guestcost
                    ELSE b.slots * f.membercost
                END AS cost,
                DATE(b.starttime) AS booking_date
            FROM Bookings AS b
            JOIN Facilities AS f ON b.facid = f.facid
            JOIN Members AS m ON b.memid = m.memid
        ) AS booking_costs
        WHERE booking_date = '2012-09-14'
        AND cost > 30
        ORDER BY cost DESC;
        """
    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("2. Query all tasks")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()