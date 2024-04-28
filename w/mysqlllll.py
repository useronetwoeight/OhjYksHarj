import mysql.connector

bamse = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    passwd='bamse',
    autocommit=True
    )

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to count the rows in your table
cursor.execute('SELECT COUNT(*) FROM flight_game')

# Fetch the result
row_count = cursor.fetchone()[0]

# Close the cursor and the connection
cursor.close()
conn.close()

print(f"Number of rows: {row_count}")
