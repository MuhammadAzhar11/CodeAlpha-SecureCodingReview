import sqlite3
import os
import subprocess
import re

# Credentials loaded from environment variables (not hardcoded)
DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_KEY = os.environ.get("API_KEY")

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Parameterized query - prevents SQL Injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    conn.close()
    return result

def run_system_command(user_input):
    # Input validated - only allows safe characters, prevents Command Injection
    if not re.match("^[a-zA-Z0-9.]+$", user_input):
        print("Invalid input")
        return
    subprocess.run(["ping", "-c", "4", user_input], check=False)

def save_user_data(filename, data):
    # Filename sanitized to prevent path traversal
    safe_filename = os.path.basename(filename)
    with open(safe_filename, "w") as file:
        file.write(data)

def get_user_input():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return login(username, password)

if __name__ == "__main__":
    print("Welcome to the login system")
    get_user_input()
