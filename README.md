# Client-Server-Communication-Using-Python

This implementation simulates the client server communication using python. Sockets have been used to send data each other. Apart from that the server can handle evrypted text file as well as dictionary when sending messages. The program also prompts the server to choose whether to print the recieved message on the console or save it in a file. The code has been written according to the PEP Standards and exception handling has been inculcated as well. Unit test for each code file are also included.

# How to use the program.
The program is launched in two stages, first, launch server.py and that should open the server and assign a socket to listen for client entry. Second, launch client.py which should transfer a file to the server. The server terminal will now give you the option to save or print the information that is received. 

You can change the data being sent from a text file to a dictionary by commenting out line 31 and removing the comment hash from line 28. You can change the encryption handling by changing the variable value on line 31 from json to either binary or XML. 

# How to use testing scripts.
Within client.py there is a set of tests that have been commented out. These tests can be run by removing the triple apostrophes at the beginning and end of these sections.

To use client_unit_test.py, you must launch server.py before running the test script as the tests require a server socket to be open before running. To use server_unit_test.py, you can run this as a standalone file as it opens and closes a socket server as part of its setup and teardown test functions.

# Task requirements
- Build a simple client/server network
- Create a dictionary, populate it, serialize it and send it to a server
- Create a text file and send it to a server
- With the dictionary, the user should be able to set the pickling format to one of the following: binary, JSON and XML
- The user will need to have the option to encrypt the text in a text file
- The server should have a configurable option to print the contents of the sent items to the screen and or to a file
- The server will need to be able to handle encrypted contents
- The client and server can be on separate machines or on the same machine.
- Make sure that the code is written to PEP standard and uses exception handling to handle potential errors
- Write unit tests
- Upload the project to the source control website

# Directory Tree
```
C:\Users\rohba\OneDrive\Desktop\Fiv 4\
├── Task requirements.docx
├── client.py
├── client_unit_test.py
├── received_file.txt
├── sample.txt
├── server.py
├── server_unit_test.py
├── tree.txt
├── Commit Logs.txt
└── requirements.txt
```
