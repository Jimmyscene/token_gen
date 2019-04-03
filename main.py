#!/usr/bin/env python3
from getpass import getpass
import base64

if __name__ == "__main__":
    username = input("Username: ")
    password = getpass().strip()
    token = base64.b64encode(f"${username}:${password}".encode('utf-8'))
    print(token.decode('utf-8'))

