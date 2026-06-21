import requests

username = "Dhruv-Mishra-dm"
url = f"https://api.github.com/users/{username}"

print("Fetching data....")
response = requests.get(url)

data = response.json()

print(f"Name: {data['name']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")