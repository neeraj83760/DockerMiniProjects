import pymysql

# Replace these variables with your actual MySQL credentials
host = 'localhost'
user = 'abstract-programmer'
password = 'Ramswarup@104'
database = 'userinfo'

def connect_to_database():
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        print("Connected to the database!")
        # Perform database operations here
        connection.close()
    except pymysql.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_database()
