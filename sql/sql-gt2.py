from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

# Simulating a DataSourceProvider class (SQLite database connection)
class DataSourceProvider:
    def get_connection(self):
        # Here, we're assuming SQLite, replace with your actual database logic
        conn = sqlite3.connect('security_module.db')
        return conn

data_source_provider = DataSourceProvider()

# Utility class for query result formatting
class QueryResult:
    @staticmethod
    def failure(handler, output=""):
        return {"status": "failure", "handler": str(handler), "output": output}

    @staticmethod
    def success(handler):
        return {"status": "success", "handler": str(handler), "output": "", "feedback": "", "feedbackArgs": []}

# Utility to format results (mocked)
class ResultFormatter:
    @staticmethod
    def format_results(results, results_meta_data):
        columns = [results_meta_data.getColumnName(i+1) for i in range(results_meta_data.getColumnCount())]
        rows = []
        while results.next():
            rows.append([results.getString(col) for col in columns])
        return str(columns) + "\n" + str(rows)

# Function to handle the query
@app.route('/UserData/query', methods=['POST'])
def execute_query():
    user_input = request.form.get('user_input')
    return jsonify(perform_query(user_input))

def perform_query(input_query):
    query = ""
    try:
        connection = data_source_provider.get_connection()
        contains_union = check_union_usage(input_query)
        query = f"SELECT * FROM user_data WHERE last_name = '{input_query}'"
        return process_query(connection, query, contains_union)
    except Exception as e:
        return QueryResult.failure(UserDataQueryHandler, f"{e} Your query was: {query}")

def check_union_usage(input_query):
    # Check for UNION SQL injection pattern (case-insensitive)
    return bool(re.match(r"(?i)(^[^-/*;)]*)(\s*)UNION(.*$)", input_query))

def process_query(connection, query, contains_union):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            return QueryResult.failure(UserDataQueryHandler, f"Query failed. No results. Your query was: {query}")

        results_meta_data = cursor.description
        output = []
        success_message = generate_success_message(contains_union)

        output.append(ResultFormatter.format_results(cursor, results_meta_data))

        # Simulating last row check
        if "dave" not in str(results) or "passW0rD" not in str(results):
            return QueryResult.failure(UserDataQueryHandler, f"{output} Your query was: {query}")

        output.append(success_message)
        return QueryResult.success(UserDataQueryHandler).update({"feedback": "query.success", "feedbackArgs": output, "output": f"Your query was: {query}"})

    except sqlite3.Error as e:
        return QueryResult.failure(UserDataQueryHandler, f"{e} Your query was: {query}")

def generate_success_message(used_union):
    return "Well done! Can you also figure out another approach by " + \
        ("appending a new SQL statement?" if used_union else "using a UNION clause?")

if __name__ == '__main__':
    app.run(debug=True)
