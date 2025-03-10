from flask import Flask, request

app = Flask(__name__)

@app.route('/simple-post', methods=['POST'])
def handle_post_request():
    input_data = request.form.get('input')
    return f"""
    <html>
        <head><title>Simple POST Response</title></head>
        <body>
            <h1>You sent:</h1>
            <p>{input_data}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
