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

            # Query with a placeholder for safe parameter binding
            query = "SELECT 1 FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))

            # Check if any record exists
            if cursor.fetchone():
                print("Account exists!")
            else:
                print("Account does not exist.")

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
