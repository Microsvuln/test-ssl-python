from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'password'
DB_NAME = 'myapp'

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        return "okay"
    
    comment_id = request.args.get('id', '')
    
    if not comment_id.isdigit():
        return "Invalid ID"

    # Connect to the database
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        cursor = conn.cursor()

        query = f"SELECT username, comment FROM comments WHERE id = {comment_id}"
        cursor.execute(query)
        results = cursor.fetchall()

        comments_html = "<h1>Comments</h1>"
        for username, comment in results:
            comments_html += f"<p><strong>{username}:</strong> {comment}</p>"
        
        return render_template_string(comments_html)
    
    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
