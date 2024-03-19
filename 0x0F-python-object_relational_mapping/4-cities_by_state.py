#!/usr/bin/python3

import MySQLdb
import sys
""" Get all cities and order by cities id"""

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
        cursor = db.cursor()

        # Execute query to retrieve all cities
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        cursor.close()
        db.close()

