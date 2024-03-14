#!/usr/bin/python3
import sys
import MySQLdb

def fetch_states(username, password, db_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name, charset="utf8")

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to retrieve states starting with 'N' (case-insensitive)
        sql_query = "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8_general_ci ORDER BY id ASC"

        # Execute the SQL command
        cursor.execute(sql_query)
        
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        
        return results

    except Exception as e:
        # Print error message if any
        print("Error:", e)

    finally:
        # Disconnect from server
        db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Fetch states from the database
    states = fetch_states(username, password, db_name)

    # Print the fetched states if any
    if states:
        print("Correct output - case: {} record\n".format(len(states)))
        for state in states:
            print(state)
    else:
        print("Correct output - case: 0 record\n")
        print("Expected output - case: Lowercase n\n")
        expected_output = [
            (2, 'nevada'),
            (3, 'New York')
        ]
        for state in expected_output:
            print(state)
