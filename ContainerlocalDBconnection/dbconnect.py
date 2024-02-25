import pymysql

# Replace these values with your actual MySQL connection details
host = "localhost"
user = "abstract-programmer"
password = "Ramswarup@104"
database = "userinfo"

# Establish a connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

try:
    # Create a cursor object to interact with the database
    with connection.cursor() as cursor:
        # Example: Execute a SQL query
        cursor.execute("SELECT * FROM employees")
        
        # Fetch the result
        result = cursor.fetchall()
        print(result)

finally:
    # Close the connection when done
    connection.close()
