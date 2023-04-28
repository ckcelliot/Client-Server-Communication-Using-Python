import socket
import json
import pickle
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet
import unittest
import os

# Replace with the IP address and port you want to bind the server to
SERVER_IP = "0.0.0.0"
SERVER_PORT = 1234

class TestServer(unittest.TestCase):

    def setUp(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_IP, SERVER_PORT))
        self.server_socket.listen()

    def tearDown(self):
        self.server_socket.close()

    def test_receive_encrypted_file(self):
        # Create a Fernet key for encryption
        key = Fernet.generate_key()
        cipher = Fernet(key)

        # Send some encrypted data to the server
        data = cipher.encrypt(b"hello world")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.sendall(data)
        client_socket.sendall(key)
        client_socket.close()

        # Check that the server saved the decrypted data to a file
        with open("received_file.txt", "rb") as f:
            decrypted_data = f.read().decode()
            self.assertEqual(decrypted_data, "hello world")

        # Clean up the file
        os.remove("received_file.txt")

    def test_receive_json_dict(self):
        # Send some JSON data to the server
        data = json.dumps({"key": "value"}).encode()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.sendall(data)
        client_socket.close()

        # Check that the server printed the correct dictionary
        with self.assertLogs(level='INFO') as cm:
            print_or_save = "p"
            self.assertEqual(print_or_save, "p")
        self.assertIn(f"INFO:root:Received dictionary: {'key': 'value'}", cm.output)

    def test_receive_xml_dict(self):
        # Send some XML data to the server
        data = b"<root><key>value</key></root>"
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.sendall(data)
        client_socket.close()

        # Check that the server printed the correct dictionary
        with self.assertLogs(level='INFO') as cm:
            print_or_save = "p"
            self.assertEqual(print_or_save, "p")
        self.assertIn(f"INFO:root:Received dictionary: {'key': 'value'}", cm.output)

    def test_receive_pickled_dict(self):
        # Send some pickled data to the server
        data = pickle.dumps({"key": "value"})
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.sendall(data)
        client_socket.close()

        # Check that the server printed the correct dictionary
        with self.assertLogs(level='INFO') as cm:
            print_or_save = "p"
            self.assertEqual(print_or_save, "p")
        self.assertIn(f"INFO:root:Received dictionary: {'key': 'value'}", cm.output)

if __name__ == '__main__':
    unittest.main()
