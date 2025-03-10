from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/safeServlet', methods=['GET'])
def safe_servlet():
    user_input = request.args.get('name', '')

    # Escape the input to prevent XSS
    escaped_input = escape(user_input)

    return f"""
    <html>
        <body>
            <h1>Hello, {escaped_input}</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
