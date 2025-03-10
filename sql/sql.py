class SQLExample:

    @staticmethod
    def login_user(username, password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
        print(f"Executing query: {query}")
        return SQLExample.execute_query(query)

    @staticmethod
    def get_user_role(username):
        # Hardcoded role retrieval for demonstration purposes
        if username == "admin":
            return "Administrator"
        else:
            return "User"

    @staticmethod
    def sanitize_input(input_str):
        return input_str.replace("'", "''")

    @staticmethod
    def execute_query(query):
        # Simulate a successful query execution
        return "admin" in query

    @staticmethod
    def main(username, password):
        username = SQLExample.sanitize_input(username)
        password = SQLExample.sanitize_input(password)
        if SQLExample.login_user(username, password):
            print(f"Login successful for user: {username}")
            print(f"User role: {SQLExample.get_user_role(username)}")
        else:
            print(f"Login failed for user: {username}")

        print(f"Sanitized username: {username}")


# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    SQLExample.main(username, password)
