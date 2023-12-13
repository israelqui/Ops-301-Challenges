#!/usr/bin/env python3

# Script: Request Library
# Author: Israel Quirola
# Date: Dec 12, 2023

import requests

#response = requests.get('https://www.google.com')

#print(response.status_code)
#print(response.headers)
#print(response.text)

# Function to translate status code to human-readable message
def translate_status_code(code):
    status_codes = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Site Not Found',
        405: 'Method Not Allowed',
        500: 'Internal Server Error'
        # Add more status codes and their messages if needed
    }
    return status_codes.get(code, 'Unknown Status')

# Prompt user for destination URL
destination_url = input("Enter the destination URL: ")

# Prompt user to select HTTP Method
http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the request details and ask for confirmation
print(f"\nRequest about to be sent:\nURL: {destination_url}\nHTTP Method: {http_method}")
confirmation = input("Do you want to proceed? (y/n): ").lower()

if confirmation == 'y':
    # Perform request
    response = requests.request(http_method, destination_url)

    # Translate and print response status code
    print(f"\nResponse Status: {response.status_code} - {translate_status_code(response.status_code)}")

    # Print response headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
else:
    print("Request cancelled.")


# https://www.restapitutorial.com/httpstatuscodes.html
