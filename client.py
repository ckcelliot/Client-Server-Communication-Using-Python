import socket
import json
import pickle
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Replace with the IP address and port of the server
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

# Replace with the path to the file you want to send
FILE_PATH = "sample.txt"

try:
    with open(FILE_PATH, "r") as file:
        file_contents = file.read()
except IOError as e:
    print("Error opening file:", e)
    exit()

# Choose which type of data to send
# A File type
data = file_contents
        
# # Create a dictionary and populate it with data
# # A Dictionary type
# data = {"name": "John", "age": 30, "city": "New York"}

# Set the pickling format to one of binary, JSON, or XML
pickling_format = "json"  # Possible values: "binary", "json", "xml"

# Serialize the dictionary to the specified pickling format
if pickling_format == "binary":
    serialized_data = pickle.dumps(data)
elif pickling_format == "json":
    serialized_data = json.dumps(data).encode()
elif pickling_format == "xml":
    root = ET.Element("data")
    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    serialized_data = ET.tostring(root)
else:
    raise ValueError("Invalid pickling format specified")

# Create a socket and connect to the server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
except socket.error as e:
    print("Error connecting to server:", e)
    exit()

# Check if the data is a dictionary or a file
if isinstance(data, dict):
    # Send the serialized data to the server
    try:
        client_socket.sendall(serialized_data)
    except socket.error as e:
        print("Error sending data to server:", e)
        client_socket.close()
        exit()
else:
    # Encrypt the file contents using Fernet encryption
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_contents = cipher.encrypt(file_contents.encode())
    # Send the encrypted file contents and the encryption key to the server
    try:
        client_socket.sendall(encrypted_contents)
        client_socket.sendall(key)
    except socket.error as e:
        print("Error sending data to server:", e)
        client_socket.close()
        exit()

# Close the socket
client_socket.close()
