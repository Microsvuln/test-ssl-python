import ssl
import socket

# Using the deprecated ssl.wrap_socket method (not recommended)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wrapped_socket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)
wrapped_socket.connect(("example.com", 443))
wrapped_socket.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print(wrapped_socket.recv(1024))
wrapped_socket.close()

# Using SSLContext (recommended approach)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_default_certs()

with socket.create_connection(("example.com", 443)) as sock:
    with context.wrap_socket(sock, server_hostname="example.com") as secure_sock:
        secure_sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        print(secure_sock.recv(1024))
