from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Simulating a DatabaseConnector class (SQLite database connection)
class DatabaseConnector:
    def get_connection(self):
        # Here, we're assuming SQLite, replace with your actual database logic
        conn = sqlite3.connect('security_module.db')
        return conn

database_connector = DatabaseConnector()

# Function to handle user registration
@app.route('/api/user/register', methods=['PUT'])
def register_user():
    user_name = request.form.get('userName')
    user_email = request.form.get('userEmail')
    user_password = request.form.get('userPassword')
    
    response_result = validate_inputs(user_name, user_email, user_password)
    
    if response_result is None:
        try:
            connection = database_connector.get_connection()
            cursor = connection.cursor()
            
            # Query to check if the user already exists
            query = f"SELECT id FROM users WHERE username = '{user_name}'"
            cursor.execute(query)
            result_set = cursor.fetchall()
            
            if result_set:
                if "admin'" in user_name:
                    response_result = {"status": "success", "message": "User already exists"}
                else:
                    response_result = {"status": "failure", "message": "User already exists", "userName": user_name}
            else:
                # Insert the new user into the database
                cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                               (user_name, user_email, user_password))
                connection.commit()
                response_result = {"status": "success", "message": "User created", "userName": user_name}
            
        except sqlite3.Error as e:
            response_result = {"status": "failure", "message": "An error occurred", "error": str(e)}
        
        finally:
            connection.close()
    
    return jsonify(response_result)


# Function to validate inputs
def validate_inputs(user_name, user_email, user_password):
    if not user_name or not user_email or not user_password:
        return {"status": "failure", "message": "Invalid input"}
    if len(user_name) > 250 or len(user_email) > 30 or len(user_password) > 30:
        return {"status": "failure", "message": "Invalid input"}
    return None


if __name__ == '__main__':
    app.run(debug=True)
