import socket
import json
import pickle
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Replace with the IP address and port you want to bind the server to
SERVER_IP = "0.0.0.0"
SERVER_PORT = 1234

# Create a socket and bind it to the specified IP address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

# Writing on console to mark server starting
print("Server started.....")

# Listen for incoming connections
server_socket.listen()

# Accept a connection from a client
client_socket, client_address = server_socket.accept()

# Receive the data from the client
data = client_socket.recv(1024)



# Check if the data is a dictionary or a file
if isinstance(data, bytes):
    try:
        # Try to decrypt the data as Fernet encryption
        key = client_socket.recv(1024)
        cipher = Fernet(key)
        decrypted_contents = cipher.decrypt(data)
        print("Received decrypted file contents:")
        # print(decrypted_contents.decode())

        SAVE_PATH = "received_file.txt"

        print_or_save = input("Do you want to print the data or save it to a file? (P/S): ")

        if print_or_save.lower() == "s":
            # Save the file contents to disk
            with open(SAVE_PATH, "wb") as file:
                file.write(decrypted_contents.decode().encode())

        elif print_or_save.lower() == "p":
                print(decrypted_contents.decode())

        else:
            print("Invalid option selected. Please try again.")
        
        
    except:
        # If unsuccessful, the data is not encrypted
        print("Received file data:")
        # Replace with the path and filename where you want to save the text file
        SAVE_PATH = "received_file.txt"

        print_or_save = input("Do you want to print the data or save it to a file? (P/S): ")

        if print_or_save.lower() == "s":
            # Save the file contents to disk
            with open(SAVE_PATH, "wb") as file:
                file.write(data)

        elif print_or_save.lower() == "p":
                print(data)

        else:
            print("Invalid option selected. Please try again.")
    
        
else:
    try:
        # Try to deserialize the data as JSON
        data_dict = json.loads(data)

        SAVE_PATH = "received_file.txt"
        print_or_save = input("Do you want to print the data or save it to a file? (P/S): ")

        if print_or_save.lower() == "s":
            # Save the file contents to disk
            with open(SAVE_PATH, "wb") as file:
                file.write(data)

        elif print_or_save.lower() == "p":
            print(f"Received dictionary: {data_dict}")

        else:
            print("Invalid option selected. Please try again.")


    except (json.JSONDecodeError, UnicodeDecodeError):
        try:
            # Try to deserialize the data as XML
            root = ET.fromstring(data)
            data_dict = {}
            for child in root:
                data_dict[child.tag] = child.text

            SAVE_PATH = "received_file.txt"
            print_or_save = input("Do you want to print the data or save it to a file? (P/S): ")

            if print_or_save.lower() == "s":
                # Save the file contents to disk
                with open(SAVE_PATH, "wb") as file:
                    file.write(data)

            elif print_or_save.lower() == "p":
                print(f"Received dictionary: {data_dict}")

            else:
                print("Invalid option selected. Please try again.")

        except:
            # If unsuccessful, the data is serialized using pickle
            data_dict = pickle.loads(data)

            SAVE_PATH = "received_file.txt"
            print_or_save = input("Do you want to print the data or save it to a file? (P/S): ")

            if print_or_save.lower() == "s":
                # Save the file contents to disk
                with open(SAVE_PATH, "wb") as file:
                    file.write(data)

            elif print_or_save.lower() == "p":
                print(f"Received dictionary: {data_dict}")

            else:
                print("Invalid option selected. Please try again.")

# Close the connection
client_socket.close()



