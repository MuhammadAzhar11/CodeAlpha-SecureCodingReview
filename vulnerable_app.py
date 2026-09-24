import sqlite3
import os

# Hardcoded credentials - BAD PRACTICE
DB_PASSWORD = "admin123"
API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b"

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # SQL Injection vulnerability - user input directly in query
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    conn.close()
    return result

def run_system_command(user_input):
    # Command Injection vulnerability
    os.system("ping " + user_input)

def save_user_data(filename, data):
    # No input validation, path traversal risk
    file = open(filename, "w")
    file.write(data)
    file.close()

def get_user_input():
    # No sanitization
    username = input("Enter username: ")
    password = input("Enter password: ")
    return login(username, password)

if __name__ == "__main__":
    print("Welcome to the login system")
    get_user_input()
