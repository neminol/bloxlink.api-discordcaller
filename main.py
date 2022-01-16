import requests

introduction = print("Welcome to the script! I believe you're here to use the Bloxlink API to check your Discord ID for any accounts used by Bloxlink(and it's API).")
introduction2 = print("Let's get started, shall we?")

id = int(input("Please print your discord ID here:"))

request = requests.get(f'https://api.blox.link/v1/user/{id}')

print("Here are the results!")
result = print(request.text)
