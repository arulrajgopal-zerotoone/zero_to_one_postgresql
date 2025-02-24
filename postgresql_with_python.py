# install--> pip install psycopg2-binary or pip install psycopg2-binary
import psycopg2


try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        dbname="mydatabase",
        user="postgres",
        password = "test@1234",
        port="5432"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query
    cursor.execute("select * from employees")

    # Fetch the results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
