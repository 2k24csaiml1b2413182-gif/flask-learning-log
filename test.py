import requests
from datetime import datetime, timezone

response = requests.get("https://api.github.com/users/2k24csaiml1b2413182-gif")
data=response.json()
# print(response.status_code)
# print(type(data))
print(data['public_repos'])
# print(data["name"].upper())
# print(data['public_repos'])
# print(data['created_at'])

repos_response = requests.get("https://api.github.com/users/2k24csaiml1b2413182-gif/repos")
repos_data = repos_response.json()
# print(repos_data[0])
# print(repos_data[0]['language'])
# print(type(repos_data))
languages=[repo['language'] for repo in repos_data]
language_counts={}

for lang in languages:
    if lang is None:
        continue
    if lang in language_counts:
        language_counts[lang]+=1
    else :
        language_counts[lang]=1

print(language_counts)
top_language=max(language_counts, key=language_counts.get)
print (top_language)

created_at_str=data['created_at']
created_at_date = datetime.fromisoformat(created_at_str.replace('Z','+00:00'))

now = datetime.now(timezone.utc)
account_age_days = (now - created_at_date).days
account_age_years = account_age_days // 365

print(account_age_days)
print(account_age_years)

if account_age_years >= 1:
    account_age_display = f"{account_age_years} years on GitHub"
else:
    account_age_display = f"{account_age_days} days on GitHub"

print(account_age_display)
# now = datetime.now(timezone.utc)

# most_recent_push = None

# for repo in repos_data:
#     pushed_at_str = repo['pushed_at']
#     pushed_at_date = datetime.fromisoformat(pushed_at_str.replace('Z', '+00:00'))
    
#     if most_recent_push is None or pushed_at_date > most_recent_push:
#         most_recent_push = pushed_at_date

# print(most_recent_push)
# difference = now - most_recent_push
# is_active = difference.days < 90
# print(difference.days)
# print(is_active)