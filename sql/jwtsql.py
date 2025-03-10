import base64
import json
import sqlite3
from flask import Flask, request, jsonify
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

app = Flask(__name__)

# Simulating a LessonDataSource (SQLite database connection)
def get_db_connection():
    conn = sqlite3.connect('lesson_data.db')
    return conn

@app.route('/JWT/kid/follow/<string:user>', methods=['POST'])
def follow(user):
    if user == "UserA":
        return "Following yourself seems redundant", 200
    else:
        return "You are now following UserB", 200

@app.route('/JWT/kid/delete', methods=['POST'])
def reset_votes():
    token = request.args.get('token')

    if not token:
        return jsonify({"status": "failed", "message": "jwt-invalid-token"}), 400

    try:
        error_message = None
        decoded_jwt = None

        def resolve_signing_key(kid):
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT key FROM jwt_keys WHERE id = ?", (kid,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    return base64.b64decode(row[0])
            except sqlite3.Error as e:
                return str(e)

        # Parse the JWT token
        decoded_jwt = jwt.decode(
            token,
            options={"verify_signature": False},
            algorithms=["HS256"],  # Adjust if needed
            signing_key=resolve_signing_key
        )
        
        if error_message:
            return jsonify({"status": "failed", "message": error_message}), 400

        username = decoded_jwt.get("username")
        if username == "UserA":
            return jsonify({"status": "failed", "message": "jwt-final-usera-account"}), 400
        if username == "UserB":
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "failed", "message": "jwt-final-not-userb"}), 400

    except (ExpiredSignatureError, InvalidTokenError) as e:
        return jsonify({"status": "failed", "message": "jwt-invalid-token", "output": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
