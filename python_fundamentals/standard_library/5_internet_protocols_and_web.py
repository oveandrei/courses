'''urllib.request'''

import urllib.request

# Download and read a webpage
with urllib.request.urlopen("https://example.com") as response:
    html = response.read()
    print(html.decode()) # Outputs HTML content

# Download a file
urllib.request.urlretrieve("https://example.com/image.png", 'image.png')

# Basic for HTTP operations -- no third-party dependencies


'''smtplib'''

import smtplib

# Send a simple email
sender = "you@example.com"
receiver = "friend@example.com"
message = """\
Subject: Hi There

This is a test email from Python."""

with smtplib.SMTP("smtp.exampl.com", 587) as server:
    server.starttls() # Upgrade to secure connection
    server.login("you@example.com", "password") # Login
    server.sendmail(sender, receiver, message)
# Works well with email.message for more complex email content


'''email.message'''

from email.message import EmailMessage

# Construct an email message with subject and body
msg = EmailMessage()
msg['Subject'] = "Meeting Reminder"
msg['From'] = "you@example.com"
msg['To'] = "friend@example.com"
msg.set_content("Don't forget our meeting at 10am tomorrow.")

# Send it using smtplib
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("you@example.com", "password")
    server.send_message(msg)
# You can also use msg.add_attachment() for files.


'''json'''

import json

# Dictionary to JSON string
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str) # {"name": "Alice", "age": 30}

# JSON string to dictionary
parsed = json.loads(json_str)
print(parsed['name']) # Alice

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read JSON from file
with open('data.json') as f:
    loaded = json.load(f)
    print(loaded)


'''xmlrpc.client'''

import xmlrpc.client

# Connect to an XML-RPC server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call remote method
result = server.add(5, 3)
print(result) # Should print 8 if server defines `add`


'''xmlrpc.server'''

from xmlrpc.server import SimpleXMLRPCServer

# Define a function to expose
def add(x, y):
    return x + y

# Create server and register the function
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")

print("Server running on port 8000...")
server.serve_forever()
# You can call this server using xmlrpc.client as show above.