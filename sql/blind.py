import mysql.connector
from mysql.connector import Error

DB_URL = "localhost"
DB_USER = "user"
DB_PASSWORD = "password"
DB_NAME = "mydb"

def check_account_exists(user_id):
    try:
        # Establish a connection to the database
        conn = mysql.connector.connect(
            host=DB_URL,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Query to check if user exists
            query = f"SELECT 1 FROM users WHERE id = '{user_id}'"
            cursor.execute(query)

            # Check if any record exists
            if cursor.fetchone():
                print("Account exists!")  # True condition
            else:
                print("Account does not exist.")  # False condition

            cursor.close()
            conn.close()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()

def main():
    user_id = input("Enter your user ID to check if your account exists: ")
    check_account_exists(user_id)

if __name__ == "__main__":
    main()
