import requests

response = requests.get("https://api.github.com/users/2k24csaiml1b2413182-gif")
data=response.json()
print(type(data))
print(data["name"].upper())
print(data['public_repos'])
print(data['created_at'])

repos_response = requests.get("https://api.github.com/users/2k24csaiml1b2413182-gif/repos")
repos_data = repos_response.json()
print(len(repos_data))
print(repos_data[0]['language'])
print(type(repos_data))
languages=[repo['language'] for repo in repos_data]
print(languages)