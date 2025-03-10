import sys
import urllib.parse
import requests

def log_request(log):
    # Simulating logging of request data
    print(f"Log: {log}")

def main():
    data = sys.argv[1]
    target = f"http://example.com/api?target={urllib.parse.quote(data)}"

    try:
        response = requests.get(target)

        status = response.status_code
        print(f"Status: {status}")

        if status == 200:
            print(f"Response: {response.text}")
        else:
            print("Error: Unable to fetch data")

        log = f"Request made to: {target} with response status: {status}"
        log_request(log)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
