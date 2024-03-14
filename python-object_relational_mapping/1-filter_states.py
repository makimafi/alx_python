#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to retrieve states starting with 'N' (case-insensitive)
    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8_general_ci ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql_query)
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        # Display the results
        for row in results:
            print(row)
    except Exception as e:
        # Rollback in case there is any error
        print("Error:", e)
        db.rollback()

    # Disconnect from server
    db.close()

    # Expected output for lowercase 'n'
    expected_output = [
        (2, 'nevada'),
        (3, 'New York')
    ]

    # Print the expected output
    print("\nExpected output - case: Lowercase n\n")
    for state in expected_output:
        print(state)
