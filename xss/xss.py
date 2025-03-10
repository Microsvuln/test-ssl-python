from flask import Flask, request

app = Flask(__name__)

@app.route('/Servlet', methods=['GET'])
def servlet():
    # Get a query parameter from the user input
    user_input = request.args.get('name', '')

    return f"""
    <html>
        <body>
            <h1>Hello, {user_input}</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
