#!/usr/bin/python3

import MySQLdb
import sys
""" Get all states with a given argument as name"""

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
        cursor = db.cursor()

        # Execute query to retrieve states matching the provided name (safe from injections)
        sql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cursor.execute(sql_query, (search_name,))
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

